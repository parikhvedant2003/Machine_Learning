from random import randint

def train_test_split(df, train_split_percentage):
    total_rows = len(df)
    train_size = int((total_rows * train_split_percentage) / 100)

    train_indices = []
    test_indices = []

    while len(train_indices) < train_size:
        idx = randint(0, total_rows - 1)
        if idx not in train_indices:
            train_indices.append(idx)

    for i in range(total_rows):
        if i not in train_indices:
            test_indices.append(i)

    train_df = df.iloc[train_indices]
    test_df = df.iloc[test_indices]

    return train_df, test_df
