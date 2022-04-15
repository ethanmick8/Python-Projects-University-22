# Lists1 Assignment - Python 1
# Author: Ethan Mick
# Instructor: Dale Musser
# Description: This program just performs various list operations on a list called "foods".

def display_list(label, items):
    print(label)
    for element in items:
        print(element)

foods = ['pizza', 'salad', 'hamburger', 'steak', 'apple', 'orange']

display_list('foods in original order:', foods)

foods.sort()
display_list('foods in ascending alphabetical order:', foods)

foods.sort(reverse=True)
display_list('foods in descending alphabetical order:', foods)

foods2 = sorted(foods)
display_list('foods2 in ascending alphabetical order:', foods2)

foods.reverse()
display_list('foods in ascending alphabetical order(again):', foods)

foods.append('carrot')
foods.append('milk')
display_list("sorted foods with carrot and milk appended to end:", foods)

foods.sort()
display_list('foods in ascending alphabetical order(again again):', foods)

pizza_index = foods.index('pizza')
print("Pizza is at index", pizza_index)

foods.insert(pizza_index, 'fries')
pizza_index = foods.index('pizza')
print("Pizza is now at index", pizza_index)