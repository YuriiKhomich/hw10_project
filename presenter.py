
from model import users, user_types


def show_menu():
    """Displays the program menu."""
    print("Меню:")
    print("1. Регистрация")
    print("2. Вход")
    print("3. Вывести всех зарегистрированных пользователей")  # временная опция, перейдет в админку
    print("4. Выход")
    print()


def register_user():
    """New user registration function."""
    print("Выберите тип пользователя:")
    print("1. Автор")
    print("2. Подписчик")
    print("3. Администратор")

    user_type_choice = input("Введите номер типа пользователя: ")
    if user_type_choice not in ["1", "2", "3"]:
        print("Некорректный выбор типа пользователя.")
        return

    user_type = list(user_types.keys())[int(user_type_choice) - 1]
    username = input("Введите имя пользователя: ")
    for user in users.data:
        if user.username == username:
            print("Пользователь с таким именем уже существует.")
            return
    password = input("Введите пароль: ")
    users.register(user_type, username, password)
    print("Пользователь успешно зарегистрирован.")


def login_user():
    """Function for user login."""
    if not users.data:
        print("База данных пользователей пуста. Пожалуйста, зарегистрируйтесь.")
        return
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    user = users.login(username, password)
    if user:
        print("Вход выполнен успешно:", user)
    else:
        print("Неверные учетные данные.")
