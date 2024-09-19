import random
import string
import re
import hashlib
import base64

# Функция для генерации случайного пароля
def generate_password(length=12, use_digits=True, use_upper=True, use_special=True):
    characters = string.ascii_lowercase  # Буквы нижнего регистра
    if use_upper:
        characters += string.ascii_uppercase  # Добавляем заглавные буквы
    if use_digits:
        characters += string.digits  # Добавляем цифры
    if use_special:
        characters += string.punctuation  # Добавляем специальные символы

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Функция для проверки надежности пароля с использованием регулярных выражений
def check_password_strength(password):
    length_check = len(password) >= 8
    digit_check = re.search(r"\d", password) is not None
    upper_check = re.search(r"[A-Z]", password) is not None
    special_check = re.search(r"[@$!%*?&#]", password) is not None
    return length_check and digit_check and upper_check and special_check

# Функция для шифрования пароля
def encrypt_password(password, method):
    if method == "SHA256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif method == "MD5":
        return hashlib.md5(password.encode()).hexdigest()
    elif method == "Base64":
        return base64.b64encode(password.encode()).decode()
    else:
        raise ValueError("Неизвестный метод шифрования!")

# Доступные методы шифрования
encryption_methods = {
    "1": "SHA256",
    "2": "MD5",
    "3": "Base64"
}

# Запрос на ввод пароля пользователем или его генерацию
def get_user_password():
    choice = input("Хотите сгенерировать пароль автоматически? (да/нет): ").lower()
    if choice == 'да':
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
        use_digits = input("Использовать цифры? (да/нет, по умолчанию да): ").lower() != 'нет'
        use_upper = input("Использовать заглавные буквы? (да/нет, по умолчанию да): ").lower() != 'нет'
        use_special = input("Использовать специальные символы? (да/нет, по умолчанию да): ").lower() != 'нет'
        return generate_password(length=length, use_digits=use_digits, use_upper=use_upper, use_special=use_special)
    else:
        return input("Введите свой пароль: ")

# Основная программа
password = get_user_password()
print(f"\nВаш пароль: {password}")

# Проверка надежности пароля
if check_password_strength(password):
    print("Пароль надежен.")
else:
    print("Пароль недостаточно надежен. Рекомендуется использовать более сложный пароль.")

# Выбор метода шифрования пользователем
print("\nВыберите метод шифрования:")
print("1: SHA256")
print("2: MD5")
print("3: Base64")

choice = input("Введите номер метода шифрования (1, 2 или 3): ")

if choice in encryption_methods:
    selected_method = encryption_methods[choice]
    encrypted_password = encrypt_password(password, method=selected_method)
    print(f"\nЗашифрованный пароль ({selected_method}): {encrypted_password}")
else:
    print("Ошибка: выбран неизвестный метод шифрования.")

'''
1. random и string используются для генерации случайных паролей.
2. re (регулярные выражения) используется для проверки пароля на соответствие критериям надежности.
3. hashlib предоставляет функции для хэширования с использованием алгоритмов, таких как SHA256 и MD5.
4. base64 позволяет кодировать данные в формат Base64.
'''

'''
[Функция генерации случайного пароля]
1. Генерирует случайный пароль длиной по умолчанию 12 символов.
2. Пользователь может настроить длину пароля и выбрать, использовать ли цифры, заглавные буквы и специальные символы.
3. Генерация выполняется с использованием библиотеки random, которая случайным образом выбирает символы из строки допустимых символов.
'''

'''
[Функция проверки надежности пароля]
Длина: минимум 8 символов.
Наличие хотя бы одной цифры.
Наличие хотя бы одной заглавной буквы.
Наличие хотя бы одного специального символа (из набора @$!%*?&#).

Если все критерии выполнены, возвращается True, иначе False.
'''

'''
Эта функция шифрует пароль с использованием выбранного метода:
1. SHA256 — создает криптографический хэш с помощью алгоритма SHA256.
2. MD5 — создает хэш с помощью алгоритма MD5.
3. Base64 — кодирует пароль в формат Base64.

Если выбран неизвестный метод, выбрасывается ошибка.
'''

'''
[Методы шифрования]
Здесь задаются методы шифрования, которые пользователь может выбрать, используя соответствующие номера (1, 2 или 3).
'''

'''
[Запрос пароля от пользователя]
Эта функция предлагает пользователю выбрать:
    Генерировать пароль или ввести свой вручную:
        Если пользователь выбрал автоматическую генерацию, ему предлагается задать параметры (длину, использование цифр, заглавных букв и специальных символов).
        Если выбран ввод вручную, программа запрашивает пароль от пользователя.
'''

# TODO: Заметки
## Автор: Дуплей Максим Игоревич
## Дата: 19.09.2024