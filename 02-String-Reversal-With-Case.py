sentence = "Python is Awesome"
words = sentence.split()  # Split into list of each word
res = ''
for word in words:
    word = word[::-1]  # Reverse the word
    word = word.capitalize() + ' '  # Capitalize and add empty space
    res += word  # Append the word to the output string
print(res)