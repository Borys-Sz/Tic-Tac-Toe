text = input()

def markdel(text):
    new_text = text.strip('*')
    new_text = new_text.strip("_")
    new_text = new_text.strip("~")
    new_text = new_text.strip("`")
    return new_text

print(markdel(text))