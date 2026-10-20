def input_validation(n : str) -> int:
    try:
        val = int(n)
    except ValueError:
        raise ValueError("Введённое значение не целое число!")

    if val < 1:
        raise ValueError("Введённое значение должно быть не меньше 1!")
    
    return val
            

def main() -> None:
    try:
        n = input_validation(input("Введите значение верхнего диапазона: "))     
    except ValueError as e:
        print(f'Ошибка {e}')
        return
    
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    main()