
text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for char in punctuation:
    text = text.replace(char, "")

words = text.split()


num_of_words = set(words)


longest_word = words[0]

for word in words:
  if len(word) > len(longest_word):
    longest_word = word

shortest_word = words[0]

for word in words:
  if len(shortest_word) > len(word):
    shortest_word = word


word_frequency = dict()

for word in words:
    if word not in word_frequency.keys():
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

char_frequency = dict()

for char in text:

      if char not in char_frequency.keys():
          char_frequency[char] = 1
      else:
          char_frequency[char] += 1

print(f"Количество разных слов: {len(num_of_words)}")
print(f"Самое длинное слово: {longest_word}")
print(f"Самое короткое слово: {shortest_word}")

print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")

print("Частота символов:")
for char, frequency in char_frequency.items():
    print(f"{char}: {frequency}")