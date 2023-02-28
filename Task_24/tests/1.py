codecs = ["utf-16"]
for codec in codecs:
    with open("my_cookies.txt", "r", encoding=codec) as file:
        text = file.read()
    print(codec.rjust(12), "|", text)
