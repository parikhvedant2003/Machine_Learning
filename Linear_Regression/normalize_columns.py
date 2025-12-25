from stats import min_value, max_value

def normalize_columns(column):
    min_val, max_val = min_value(column), max_value(column)
    return [round((val - min_val) / (max_val - min_val), 2) for val in column]
