# user_input = input("이름을 입력하세요!:")
# print("안녕하세요," + user_input + "님!")

# num1 = input("숫자? ").split()
# print(num1)

# numbers = input("숫자를 입력하세요").split()
# print(numbers)

# numbers = input("숫자를 입력하세요").split(',')
# print(numbers)


# num = input("숫자들 ?").split()
# total = 0
# for data in num:
#     total = total + float(data)

# print(f'합계는 {total} 입니다')

list1 = input("이름 국어 영어 수학 점수를 차례로 입력하세요 \n").split()

hap = 0
for  i in list1[1:4]:
    hap = hap + int(i)

list1.append(hap)
ave = hap /3
list1.append(ave)

print('Name  KOR  ENG  MAT  TOTAL  AVE')
for data in list1:
    print(f'{data}   ', end='')
    
