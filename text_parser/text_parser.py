import re
from pathlib import Path
from itertools import islice
from collections import Counter

def intro() -> str:
    return ("""Анализ текста
        1 — Ввести текст с клавиатуры
        2 — Прочитать текст из файла
        0 — Выход
Ваш выбор: """)

def input_validation(user_input: str, min_val = 0, max_val = 2) -> int:
    try:
        int(user_input)
    except ValueError:
        raise ValueError("Введённые данные не являются числом!")

    if int(user_input) < min_val or int(user_input) > max_val:
        raise ValueError("Выбрано неверное значение!")

    return int(user_input)

#Функции обработки текста
def normalize_text(text: str) -> list[str]:
    words_list = re.findall(r'[^\W_]+', text.lower())

    return words_list

def count_words(words: list[str]) -> dict[str, int]:
    d = dict(Counter(words))
    all_words = len(words)
    unique_words = len(d.keys())

    return all_words, unique_words, d

def get_top_words(frequencies: dict[str, int], n: int) -> list[tuple[str, int]]:

    return frequencies, sorted(frequencies.items(), key=lambda x:(-x[1], x[0]))[:n]

def text_validation(text: str) -> str:
    text = normalize_text(text)
    if not text:
        raise ValueError('Текст не содержит слов!')
    return ' '.join(text)


#Функции ввода текста
def manual_input() -> str:
    return text_validation(input("Текст: "))

def read_text_from_file(path: str) -> str:
    try:
        path = Path(path)
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
            return text

    except FileNotFoundError:
        raise FileNotFoundError("Проверьте наличие файла!")
    except PermissionError:
        raise PermissionError("Нет прав доступа работы с файлом!")
    except UnicodeDecodeError as e:
        raise ValueError("файл не в кодировке UTF-8") from None

#Общая последовательность обработки текста
def text_processing(text: str) -> str:
    # Нормализация текста
    normaized_text = normalize_text(text)
    print(f'Нормализованные слова: {normaized_text}')

    # Количество всех/уникальных слов
    all_words, unique_words, words_dict = count_words(normaized_text)
    print(f'Всего слов: {all_words}')
    print(f'Уникальных слов: {unique_words}')

    # Определение топ-N слов
    enter_tf = True
    while enter_tf:
        try:
            top_frequency_threahold = input_validation(input("Введите значение для фильтрации ТОП-слов: "), min_val=1, max_val=unique_words)
            if int(top_frequency_threahold):
                enter_tf = False
            full_frequencies, top_frequencies = get_top_words(words_dict, top_frequency_threahold)
            top_frequencies_str =''.join(f'\n{t}' for t in top_frequencies)
            print(f'Частоты: {full_frequencies}')
            print(f'Топ-3: {top_frequencies_str}')
            print()

        except ValueError as e:
            print(f"Ошибка: {e}")


def main() -> None:
    to_repeat = True
    while to_repeat:
        try:
            user_input = input_validation(input(intro(), ))
        except ValueError as e:
            print(f'Ошибка: {e}')
            continue

        if user_input == 0:
            to_repeat = False
            print("До свидания!")

        match user_input:
            case 1:
                try:
                    text = manual_input()
                    text_processing(text)
                except ValueError as e:
                    print(f'Ошибка: {e}')
                    continue

            case 2:
                try:
                    #Ввод текста
                    file_path = input("Введите путь к файлу: ", ).rstrip('"').strip('"')
                    text = read_text_from_file(file_path)

                    text_processing(text)

                except Exception as e:
                    print(f"Ошибка {e}")

if __name__ == "__main__":
    main()