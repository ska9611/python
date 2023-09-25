# a = 10
# b = 0
# print(a+b)
# try:    
#     print(a/b)
# except ZeroDivisionError as e:
#     print(f"0으로는 나누지 못해요") 
# print(a*b)
# print(a-b)


# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print(f"에러 발생: {e}")
# else:
#     print("정상적으로 계산 결과 얻음.")
# finally:
#     print("항상 실행됨.")



list1 = [10,20,30,40,50]
# length = len(list1)

try:
    
    for i in range(6):
        print(list1[i])
except IndexError as e:
    print('인덱스 범위를 벗어났습니다')

