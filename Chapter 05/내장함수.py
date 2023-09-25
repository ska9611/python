# a = 13
# print(abs(a))


# alpha = ord('A')
# list1 = []

# for  i  in  range(1,27):
#     list1.append(chr(alpha))
#     alpha += 1
# print(list1)




# print(chr(67))




# str1 = "ABCDEFGHIJKLMNOVQRSTUVWXYZ"
# list1 = list(str1) 
# print(list1)


# print(dir([1,3,1,5,4]))


# a = 10
# b = 3
# mok = a // b
# na = a % b
# mok, na = divmod(a,b)
# print(divmod(a,b))




# list1 = [10,2,5,7,54,51,584,4]
# for i,v  in enumerate(list1):
#     print(f'list1[{i}] = {v}')

# str1 = "ABCDEFGHIJKLMNOVQRSTUVWXYZ"
# list1 = list(str1)
# for i,v in enumerate(list1):
#     print(i,v)



#filter 함수

# def is_even(num):
#     return num % 2 == 0
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))



# list1 = [-10,20,-78,60,185,-47]
# def poss(data_1):
#     result = []
#     for i in data_1: 
#         if i < 0: result.append(i)
#     return result
# print(poss(list1))
    


# list1 = [-10,20,-78,60,185,-47,45,-80,45,88]
# def poss(x):
#     return x > 0
# print(list(filter(poss, list1)))



# list1 = [-10,60,185,-47,45,-80,45,88]
# print(list(filter(lambda x: x > 0, list1)))



# sorted 함수
# print(sorted([3, 1, 2]))
# print(sorted(['a', 'c', 'b']))
# print(sorted("zero"))
# print(sorted((3, 2, 1)))


# list1 = [15,789,7,2,4896,25,56]
# print('정렬 전', list1)
# print('정렬 후', sorted(list1))
