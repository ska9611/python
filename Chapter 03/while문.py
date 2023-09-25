# 총합 = 0
# for i in range(1,100):
#     if i % 3 == 0:
#         총합 += i
# print(총합)

# treeHit = 0
# while treeHit <= 10 :
#      treeHit = treeHit +1   
#      print("나무를 %d번 찍었습니다." % treeHit)



# treeHit = 0
# while treeHit <= 10 :
#      treeHit = treeHit +1   # treeHit += 1
#      print(f"나무를 {treeHit}번 찍었습니다.")

     


# cnt = 10

# while  cnt != 0:
#     print(f'{11 - cnt}회 실행')
#     cnt = cnt - 1



set1 = set("ABCDE")
print(set1)
while True:
    if len(set1) == 0: 
        print("또 꺼낼 것이 없어요")
        break
    else:
        p1 = set1.pop()
        print(f'{p1}를 꺼냈습니다.')
        print(set1)
        