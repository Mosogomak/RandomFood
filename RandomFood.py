#파이썬 - 랜덤으로 점심 정해주기
lunch = ["짜장면","마라탕","치킨","떡볶이","김치찌개","보쌈"]

#점심 추가하기
while True:
    print(lunch)
    food = input("음식을 추가하세요 (멈추고 싶으면 q를 입력 하세요.) : ")
    if food == "q":
        break
    else:       
        lunch.append(food)
print(lunch)

#점심 삭제하기 
set_lunch = set(lunch)

while True:
    print(set_lunch)
    item = input("음식을 삭제하세요 (멈추고 싶으면 q를 입력 하세요.) : ")
    if item == "q":
        break
    else:
        set_lunch = set_lunch - set([item])

