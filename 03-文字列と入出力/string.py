# -*- coding: utf-8 -*-

print 123

# どちらでもよいが、チュートリアルではダブルクオートを使っているので、ダブルのほうがいいっぽい
print 'Python Programming!'
print "Python Programming!"

print(10, 2 * 10, 30)

# マルチバイト文字をprintする場合はuをつける
# https://gist.github.com/devlights/4561968
print(u"もも5つと、みかん8つで")

# これはエラー
# pring "a" * "b"

string = input()
print("文字列", string, "が入力されました。")
