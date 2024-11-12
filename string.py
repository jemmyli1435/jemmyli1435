# 如何使用字串
print("Hello\" YAYAYA") #ans: Hello" YAYAYA

# 函式
phrase = "Hello Mr. White"
print(phrase.upper()) #字母全部大寫
print(phrase.lower()) #字母全部小寫
print(phrase.isupper()) #字母全部大寫的話 回傳true
print(phrase.islower()) #字母全部小寫的話 回傳true
print(phrase.upper().isupper()) #字母全部大寫，回傳true
print(phrase.lower().islower()) #字母全部小寫，回傳true

print(phrase[0]) #數字從0開始計算