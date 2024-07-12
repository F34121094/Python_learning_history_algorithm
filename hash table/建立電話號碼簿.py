phone_list = {}
phone_list["Lisa"] = "0912111111"
phone_list["Trump"] = "0912111111"
phone_list["Mike"] = "0912111111"
name = input("請輸入名字 : ")
if name in phone_list:
    print(f" {name} 的電話號碼是 {phone_list[name]}")
else:
    print(f"沒有查到 {name} 的電話號碼")
