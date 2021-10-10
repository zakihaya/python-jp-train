counter = 1

while counter <= 5:
    text = input("値を入力してください:")

    if text == "999":
        print("中断します")
        break

    number = int(text)
    print(counter, "回目:", number * number)
    counter = counter + 1

print("終了しました")

