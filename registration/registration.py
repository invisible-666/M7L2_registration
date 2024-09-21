def initialize_users():
    """Возвращает заранее определенный словарь пользователей."""
    return {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3",
        "user4": "password4",
        "user5": "password5",
    }

def add_user(users, username, password):
    """Добавляет нового пользователя, если его еще нет в словаре.
    Возвращает обновленный словарь пользователей."""
    if username in users:
        return "Пользователь с таким логином уже существует."
    else:
        users[username] = password
        return f"Новый пользователь {username} успешно добавлен."

def display_users(users):
    """Выводит список всех пользователей и их пароли."""
    print("В системе уже зарегистрированы следующие пользователи с их паролями:")
    for username, password in users.items():
        print(f"Логин: {username}, Пароль: {password}")

def main():
    users = initialize_users()
    display_users(users)

    print("\nВы можете добавить нового пользователя.")
    username = input("Введите логин нового пользователя: ")
    password = input("Введите пароль нового пользователя: ")
    result = add_user(users, username, password)
    print(result)

    print("\nСписок всех пользователей после добавления нового:")
    display_users(users)

if __name__ == "__main__":
    main()
