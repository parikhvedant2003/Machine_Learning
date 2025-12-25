import matplotlib.pyplot as plt

from load_data import load_data
from normalize_columns import normalize_columns
from train_test_split import train_test_split
from stats import find_model, mean_square_error, evaluate_model

df = load_data(r"C:\Users\LENOVO\Desktop\Linear_Regression\Housing.csv")
print(df.columns)

train_split_percentage = 80

training_data, testing_data = train_test_split(df, train_split_percentage)

# Uni Variate - 2D

input_training_data = training_data["area"].tolist()
output_training_data = training_data["price"].tolist()

input_testing_data = testing_data["area"].tolist()
output_testing_data = testing_data["price"].tolist()

normalize_input_training_data = normalize_columns(input_training_data)
normalize_output_training_data = normalize_columns(output_training_data)

normalize_input_testing_data = normalize_columns(input_testing_data)
normalize_output_testing_data = normalize_columns(output_testing_data)

# plt.scatter(input_training_data, output_training_data)
# plt.show()

# plt.scatter(normalize_input_training_data, normalize_output_training_data)
# plt.show()

slope, intercept, min_ssr, predicted_training_output = find_model(normalize_input_training_data, normalize_output_training_data)
train_mse = mean_square_error(min_ssr, len(predicted_training_output))
print("Training Data Stats:")
print(f"slope is {slope}")
print(f"intercept is {intercept}")
print(f"min_ssr is {min_ssr}")
print(f"train_mse is {train_mse}")

plt.scatter(normalize_input_training_data, normalize_output_training_data)
plt.plot(normalize_input_training_data, predicted_training_output)
plt.show()

predicted_testing_output, test_ssr = evaluate_model(normalize_input_testing_data, slope, intercept, normalize_output_testing_data)
test_mse = mean_square_error(test_ssr, len(predicted_testing_output))
print("Testing Data Stats:")
print(f"test_ssr is {test_ssr}")
print(f"test_mse is {test_mse}")

plt.scatter(normalize_input_testing_data, normalize_output_testing_data)
plt.plot(normalize_input_testing_data, predicted_testing_output)
plt.show()
