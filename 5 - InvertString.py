def reverseText(text):
    reverse = ""
    for i in range(len(text)-1, -1, -1):
        reverse += text[i]
    return reverse

try:
    text = str(input("Insert text: "))
    reverse = reverseText(text)
    print(reverse)
except:
    print("Unable to identify text!")