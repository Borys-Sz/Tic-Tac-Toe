text = input()
words = text.split()
for word in words:
    if word.startswith("https://") or word.startswith("http://") or word.startswith("www.") or word.startswith("WWW."):
        print(word)