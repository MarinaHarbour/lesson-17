import random


def stone_1():
    return random.randint(3, 20)


def generate_password(n):
    result = []
    for x in range(1, 21):
        for y in range(x + 1, 21):
            if n % (x + y) == 0:
                result.append(str(x))
                result.append(str(y))
    return ''.join(result)


if __name__ == "__main__":

    n = stone_1()
    print(f"Число на первой вставке: {n}")

    password = generate_password(n)
    print(f"Пароль: {password}")

    print("\nПроверка для всех чисел от 3 до 20:")
    for i in range(3, 21):
        password = generate_password(i)
        print(f"{i} - {password}")
