VALID_OPERATIONS = {'+', '-', '*', '/'}

def check_number(raw : str, name : str) -> float:
    try:
        return float(raw)
    except ValueError:
        raise ValueError(f"{name} <{raw}> не является числом!")

def check_operation(oper):
    oper = oper.strip()
    if oper in VALID_OPERATIONS:
        return oper
    else:
        raise ValueError(
            f"{oper} - неподдерживаемая операция)\n"
            f"Доступные операции: {', '.join(sorted(VALID_OPERATIONS))}")

def calculate(a : float, b : float, op : str) -> float:

    match op:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            if b == 0:
                raise ZeroDivisionError("Делить на ноль нельзя!")
            result = a / b
        case _:
            raise AssertionError("Неизвестная операция {oper}")

    return result
    
def main() -> None:

    try:
        a = check_number(input('Введите первое число: '), 'Первое число')
        b = check_number(input('Введите второе число: '), 'Второе число')
        op = check_operation(input('Введите знак операции (+ - * /): '))
        result = calculate(a, b, op)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Ошибка: {e}")
    else:
        print(f"Результат: {result}")

if __name__ == '__main__':
    main()