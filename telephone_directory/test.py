# def benchmark(func):
#     def wrapper(n):
#         return func(n)
#     return wrapper
#
# @benchmark
# def my_func(n):
#     pass
#
# # Проверяем, как Python видит нашу функцию теперь:
# print(my_func.__name__)
# # Выведет: wrapper!
#
# hidden_contents = my_func.__closure__
# print(hidden_contents)
#
# original_func = hidden_contents[0].cell_contents
# print(original_func.__name__)

from itertools import islice

# d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}
#
# print(*sorted(d.items(), key=lambda x:(x[1], -x[0]))[:3])

def test():
    try:
        i = int(input("ENter text: "))
        if i:
            print(i)
    except ValueError:
        raise ValueError('Error!') from None

    return i

if test():
    print('Ok')