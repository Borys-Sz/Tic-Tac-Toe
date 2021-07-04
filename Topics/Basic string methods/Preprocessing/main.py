text = input()

def badpunc(text):
    new_text = text.replace(',', '')
    new_text = new_text.replace('.', '')
    new_text = new_text.replace('!', '')
    new_text = new_text.replace('?', '')
    return new_text.lower()

print(badpunc(text))