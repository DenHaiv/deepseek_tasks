def validate_number(n : str) -> int:
    try:
        value = int(n)
            
    except ValueError:
        raise ValueError("Введено нецелое число!") from None

    if int(value) < 2:
        raise ValueError("Число должно быть не меньше 2!") from None

    return value

def check_if_simple(n : int) -> bool:

    is_simple = True
    if n > 2 and n % 2 == 0:
        is_simple = False
    else:
        sqr_n = int((n ** 0.5) // 1)
        for i in range(3, sqr_n + 1, 2):
            if n % i == 0:
                is_simple = False
                break

    return is_simple

def main() -> None:
    try:
        n = validate_number(input("Введите число: "))
    except ValueError as e:
        print(f"Ошибка {e}")
        return

    print(f"{n} - простое число" if check_if_simple(n) else f"{n} - не простое число")

if __name__ == "__main__":
    main()