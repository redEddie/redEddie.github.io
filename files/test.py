def add_text_to(text):
    textpost = text
    textpost += "testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest"

    return textpost


sample = "none"

print(sample)
sample += "+none"
print(sample)
sample = add_text_to(sample)
print(sample)
