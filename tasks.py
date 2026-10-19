import sys

# Список для задач
my_tasks = []

def menu():
    sys.stdout.write("\n--- МЕНЕДЖЕР ЗАДАЧ ---\n")
    sys.stdout.write("1. Показать задачи\n")
    sys.stdout.write("2. Добавить задачу\n")
    sys.stdout.write("3. Изменить задачу\n")
    sys.stdout.write("4. Удалить задачу\n")
    sys.stdout.write("0. Выход\n")
    sys.stdout.write("Выбор: ")

def pokaz():
    if len(my_tasks) == 0:
        sys.stdout.write("\nСписок пуст.\n")
    else:
        sys.stdout.write("\nЗадачи:\n")
        for i in range(len(my_tasks)):
            sys.stdout.write(str(i + 1) + ". " + my_tasks[i] + "\n")

def dobavit():
    sys.stdout.write("\nВведите задачу: ")
    text = sys.stdin.readline().strip()
    if text != "":
        my_tasks.append(text)
        sys.stdout.write("Добавлено.\n")
    else:
        sys.stdout.write("Пустая строка.\n")

def izmenit():
    pokaz()
    if len(my_tasks) == 0:
        return
    sys.stdout.write("Номер задачи для изменения: ")
    num = sys.stdin.readline().strip()
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(my_tasks):
            sys.stdout.write("Новое название: ")
            new_text = sys.stdin.readline().strip()
            if new_text != "":
                my_tasks[idx] = new_text
                sys.stdout.write("Изменено.\n")
            else:
                sys.stdout.write("Пустая строка.\n")
        else:
            sys.stdout.write("Нет такой задачи.\n")
    else:
        sys.stdout.write("Введите число.\n")

def udalit():
    pokaz()
    if len(my_tasks) == 0:
        return
    sys.stdout.write("Номер задачи для удаления: ")
    num = sys.stdin.readline().strip()
    if num.isdigit():
        idx = int(num) - 1
        if 0 <= idx < len(my_tasks):
            my_tasks.pop(idx)
            sys.stdout.write("Удалено.\n")
        else:
            sys.stdout.write("Нет такой задачи.\n")
    else:
        sys.stdout.write("Введите число.\n")

def main():
    while True:
        menu()
        choice = sys.stdin.readline().strip()
        if choice == '1':
            pokaz()
        elif choice == '2':
            dobavit()
        elif choice == '3':
            izmenit()
        elif choice == '4':
            udalit()
        elif choice == '0':
            sys.stdout.write("Выход.\n")
            break
        else:
            sys.stdout.write("Неверный пункт.\n")

if __name__ == "__main__":
    main()