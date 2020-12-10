text = input()
words = text.split()
for i, word in enumerate(words):
    print(i, word[:10])