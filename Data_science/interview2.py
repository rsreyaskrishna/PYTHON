lst = ['words', 'maths', 'ipl', 'world', 'isl', 'dfg', 'klm']
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
words_vowels = []
for word in lst:
    if any(char in vowels for char in word):
        words_vowels.append(word)
if words_vowels:
    print('Words with vowels:', words_vowels)
else:
    print('No words with vowels found.')
