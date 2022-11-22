# Problem Statement:-
# You visited a restaurant called CodeWithHarry,
# and the food items in that restaurant are sorted, based on their amount of calories.
# You have to reverse this list of food items containing calories.
#
# You have to use the following three methods to reserve a list:
# 1) In-built method of python
# 2) List name [::-1] slicing trick
# 3) Swap the first element with the last one and second element with second last one and so on like,
#       [6 7 8 34 5] -> [5 34 8 7 6]

#   Input:
#       Take a list as an input from the user
#       [5, 4, 1]

#   Output:
#       [1, 4, 5]
#       Print only when All three methods give the same results!

try:
    l1 = input('Please create a list in the form of 1, 2, 5, ... :\n')
    list1 = list(map(int, l1.split(',')))
    # splits the list and using map function the list will be turned to integers list and converts back to list

    method1 = list1.copy()
    method1.reverse()

    method2 = list1[::-1].copy()

    method3 = list1.copy()
    for i in range(len(method3)//2):    # //2 BECAUSE AN INT IS NEEDED; IF IT'S NOT 2 THEN THE LIST WILL GO BACK TO NORMAL
        method3[i], method3[len(method3)-i-1] = method3[len(method3)-i-1], method3[i]
    #   FIRST POSITION, SECOND POSITION = SECOND POSITION, FIRST POSITION

    if method1 == method2 and method2 == method3:
        print(f'Original list {list1}\n First list {method1}\n Second list {method2}\n Third list {method3}')
        print('All lists reversed are same!')
except:
    print('Incorrect Value has been entered')