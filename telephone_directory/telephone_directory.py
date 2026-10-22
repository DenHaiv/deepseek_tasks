def show_menu() -> str:
    return ("""Телефонный справочник
        1 — Добавить контакт
        2 — Найти контакт
        3 — Удалить контакт
        4 — Показать все контакты
        0 — Выход
        Ваш выбор: """)

def validate_spaces(string: str) -> str:
    if string.strip() == '':
        raise ValueError("Вы ничего не ввели!")
    else:
        return string.strip()

def validate_user_input() -> int:

    try:
        user_input = int(input(show_menu()))
    except ValueError:
        raise ValueError("Вы ввели не числовое значение!\n")

    if user_input < 0 or user_input > 4:
        raise ValueError("Выбранное значение должно быть в диапазоне между 1 и 4!\n")

    return user_input

def add_contact(phonebook: dict[str, str]) -> None:
    name = validate_spaces(input("Введите имя: ", ))
    phonenumber = validate_spaces(input("Введите номер телефона: ", ))

    if name in phonebook.keys():
        raise ValueError(f"Ошибка: контакт «{name}» уже существует.") from None

    phonebook[name] = phonenumber
    print(f"Контакт <{name} : {phonenumber}> был успешно добавлен!")

def find_contact(phonebook: dict[str, str]) -> None:
    name = validate_spaces(input("Введите имя: ", ))
    if name in phonebook.keys():
        print(f'<{name}> : <{phonebook[name]}>')
    else:
        print("Контакт не найден.")

def delete_contact(phonebook: dict[str, str]) -> None:
    name = validate_spaces(input("Введите имя: ", ))

    if name in phonebook.keys():
        phonebook.pop(name)
        print(f"Контакт <{name}> удалён.")
    else:
        print(f"Контакт <{name}> не найден.")

def show_all_contacts(phonebook: dict[str, str]) -> None:
    if phonebook.keys():
        print(*(f'{i} : {j}' for i, j in sorted(phonebook.items())), sep='\n')
    else:
        print("Справочник пуст")

def main() -> None:
    phonebook = {}
    is_finished = False
    while not is_finished:
        try:
            user_input = validate_user_input()
        except ValueError as e:
            print(f"Ошибка: {e}")
            show_menu()
            continue

        if user_input == 0:
            is_finished = True
            print("До свидания!")

        match user_input:
            case 1:
                try:
                    add_contact(phonebook)
                except ValueError as e:
                    print(e)

            case 2:
                find_contact(phonebook)

            case 3:
                delete_contact(phonebook)

            case 4:
                show_all_contacts(phonebook)

            case _:
                pass


if __name__ == "__main__":
    main()
