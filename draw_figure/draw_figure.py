def show_menu() -> None:
    print("""Выберите фигуру:
                1 — Квадрат
                2 — Прямоугольный треугольник
                3 — Равнобедренный треугольник
                0 — Выход
                Ваш выбор:""")

def validate_user_input(n : str, min_val = 0, max_val = 3) -> int:
    try:
        val = int(n)
    except ValueError:
        raise ValueError("Вы ввели не цифровое значение!") from None

    if int(n) < min_val or int(n) > max_val:
        raise ValueError("Вы ввели значине вне диапазона 1-3!")

    return val

def draw_square(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print('* ', end='')
        print()

def draw_right_triangle(n: int) -> None:
    for i in range(n):
        for j in range(i + 1):
            print('* ', end='')
        print()

def draw_isosceles_triangle(n: int) -> None:
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1), end='')
        print()

def draw_preconditions(figure_size=1) -> tuple[int, int]:
    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = validate_user_input(input("Сделайте ваш выбор: "))
            if user_input == 0:
                break

            while True:
                try:
                    figure_size = validate_user_input(input("Введите размер фигуры: "), min_val=1, max_val=100)
                    is_valid_input = True
                    break
                except ValueError as e:
                    print(f"Ошибка {e}")
                    show_menu()
                    break

        except ValueError as e:
            print(f"Ошибка {e}")
            show_menu()

    return (user_input, figure_size)

def main() -> None:
    user_input = True
    while user_input:
        show_menu()

        user_input, figure_size = draw_preconditions()

        match user_input:
            case 1:
                draw_square(figure_size)
            case 2:
                draw_right_triangle(figure_size)
            case 3:
                draw_isosceles_triangle(figure_size)
            case _:
                print("До свидания!")

if __name__ == "__main__":
    main()