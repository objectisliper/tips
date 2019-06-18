
array = [{'text': 'test 1', 'id': 1, 'parent': None}, {'text': 'test 1', 'id': 9, 'parent': None}, {'text': 'test 2', 'id': 2, 'parent': 1}, {'text': 'test 2', 'id': 3, 'parent': 1}, 
        {'text': 'test 2', 'id': 4, 'parent': 1}, 
        {'text': 'test 3', 'id': 5, 'parent': 2}, {'text': 'test 3', 'id': 6, 'parent': 3}, {'text': 'test 4', 'id': 7, 'parent': 6}, {'text': 'test 5', 'id': 8, 'parent': 7},
        {'text': 'test 2', 'id': 2, 'parent': 9}]

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
        new_choice = choice
        
        existed_choice = next((existed_choice for existed_choice in new_array[column] if existed_choice['id'] == new_choice['id']), None)
        
        if existed_choice:
            existed_choice['parents'].append = choice['parent']
        else:
            if len(choice['parent']) > 0:
                new_choice['parents'] = []
                new_choice['parents'].append(choice['parent'])
                new_choice.pop('parent', None)
            else:
                new_choice.pop('parent', None)
            new_array[column].append(new_choice)

print(new_array)
