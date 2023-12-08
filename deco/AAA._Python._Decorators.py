# %% [markdown]
# # Дектораторы
#
# В этом домашнем задании мы напишем собственные дектораторы, которые будут менять системные объекты. Но для начала мы с вами познакомимся с функцией `write`.

# %%
import sys

sys.stdout.write("Hello, my friend!")

# %% [markdown]
# Это метод объектов file-like классов, то есть классов, которые реализуют семантику "Меня можно создать, из меня можно прочитать и в меня можно записать".
#
# Самый главный пример такого объекта -- объект `file`, являющийся результатом вызова фукнции `open()`. Для простоты и универсальности взаимодействия, стандартный ввод и стандартный вывод тоже являются файлами, из которых можно читать и в которые можно писать.

# %%
output = open("./some_test_data.txt", "w")

# %%
output.write("123")

# %%
output.close()

# %% [markdown]
# Как вы могли заметить, функция возвращает число записанных байт. Это важная часть контракта, которую нужно поддержать, если вы хотите как-то подменять эту функцию.

# %% [markdown]
# ## Задача 1

# %% [markdown]
# Для начала, давайте подменим метод `write` у объекта `sys.stdin` на такую функцию, которая перед каждым вызовом оригинальной функции записи данных в `stdout` допечатывает к тексту текущую метку времени.

# %%
from datetime import datetime

original_write = sys.stdout.write


def my_write(string_text: str) -> int:
    if string_text == "\n":  # bypass newline
        return original_write("\n")

    date_now = datetime.now().strftime("[%Y-%m-%d %H:%M%:%S]: ")
    return original_write(date_now + string_text)


sys.stdout.write = my_write

# %%
print("1, 2, 3")

# %%
sys.stdout.write = original_write

# %% [markdown]
# Вывод должен был бы быть примерно таким:

# %% [markdown]
# ```
# [2021-12-05 12:00:00]: 1, 2, 3
# ```

# %% [markdown]
# ## Задача 2
#
# Упакуйте только что написанный код в декторатор. Весь вывод фукнции должен быть помечен временными метками так, как видно выше.


# %%
def timed_output(function):
    original_write = sys.stdout.write

    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write  # очень похоже на патчинг
        result = function(*args, **kwargs)
        sys.stdout.write = original_write
        return result

    return wrapper


# %%
@timed_output
def print_greeting(name):
    print(f"Hello, {name}!")


# %%
print_greeting("Саша")  # Согласно гугл доку

# %% [markdown]
# Вывод должен быть похож на следующий:
#
# ```
# [2021-12-05 12:00:00]: Hello, Nikita!
# ```

# %% [markdown]
# ## Задача 3
#
# Напишите декторатор, который будет перенаправлять вывод фукнции в файл.
#
# Подсказка: вы можете заменить объект sys.stdout каким-нибудь другим объектом.


# %%
def redirect_output(filepath):
    def decorator(function):
        original_stdout = sys.stdout

        def wrapper(*args, **kwargs):
            sys.stdout = open(filepath, "w", encoding="utf-8")
            result = function(*args, **kwargs)
            sys.stdout = original_stdout
            return result

        return wrapper

    return decorator


# %%
@redirect_output("./function_output.txt")
def calculate():
    for power in range(1, 5):
        print("|", end="")
        for num in range(1, 20):
            print(f"{num**power:>7,}", end="|")
        print()


# %%
calculate()

# %% [markdown]
# Я немного разукрасил (может выглядеть упорото на нешироких мониторах)

# %%
# %cat function_output.txt

# %%
print("I am still working")

# %% [markdown]
# И ни в коем случае не вспоминаем, что в `print` есть параметр, отвечающий за перенаправление выхода в file-like object.

# %%
help(print)
