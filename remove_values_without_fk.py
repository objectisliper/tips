array_with_values = ['First', 'NotExist', 'Second', 'NotExist', 'Third']

array_with_fk = [{'parents': [0]}, {'parents': [2]}, {'parents': [4]}, {'parents': [0, 2]}, {'parents': [0, 4]},
                 {'parents': [2, 4]}, {'parents': [0, 2, 4]}]


def remove_values_without_fk(array_of_value: list, array_of_fk: list, fk_name: str) -> (list, list):
    # Get values without fk

    index_of_values_without_fk = []

    for index_of_value, value in enumerate(array_of_value):

        is_without_fk = all(index_of_value not in fk[fk_name] for index, fk in enumerate(array_of_fk))

        if is_without_fk:
            index_of_values_without_fk.append(index_of_value)

    array_of_value_copy = array_of_value.copy()

    array_of_fk_copy = array_of_fk.copy()

    index_of_values_without_fk.sort(reverse=True)

    # Remove values without fk

    for index in index_of_values_without_fk:

        array_of_value_copy.pop(index)

        for fk in array_of_fk_copy:

            for parent_index, parent in enumerate(fk['parents']):

                if parent > index:
                    fk['parents'][parent_index] = parent - 1

    return array_of_value_copy, array_of_fk_copy


final_array_of_value, final_array_of_fk = remove_values_without_fk(array_with_values, array_with_fk, 'parents')

print(final_array_of_value, final_array_of_fk)