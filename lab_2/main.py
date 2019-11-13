"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows, num_cols):
    matrix = []
    if num_cols is None or num_rows is None:
        return matrix
    if not isinstance(num_rows, int) or not isinstance(num_cols, int):
        return matrix
    matrix = [[0] * num_cols for i in range(num_rows)]
    return matrix



def initialize_edit_matrix(matrix, add_weight, remove_weight):
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int):
        return list(matrix)
    if add_weight is None or remove_weight is None:
        return list(matrix)
    if [] in matrix:
        return list(matrix)
    if not matrix or not matrix[0]:
        return list(matrix)

    for i in range(1, len(matrix)):
        matrix[0][0] = 0
        matrix[i][0] = matrix[i - 1][0] + remove_weight
    for j in range(1, len(matrix[0])):
        matrix[0][0] = 0
        matrix[0][j] = matrix[0][j - 1] + add_weight
    return list(matrix)


def minimum_value(numbers):
    return min(numbers)


def fill_edit_matrix(matrix, add_weight, remove_weight, substitute_weight, original_word, target_word):

    if [] in matrix:
        return list(matrix)
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int):
        return list(matrix)
    if original_word is None:
        return list(matrix)
    if target_word == '':
        return list(matrix)


    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            rem_weight = matrix[i - 1][j] + remove_weight
            ad_weight = matrix[i][j - 1] + add_weight
            sub = substitute_weight
            if original_word[i - 1] == target_word[j - 1]:
                sub = 0
            sub_weight = matrix[i - 1][j - 1] + sub
            matrix[i][j] = minimum_value((rem_weight, ad_weight, sub_weight))
    return list(matrix)

def find_distance(original_word,
                  target_word,
                  add_weight,
                  remove_weight,
                  substitute_weight):
    if not isinstance(original_word, str) or not isinstance(target_word, str):
        return -1
    if not isinstance(add_weight, int) or not isinstance(remove_weight, int) or not isinstance(substitute_weight, int):
        return -1

    matrix = generate_edit_matrix(len(original_word) + 1, len(target_word) + 1)
    initialize_edit_matrix(tuple(matrix), add_weight, remove_weight)
    fill_edit_matrix(tuple(matrix), add_weight, remove_weight, substitute_weight, original_word, target_word)
    return matrix[len(original_word)][len(target_word)]


def save_to_csv(matrix: tuple, path_to_file) -> None:
    with open(path_to_file, 'w') as f:
        for row in matrix:
            line = ''
            for i in row:
                line += str(i)
                line += ','
            f.write(line[:-1] + '\n')
    return None


def load_from_csv(path_to_file: str) -> list:
    with open(path_to_file) as f:
        matrix = []
        full_file = f.read().split('\n')[:-1]
        for line in full_file:
            matrix.append(line.split(','))
    return full_file