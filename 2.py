#Вариант 14 Дан файл, содержащий текст на русском языке. Подсчитать количество слов, начинающихся и заканчивающихся на одну и ту же букву.
def count_words(text):
    words = text.split()
    count = 0
    for word in words:
        if len(word) > 1 and word[0].lower() == word[-1].lower():
            count += 1
    return count

def main():
    filename = "text.txt" 
 
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        words_count = count_words(text)
        print(f"Количество слов, начинающихся и заканчивающихся на одну и ту же букву: {words_count}")

if __name__ == "__main__":
    main()
