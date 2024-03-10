def count_previous_occurrences(text):
    words = text.split()  # Розділяємо текст на слова
    word_count = {}  # Створюємо порожній словник для зберігання кількості зустрічей кожного слова
    previous_counts = []  # Створюємо порожній список для зберігання кількості зустрічей кожного слова в попередніх рядках

    for word in words:
        if word in word_count:  # Перевіряємо, чи вже було зустрінуте це слово раніше
            previous_counts.append(word_count[word])  # Якщо так, додаємо кількість зустрічей до списку previous_counts
            word_count[word] += 1  # Оновлюємо лічильник для поточного слова
        else:
            previous_counts.append(0)  # Якщо слово вперше зустрінуте, додаємо 0 до списку previous_counts
            word_count[word] = 1  # Додаємо слово до словника та встановлюємо лічильник на 1

    return previous_counts


# Приклади вхідних параметрів і вихідних результатів
texts = [
   "The quick brown fox jumps over the lazy dog.\nA quick brown dog jumps over a lazy cat.\nQuick foxes are fast, but lazy dogs sleep more.\nBrown bears are not as lazy as you might think.\nFoxes, dogs, and bears all live in the forest.\nThe fox is cunning, the dog is loyal, and the bear is strong."
]

for text in texts:
    result = count_previous_occurrences(text)
    print(result)
