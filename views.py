
import presenter


while True:
    presenter.show_menu()
    choice = input("Выберите пункт меню (1-4): ")
    if choice == "1":
        presenter.register_user()
    elif choice == "2":
        presenter.login_user()
    elif choice == "3":
        print(presenter.users)
    elif choice == "4":
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
