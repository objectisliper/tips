array = [{'text': 'test 1', 'id': 1, 'parent': None}, {'text': 'test 2', 'id': 2, 'parent': 1}, {'text': 'test 2', 'id': 3, 'parent': 1}, 
        {'text': 'test 2', 'id': 4, 'parent': 1}, 
        {'text': 'test 3', 'id': 5, 'parent': 2}, {'text': 'test 3', 'id': 6, 'parent': 3}, {'text': 'test 4', 'id': 7, 'parent': 6}, {'text': 'test 5', 'id': 8, 'parent': 7}]

def sort(choice, new_array = {}, i = 0):
    for element in array:
        if element['parent'] == choice['id']:
            new_array = sort(element, new_array, i = i+1)
    
    if i in new_array:
        new_array[i].append(choice)
    else:
        new_array[i] = [choice]
    
    return new_array

dict= sort(array[0])

print(dict)
