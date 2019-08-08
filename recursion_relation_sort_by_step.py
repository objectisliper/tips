
array = [{'text': 'test 1', 'id': 1, 'parent': None}, {'text': 'test 1', 'id': 9, 'parent': None}, {'text': 'test 2', 'id': 2, 'parent': 1}, {'text': 'test 2', 'id': 3, 'parent': 1}, 
        {'text': 'test 2', 'id': 4, 'parent': 1}, 
        {'text': 'test 3', 'id': 5, 'parent': 2}, {'text': 'test 3', 'id': 6, 'parent': 3}, {'text': 'test 4', 'id': 7, 'parent': 6}, {'text': 'test 5', 'id': 8, 'parent': 7},
        {'text': 'test 2', 'id': 2, 'parent': 9},{'text': 'test3', 'id': 6, 'parent': 4}]

def sort(choice, new_array, i = 0):
    for element in array:
        if element['parent'] == choice['id']:
            new_array = sort(element, new_array, i = i+1)
    
    if i in new_array:
        new_array[i].append(choice)
    else:
        new_array[i] = [choice]
    
    return new_array

dict = {}

for choice in array:
    
    if choice['parent'] is None:
        dict = sort(choice, dict)

new_array = []


for column in dict:
    
    new_array.append([])
    
    for choice in dict[column]:
        new_choice = choice.copy()
        
        
        existed_choice = next((existed_choice for existed_choice in new_array[column] if existed_choice['id'] == new_choice['id']), None)
        
        choice_parent_index = None
        
        if column > 0:
            choice_parent_index = next((parent_index for parent_index, parent in enumerate(new_array[column-1]) if parent['id'] == choice['parent']), None)
        
        if existed_choice is not None:
            existed_choice['parents'].append(choice_parent_index)
            existed_choice['parents'] = list(set(existed_choice['parents']))
        else:
            if choice_parent_index is not None:
                new_choice['parents'] = []
                new_choice['parents'].append(choice_parent_index)
                new_choice.pop('parent', None)
            else:
                new_choice.pop('parent', None)
            new_array[column].append(new_choice)

print(new_array)
