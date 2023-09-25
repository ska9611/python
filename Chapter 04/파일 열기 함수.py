# import os
# pwd = os.getcwd()
# print('현재 작업 디렉토리 전체 경로 =',pwd)

# list1 = ['aaa', 'bbb', 'ccc']
# fp = open('output1.txt', 'w')
# fp.writelines(list1)
# fp.close()


# import os
# pwd = os.getcwd()
# print('현재 작업 디렉토리 전체 경로 =',pwd)

# list1 = ['aaa', 'bbb', 'ccc']
# fp = open('output1.txt', 'w')
# fp.writelines(list1)
# fp.writelines(' '.join(list1))
# fp.writelines(','.join(list1))
# fp.close()



# fp = open(r'./Chapter 04/output2.txt', 'a')

# for data in range(6,11):
#     fp.write(f'{data} 번째 자료 입니다\n')

# fp.close()



# list1 = ['aaa', 'bbb', 'ccc']

# fp = open('write-1.txt', 'w')
# for data in list1:
#     fp.write(data)
#     fp.write('\n')

# fp.close()






# list1 = ['aaa', 'bbb', 'ccc']

# fp = open('write-1.txt', 'w')
# fp.writelines(list1)
# fp.write('\n')
# fp.writelines(' '.join(list1))
# fp.write('\n')
# fp.writelines(','.join(list1))
# fp.write('\n')
# fp.writelines('\n'.join(list1))

# fp.close()




#read 함수
# fp = open(r'data.txt', 'r')

# while True:
#     data = fp.readline()
#     if not data:break 
#     print(data, end='')
# fp.close()


# fp = open(r'data.txt', 'r')

# list1 = fp.readlines()
# print(list1)

# fp.close()



# fp = open(r'data.txt', 'r')
# list1= fp.readlines()

# for data in list1:
#     list1(data.strip('\n'))
#     print(data)
# print(list1)

# fp.close()

fp = open(r'data.txt', 'r')
list1 = fp.readlines()

len1 = len(list1)

for i in range(len1):
    list[i] = list1[i].rstrip('\n')
    print(list1[i])

print(list1)
fp.close()


    