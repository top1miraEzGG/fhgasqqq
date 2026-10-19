import tkinter as tk

# --- 6. Функция для ввода значений с номерных кнопок ---
def input_digit(digit):
    # Получаем текущий текст из поля ввода
    current_text = text_input.cget("text")
    # Если там стандартный '0', заменяем его, иначе добавляем цифру
    if current_text == "0":
        text_input.config(text=str(digit))
    else:
        text_input.config(text=current_text + str(digit))

# Переменные для хранения первого числа и операции
first_number = 0
operation = ""

# --- 7. Пять пустых функций (теперь с логикой) ---
def summ():
    global first_number, operation
    first_number = float(text_input.cget("text"))
    operation = "+"
    text_input.config(text="0")

def diff():
    global first_number, operation
    first_number = float(text_input.cget("text"))
    operation = "-"
    text_input.config(text="0")

def multiply():
    global first_number, operation
    first_number = float(text_input.cget("text"))
    operation = "*"
    text_input.config(text="0")

def divide():
    global first_number, operation
    first_number = float(text_input.cget("text"))
    operation = "/"
    text_input.config(text="0")

def result():
    global first_number, operation
    try:
        second_number = float(text_input.cget("text"))
        if operation == "+":
            res = first_number + second_number
        elif operation == "-":
            res = first_number - second_number
        elif operation == "*":
            res = first_number * second_number
        elif operation == "/":
            if second_number == 0:
                res = "Error"
            else:
                res = first_number / second_number
        else:
            res = second_number

        # Вывод результата (убираем .0 если число целое)
        if res == int(res):
            text_input.config(text=str(int(res)))
        else:
            text_input.config(text=str(res))
            
    except ValueError:
        text_input.config(text="Error")

# --- Создание главного окна ---
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

# --- 5. Создание поля для вывода ---
text_input = tk.Label(root, text="0", font=("Arial", 24), bg="white", anchor="e", padx=10)
text_input.pack(fill="x", pady=10, padx=10)

# Фрейм для размещения кнопок
buttons_frame = tk.Frame(root)
buttons_frame.pack()

# --- 2. Создание интерфейса из 10 кнопок с номерами от 0 до 9 ---
# Делаем сетку 3x3 для цифр 1-9 и отдельно 0
digit_buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '0'
]

row_val = 0
col_val = 0

for digit in digit_buttons:
    # Использование lambda с аргументом по умолчанию (d=digit), чтобы передать нужную цифру
    btn = tk.Button(buttons_frame, text=digit, font=("Arial", 18), width=4, height=2,
                    command=lambda d=digit: input_digit(d))
    
    # Для нуля сделаем отдельную позицию
    if digit == '0':
        btn.grid(row=3, column=1) # Ставим в центр нижнего ряда
    else:
        btn.grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 2:
            col_val = 0
            row_val += 1

# --- 3 и 4. Создание матрицы операций и кнопок через цикл ---
# Матрица (список кортежей): (Текст на кнопке, Функция)
operations = [
    ("+", summ),
    ("-", diff),
    ("*", multiply),
    (":", divide),
    ("=", result)
]

# Создаем фрейм для операций (справа от цифр)
ops_frame = tk.Frame(root)
ops_frame.pack(pady=10)

for op_text, op_func in operations:
    # Цикл for для задания text и command
    op_btn = tk.Button(ops_frame, text=op_text, font=("Arial", 18), width=4, height=2,
                       command=op_func)
    op_btn.pack(side="left", padx=2)

# Запуск приложения
root.mainloop()