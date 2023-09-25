# list1 = [0,2,4,6,8,10]

# list2 = []
# for i in range(11):
#     if i % 2 ==0:
#      list2.append(i)
    
    
# list3 = [i for i in range(11) if i % 2 ==0]

# print(f'list1 = ', list1)
# print(f'list2 = ', list2)
# print(f'list3 = ', list3)



# a = 10
# if a % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')


# print('짝수' if a % 2 == 0 else '홀수')


# a = ['a','b','c','d','e']
# b = ['1','2','3','4','5']
# c = []
# for i in a:
#     for j in b:
#         c.append( i + j )
# print(c)


# a = ['a','b','c','d','e']
# b = ['1','2','3','4','5']
# print( [  i+j  for  i  in  a       for  j  in  b  ] )





# fruit_list = ["apple", "banana", “peach”]
# color_list = [“red”, “yellow”, “pink”]

# fruit_color = dict(   zip(fruit_list, color_list)   )

# fruit_color = {"apple" : "red", "banana" : "yellow", "peach":"pink"}
# no_bana = {}

# for  key   in    fruit_color:
#     if key != "banana": 
#         no_bana[key] = fruit_color[key]

# print(no_bana)




# fruit_list = ["apple", "banana", "peach"]
# color_list = ["red", "yellow", "pink"]

# fruit_color = dict(zip(fruit_list, color_list))
# # fruit_color = {"apple" : "red", "banana" : "yellow", "peach":"pink"}
# no_bana = {}

# for key in fruit_color:
#     if key != "banana":
#         no_bana[key] = fruit_color[key]

# print(no_bana)






# fruit_color = {"apple" : "red", "banana" : "yellow", "peach":"pink"}
# no_bana = { key:val  for key, val in  fruit_color.items()  if  key != "banana" }
# print(no_bana)



