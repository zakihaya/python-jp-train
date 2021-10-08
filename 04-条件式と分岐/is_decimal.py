string = input("文字列を入力してください:")

if string.isdecimal():
    print(string, "は数字です")
else:
    print(string, "は数字ではありません")
