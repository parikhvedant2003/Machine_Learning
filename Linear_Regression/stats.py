from random import randint

def min_value(column):
    return min(column)

def max_value(column):
    return max(column)

def mean(column):
    return round(sum(column) / len(column), 2)

def mean_square_error(ssr, n):
    return round((ssr / n), 2)

def random_m_c_generator(no_of_times):
    output = []
    for _ in range(no_of_times):
        output.append([randint(0, 1000) / 100, randint(0, 100) / 100])
    return output

def find_model(normalize_input_training_data, normalize_output_training_data):
    m_c_pairs = random_m_c_generator(100)
    best_pair, min_ssr, best_fitted_output = [-1, -1], float('inf'), normalize_output_training_data
    for pair in m_c_pairs:
        slope, intercept = pair
        ssr, predicted_op = 0, []
        for ip, actual_op in zip(normalize_input_training_data, normalize_output_training_data):
            p_op = (slope * ip) + intercept
            ssr += (actual_op - p_op) ** 2
            predicted_op.append(p_op)
        if min_ssr >= ssr:
            best_pair = [slope, intercept]
            min_ssr = ssr
            best_fitted_output = predicted_op
    return best_pair[0], best_pair[1], min_ssr, best_fitted_output

def evaluate_model(normalize_input_testing_data, slope, intercept, normalize_output_testing_data):
    ssr = 0
    predicted_op = []
    for ip, op in zip(normalize_input_testing_data, normalize_output_testing_data):
        p_op = (slope * ip) + intercept
        ssr += (op - p_op) ** 2
        predicted_op.append(p_op)
    return predicted_op, ssr