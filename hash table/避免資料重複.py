def voted(name):
    if vote_people[name]:
        print("你已經投過票了")
    else:
        print("歡迎投票")
        vote_people[name] = True
vote_people = {
    "Trump" : None,
    "Lisa" : None,
    "Mike" : None
}
while 1:
    name = input("請輸入姓名 : ")
    if name in vote_people:
        voted(name)
    else:
        print("你不是選民")