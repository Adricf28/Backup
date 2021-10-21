word = ['Holá', 'Buenas']

for i in word:
    if 'á' in set(i):
        word.remove(i)

print(word)