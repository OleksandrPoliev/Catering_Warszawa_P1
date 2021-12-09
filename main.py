# This is a sample Python script.
#
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# def palidrome(x:int):
#     "поняв як це працює ми порівнюєм якби масив елементів  з кожним елементом з кінця за допомогою крока   "
#         return str(x) == str(x)[::-1]
#


# x="1123"
#
# print(str(x[::-1]))

# def isValid(s) -> bool:
#     stack = []
#     d = {'(': ')', '{': '}', '[': ']'}
#     for i in s :
#         if i in ["(","{","{"]:
#             stack.append(i)
#         elif len(stack) == 0 or d[stack.pop()] != i:  # 2
#             return False
#         return len(stack) == 0
# print(isValid("()[]{}"))

# def square_digits(num):
#     rel=""
#     for i in str(num) :
#         rel+=str(int(i)+int(i))
#     return int(rel)

# def find_outlier(integers):
#     list=[x for x in integers if x%2==1]
#     list2=[x for x in integers if x%2==0]
#     return list[0] if len(list)<len(list2) else list2[0]
#
#
# print(find_outlier([6849509, 5595221, 9617227, -8931957, -4862685, -608441, 3300487, 6414523, -9005195, 9868337, 7332727, -2248845, 1374687, 4843063, 3441195, 7946451, 5402143, -9576269, -8103309, -7845303, 9472941, 5219617, -2356507, -1931039, -2733456, -7427601, 5937219, -2421493, -4198827, 7768063, 1367433, 7917245, 7946989, 8169495]))
# print(2733456%2)

# def filter_list(l:list):
#   return [x for x in l if isinstance(x, int) and x >-1]
#
# from numpy import unique
# def first_non_repeating_letter(string):
#      list_my=[x for x in string if x==x ]
#      runer=0
#      runer1=1
#      while True:
#          if list_my[runer]==list_my[runer1]:
#              list_my[runer].
#
# print(first_non_repeating_letter('moonmen'))


def highest_rank ( arr ):
    list=[]
    f_list=[]
    for item in arr:
        for elem in arr :
            if item == elem :
                list.append(elem)
        if len(f_list)< len(list):
            f_list= list
            list=[]
        else:
            list=[]
    return f_list[0]
print(highest_rank([12, 8, 8, 12, 7, 8, 4, 8, 12]))
