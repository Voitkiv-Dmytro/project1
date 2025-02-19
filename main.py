"""from calculations import add,minus,multiply,div,power
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = None
while choice != 0:
    choice = int(input("Enter your choice(0-stop program, 1-add numbers,2-minus, 3-div numbers, 4-multiply,5-power): "))
    if choice == 1:
        c = add(a,b)
        print(c)
        continue
    if choice == 2:
        c = minus(a,b)
        print(c)
        continue
    if choice == 3:
        c = div(a,b)
        print(c)
        continue
    if choice == 4:
        c = multiply(a,b)
        print(c)
        continue
    if choice ==5:
        c = power(a)
        print(c)
        continue"""

"""import os
#os.mkdir("Створена папка")
#os.rename("Створена папка", "Folder")
#os.mkdir("file.txt")    
with open("file.txt", "r") as file:
    text = file.read()
    print(text)

with open("file.txt", "a+") as my_file:
    my_file.write("This is our first text")

name = input("Введіть своє ім'я: ")
hobby = input("Введіть своє хобі: ")
dish = input("Введіть свою улюблену їжу: ")
with open("file.txt", "w") as file:
    file.write(name)
    file.write(hobby)
    file.write(dish)

with open("file.txt", "r") as file:
    text = file.read()
    print(text)
with open("file.txt", "r") as file:
    text = file.readline()
    print(text)
with open("file.txt", "r") as file:
    text = file.readlines()
    print(text)"""

"""a = int(input("Enter your choice(1-показати всі справи, 2- додати нову справу, 3-очистити справи, 4 - вийти): "))
if a == 1:
    with open("file.txt", "r") as file:
        text = file.read()
        print(text)
elif a == 2:
    b = input("Напиши справу: ")
    with open("file.txt", "a+") as file:
        file.write(b)
elif a == 3:
    with open("file.txt", "w") as file:
        file.close()
        os.remove("file.txt")
elif a == 4:
    print("Ви вийшли з програми.")


print("Вас вітає телефонна книга")
phone_book = {}
while True:
    print("1-додати новий контакт,\n2- пошук контакту,\n3-видалення контакту,\n4-вивести всі контакти")
    choice = int(input("Зробіть свій вибір: "))
    if choice == 1:
        a = input("Введіть ім'я контакту, який хочете створити: ")
        b = input("Введіть номер його телефону: ")
        phone_book[a]=b
        print("Контакт успішно створено")
        
    elif choice == 2:
        a = input("Введіть контакт який хочете знайти: ")
        if a in phone_book.keys():
            print("Контакт успішно знайдено: ")
            print(phone_book[a])
        else:
            print("На жаль, такого контакту не існує")
        
    elif choice == 3:
        a = input("Введіть контакт який хочете видалити: ")
        if a in phone_book.keys():
            del phone_book[a]
            print("Контакт успішно видалено")
        else:
            print("Невірно вказаний контакт")
        
    elif choice == 4:
        print("Список усіх контактів\n", phone_book)
        
    else:
        print("Неправильно зроблений вибір")"""


"""print("Hello world")
print(10/1)
print(5+5*2)

try:
    num = int(input("Enter number: "))
    print(f"Ти ввів {num}")
except ValueError:
    print("Ви ввели не число, а щось інше.")"""

"""try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
except ValueError:
    print("Ви ввели не число, а щось інше.")
else:
    print(a+b)
finally:
    print("Цей код виконався незалежно від помилки.")"""

"""import tkinter as tk

def my_func():
    button.config(text="Ви натиснули на мене")

def func2():
    label.config(font=("Calibri",25), fg="red")

def func3():
    text = entry.get()
    label3 = tk.Label(root,text=text,font=("Arial",18), fg="red")
    label3.pack()


root = tk.Tk()
root.title("Наша перша програма")
root.geometry("600x600")
frame1 = tk.Frame(root, bg="green")
frame1.pack(padx=10, pady=10)
label = tk.Label(frame1, text="ТУТ МІЙ ТЕКСТ", font=("Arial", 20), fg="blue")
label.pack()
button = tk.Button(root, text="Click me!", command=my_func)
button.pack()
button2 = tk.Button(root,text="Змінити колір напису", command=func2)
button2.pack()
entry = tk.Entry(root)
entry.pack()
button3 = tk.Button(root, text="Натисніть, щоб побачити введений текст", command=func3)
button3.pack()


root.mainloop()"""

"""import tkinter as tk
import random

def on_click(event):
    label.config(text= "Мене натиснуто!")

def change_backgroung_color(event):
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F0E68C", "#FF33A1"]
    root.config(bg=random.choice(colors))

root = tk.Tk()
label = tk.Label(root, text="Натисни на мене", bg="lightblue")
label.pack(padx=20, pady=20)
label1 = tk.Label(root, text="Натисни на Enter, щоб знімити колір фону", bg="lightblue")
label1.pack(padx=20, pady=40)
root.bind("<Return>", change_backgroung_color)

label.bind("<Button-3>", on_click)
root.mainloop()"""


#Autoclicker
"""import tkinter as tk
from tkinter import messagebox
import time
import keyboard
import mouse


def start_clicker():
# тут буде запуск клікера
    global running, delay
    clicks_per_second = int(entry.get())
    delay = 1/clicks_per_second
    messagebox.showinfo("Auto Clicker", "Auto Clicker started. Click 'ESC' to stop.")
    running = True
    schedule_click()

def schedule_click():
    if running:
        mouse.click()
        time.sleep(delay)
        schedule_click()

def show_info(event):
    messagebox.showinfo("Інформація", "Це автоклікер, він буде клікати мишкою зі швидкістю, яку ти вкажеш!")

def exit_app():
    global running
    running = False
    messagebox.showinfo("Auto Clicker","Auto Cliker stopped.")
    root.destroy()

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x220")
root.configure(bg="#e0f7fa")
root.bind('i', show_info)
running = False
delay = 0
# Label: назва
title_label = tk.Label(root, text="Auto Clicker", font=("Trebuchet MS", 16, "bold"), bg="#e0f7fa", fg="#00796b")
title_label.pack(pady=10) # Add some padding

# Label: кліки на секунду
label = tk.Label(root, text="Кліків на секунду:", font=("Trebuchet MS", 12), bg="#e0f7fa", fg="#00796b")
label.pack(pady=5)

# Entry для кількості кліків
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Frame, в якому будуть кнопки "почати" і "вийти"
button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20, 30))

# Кнопка "Почати"
start_button = tk.Button(button_frame, text="Почати", command=start_clicker, bg="#4caf50", fg="white", font=("Trebuchet MS", 12))
start_button.grid(row=0, column=0, padx=10)

# Кнопка "Вийти"
exit_button = tk.Button(button_frame, text="Вийти", command=exit_app, bg="#f44336", fg="white", font=("Trebuchet MS", 12))
exit_button.grid(row=0, column=1, padx=10)

keyboard.add_hotkey("esc", exit_app)

root.mainloop()"""

"""import customtkinter as ctk

def button_pressed():
    print("Кнопка натиснута")

app = ctk.CTk()
app.title("First custom app")
button = ctk.CTkButton(app, text="Click me", command=button_pressed)
button.pack(pady=20)

app.mainloop()"""

#Converter

"""import customtkinter as ctk

BTC_TO_UAH = 4119907.27
ETH_TO_UAH = 151023.61
USDT_TO_UAH = 42.12

def convert():
    amount = float(entry_amount.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()

# Якщо конвертуємо з криптовалюти в UAH
    if from_currency == "BTC":

        amount_in_uah = amount * BTC_TO_UAH

    elif from_currency == "ETH":

        amount_in_uah = amount * ETH_TO_UAH

    elif from_currency == "USDT":

        amount_in_uah = amount * USDT_TO_UAH

    elif from_currency == "UAH": # Якщо конвертуємо з гривні

        amount_in_uah = amount

# Якщо конвертуємо з UAH у криптовалюту
    if to_currency == "BTC":

        converted_amount = amount_in_uah / BTC_TO_UAH

    elif to_currency == "ETH":

        converted_amount = amount_in_uah / ETH_TO_UAH

    elif to_currency == "USDT":

        converted_amount = amount_in_uah / USDT_TO_UAH

    elif to_currency == "UAH": # Якщо конвертуємо в гривні

        converted_amount = amount_in_uah

# Оновлюємо результат
    result_label.configure(text=f"{amount} {from_currency} = {converted_amount:.4f} {to_currency}")

app = ctk.CTk()
app.title("Конвертер криптовалют")
app.geometry("400x300")
# Заголовок
title_label = ctk.CTkLabel(app, text="Конвертер криптовалют", font=("Roboto", 18))
title_label.pack(pady=10)

# Поле для вводу суми
entry_amount = ctk.CTkEntry(app, placeholder_text="Введи суму")
entry_amount.pack(pady=10)

# Вибір валюти для конвертації з
from_currency_var = ctk.StringVar(value="BTC")
from_currency_menu = ctk.CTkOptionMenu(app, variable=from_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
from_currency_menu.pack(pady=5)

# Вибір валюти для конвертації в
to_currency_var = ctk.StringVar(value="UAH")
to_currency_menu = ctk.CTkOptionMenu(app, variable=to_currency_var, values=["BTC", "ETH", "USDT", "UAH"])
to_currency_menu.pack(pady=5)

convert_button = ctk.CTkButton(app, text="Конвертувати", command=convert)
convert_button.pack(pady=10)

# Результат конвертації
result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)

# Запуск програми
app.mainloop()"""

"""try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
except ValueError:
    print("На жаль ти ввів не число!")
else:
    print("Ти молодець, ввів все без помилок ось результат")
    print(f"Сума чисел які ти ввів: {num1+num2}")
finally:
    print("Я виконуюсь завжди!")

#2
import math
try:
    number = int(input("Введіть додатнє число: "))
    if number < 0:
        raise ValueError("Неможливо обчислити квадратний корінь від'ємного числа")
except ValueError as e:
    print(f"Помилка: {e}")
else:
    print(f"Квадратний корінь з {number} = {math.sqrt(number)}")
finally:
    print("Дякуємо за звернення!")"""


#menu
"""import tkinter as tk
# Створюємо головне вікно
root = tk.Tk()
root.title("Miй додаток")
# Створюємо меню
menubar= tk.Menu(root)
# Додаємо перший пункт меню
file_menu1 = tk.Menu(menubar, tearoff=0)
file_menu1.add_command(label="Вiдкрити")
file_menu1.add_command(label="36еpeгти")
file_menu1.add_command(label="Вийти", command=root.quit)
# Додаємо другий пункт меню
file_menu2=tk.Menu (menubar, tearoff=0) 
file_menu2.add_command(label="Koпiвaти")
file_menu2.add_command(label="Вирiзати") 
file_menu2.add_command(label="Вставити")
# Додаємо два підменю в головне меню
menubar.add_cascade(label="Фaйл", menu=file_menu1)
menubar.add_cascade(label="Pедагувати", menu=file_menu2)
# Додаємо головне меню у вікно
root.config(menu=menubar)
root.mainloop()
"""
#color menu

"""import tkinter as tk

# Функції для зміни кольору фону

def change_to_red():
    root.config(bg="red")
def change_to_blue():
    root.config(bg="blue")
def change_to_green():
    root.config(bg="green")
def change_to_yellow():
    root.config(bg="yellow")
def change_to_purple():
    root.config(bg="purple")
def change_to_orange():
    root.config(bg="orange")

# Головне вікно
root = tk.Tk()
root.title("Додаток художника")
root.geometry("400x400")

# Створюємо меню
menubar = tk.Menu(root)

# Створюємо підменю
color_menu = tk.Menu(menubar, tearoff=0)
color_menu.add_command(label="Червоний", command=change_to_red)
color_menu.add_command(label="Синій", command=change_to_blue)
color_menu.add_command(label="Зелений", command=change_to_green)
color_menu.add_command(label="Жовтий", command=change_to_yellow)
color_menu.add_command(label="Фіолетовий", command=change_to_purple)
color_menu.add_command(label="Помаранчевий", command=change_to_orange)

# Додаємо підменю в головне меню
menubar.add_cascade(label="Вибір кольору", menu=color_menu)

# Додаємо головне меню до вікна
root.config(menu=menubar)

root.mainloop()"""

""""
import tkinter as tk
# Головне вікно
root = tk.Tk()
root.title("Простий редактор з панеллю інструментів") 
root.geometry("400x400")
# Функції для кнопок 
def new_file():
    print("Створено новий файл!")
def save_file():
    print("36epeжено!")
def open_file():
    print("Відкрито!")
def cut_text():
    print("Вирізано текст!")
def copy_text():
    print("Скопійовано текст!")
def paste_text():
    print("Вставлено текст!")
# Створюємо фрейм для панелі інструментів 
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
# Кнопка "Нове"
new_button = tk.Button(toolbar, text="Hoвe", command=new_file) 
new_button.pack(side=tk.LEFT, padx=2, pady=2)
# Кнопка "Зберегти"
save_button = tk.Button(toolbar, text="36еpeгти", command=save_file) 
save_button.pack (side=tk.LEFT, padx=2, pady=2)
# Кнопка "Відкрити"
open_button = tk.Button(toolbar, text="Вiдкрити", command=open_file) 
open_button.pack(side=tk. LEFT, padx=2, pady=2)
# Кнопка "Вирізати"
cut_button= tk. Button (toolbar, text="Bиpiзати", command=cut_text) 
cut_button.pack (side=tk. LEFT, padx=2, pady=2)

# Кнопка "Копіювати"
copy_button= tk.Button(toolbar, text="Koniвати", command=copy_text) 
copy_button.pack (side=tk. LEFT, padx=2, pady=2)
# Кнопка "Вставити"
paste_button = tk.Button(toolbar, text="Вставити", command=paste_text) 
paste_button.pack (side=tk. LEFT, padx=2, pady=2)
#Відображаємо панель інструментів 
toolbar.pack(side=tk.TOP, fill=tk.X)
# Основний контент
content = tk.Text(root)
content.pack (expand=1, fill=tk.BOTH)
root.mainloop()
"""

#calculator 3.6


import tkinter as tk

current_expression = ""
def on_button_click(button):
    global current_expression

    if button == "C":
        current_expression = ""
        display.delete(0, tk.END)

    elif button == "=":
        try:
            result = eval(current_expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_expression = str(result)

        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Помилка")
            current_expression = ""
    else:
            current_expression += str(button)
            display.delete(0, tk.END)
            display.insert(0, current_expression)

def set_theme(theme):
    if theme == "light":
        root.config(bg="white")
        display.config(bg = "lightgray", fg = "black")
    elif theme =="dark":
        root.config(bg="black")
        display.config(bg = "gray", fg = "white")
    for button in buttons:
        button.config(bg='lightgray' if theme == "light" else 'darkgray' if theme == "dark" else 'lightblue', 
                        fg='black' if theme != "dark" else 'white')

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x600")

display = tk.Entry(root, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Кнопки калькулятора
buttons = []
button_texts = [
'7', '8', '9', '/',
'4', '5', '6', '*',
'1', '2', '3', '-',
'C', '0', '=', '+'
]

row_val = 1
col_val = 0
# Створюємо кнопки:
for text in button_texts:

    button = tk.Button(root, text=text, font=('Arial', 18), width=5, height=2, command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# МЕНЮ
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Світла тема", command=lambda: set_theme("light"))
theme_menu.add_command(label="Темна тема", command=lambda: set_theme("dark"))
menubar.add_cascade(label="Налаштування", menu=theme_menu)
root.config(menu=menubar)
root.mainloop()


"""
import tkinter as tk

def my_func():
    button.config(text="Ви натиснули на мене")

def func2():
    label.config(font=("Calibri",25), fg="red")

def func3():
    text = entry.get()
    label3 = tk.Label(root,text=text,font=("Arial",18), fg="red")
    label3.pack()


root = tk.Tk()
root.title("Наша перша програма")
root.geometry("600x600")
frame1 = tk.Frame(root, bg="green")
frame1.pack(padx=10, pady=10)
label = tk.Label(frame1, text="ТУТ МІЙ ТЕКСТ", font=("Arial", 20), fg="blue")
label.pack()
button = tk.Button(root, text="Click me!", command=my_func)
button.pack()
button2 = tk.Button(root,text="Змінити колір напису", command=func2)
button2.pack()
entry = tk.Entry(root)
entry.pack()
button3 = tk.Button(root, text="Натисніть, щоб побачити введений текст", command=func3)
button3.pack()


root.mainloop()
"""

#3.1

"""import tkinter as tk

def my_func():
    label.config(fg="red")
    button.config(text="Ви натиснули на мене", fg="red")

def func2():
    text = entry.get()
    label3 = tk.Label(root,text=text,font=("Arial",18), fg="red")
    label3.pack()

root = tk.Tk()

root.geometry("600x600")
root.title("Наша перша програма")
label = tk.Label(root, text="ТУТ МІЙ ТЕКСТ", font=("Arial", 20), fg="blue")
label.pack()
frame1 = tk.Frame(root, bg="green")
frame1.pack(padx=10, pady=10)
button = tk.Button(frame1, text="Click me!", command=my_func)
button.pack()
entry = tk.Entry(root)
entry.pack()
button3 = tk.Button(root, text="Натисніть, щоб побачити введений текст", command=func2)
button3.pack()

root.mainloop()"""

#3.2
#pack
"""from tkinter import Tk, Label, Button

root = Tk()
root.title("GUI з Pack")

header = Label(root, text="Вітаємо у веселому GUI!", bg="lightblue", fg="white", font=("Arial", 20), padx=10, pady=10)
header.pack(side="top", fill="x")

instruction = Label(root, text="Я Верхній рядочок", bg="lime", fg="black", font=("Arial", 14), padx=20, pady=10)
instruction.pack(side="top", fill="x", padx=10, pady=10)

left_button = Button(root, text="Я Ліва кнопка", bg="orange", fg="white", font=("Arial", 12), padx=20, pady=10)
left_button.pack(side="left", fill="y", expand=True, padx=10, pady=10)

right_button = Button(root, text="Я Права кнопка", bg="purple", fg="white", font=("Arial", 12), padx=20, pady=10)
right_button.pack(side="right", fill="y", expand=True, padx=10, pady=10)

status = Label(root, text="А я Нижній рядок", bg="yellow", fg="black", font=("Arial", 12), padx=20, pady=10)
status.pack(side="bottom", fill="x")

root.mainloop()"""


#telegram
"""import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# Встав токен, який надіслав BotFather
bot = telebot.TeleBot('8179890010:AAFwchBdpwhE3kSVADDJqsxFneuIOL3NGpo')
# Команда /start: відправляє привітання, коли користувач пише /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я твій новий бот 😃")
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("Привіт")
    button2 = KeyboardButton("Почати")
    keyboard.add(button1, button2)

    # Надсилання повідомлення з кнопками
    bot.send_message(message.chat.id, "Привіт! Обери опцію:", reply_markup=keyboard)

# Обробка текстових повідомлень (реакція на кнопки)
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "Привіт":
        bot.send_message(message.chat.id, "Привіт! Як у тебе справи?")
    elif message.text == "Почати":
        keyboard = InlineKeyboardMarkup()
        button1 = InlineKeyboardButton("Відкрити сайт середовища для програмування", url="https://codehs.com/")
        button2 = InlineKeyboardButton("Відкрити сайт школи", url="https://justschool.me/uk")
        keyboard.add(button1, button2)
        bot.send_message(message.chat.id, "Обери дію:", reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, "Я не знаю такої команди, спробуй натиснути на кнопку 😊")
# Команда /help: відправляє повідомлення з підказками
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Я можу допомогти тобі з основними командами: /start, /help")
@bot.message_handler(commands=["telljoke"])
def tell_joke(message):
    bot.reply_to(message, "ТУТ МАВ БУТИ ЖАРТ. АХАХАХАХ")
@bot.message_handler(commands=["info"])
def tell_joke(message):
    bot.reply_to(message, "Я — бот, який допомагає з програмуванням і вміє жартувати!")
@bot.message_handler(commands=["random"])
def random_message(message):
    a = random.randint(1,10)
    bot.reply_to(message, f"Random number {a}")
bot.polling()"""


"""import time
import schedule
def remainder():
    print("Нагадування час зробити перерву!")

schedule.every(5).seconds.do(remainder)
while True:
    schedule.run_pending()
    time.sleep(1)"""

"""import telebot
import schedule
import time

# Токен бота
TOKEN = "8179890010:AAFwchBdpwhE3kSVADDJqsxFneuIOL3NGpo"
bot = telebot.TeleBot(TOKEN)

# ID користувача
CHAT_ID = 836948105 # Введи ID чату (@userinfobot)

# Налаштування розкладу
def send_reminder():
    bot.send_message(CHAT_ID, "Час зробити важливу справу!")

# Заплановані нагадування
schedule.every().day.at("09:00").do(send_reminder)
schedule.every().day.at("18:00").do(send_reminder)
schedule.every(10).seconds.do(send_reminder)

# Основний цикл
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(f"Помилка: {e}")
        time.sleep(5)"""


#method split
#1
"""students = "Андрій, Олена, Микола, Світлана, Юлія, Дмитро"
students_list = students.split(",")
print(students_list)
com1 = students_list[0:3]
com2 = students_list[3:6]
print(com1)
print(com2)
#2
dates = "25.12.2021, 01.01.2020, 5.15.2023"
dates_list = dates.split(", ")
print(dates_list)
years = []
for date in dates_list:
    year = date[-4:]
    years.append(year)

print(years)
#3
url = "https://example.com?page=5&sort=asc&filter=new"
query = url.split("?")[1]
params = query.split("&")
print(params)
for param in params:
    key,value = param.split("=")
    print(key,"=", value)

"""
"""import telebot
TOKEN = '8179890010:AAFwchBdpwhE3kSVADDJqsxFneuIOL3NGpo'
# Встав токен, який надіслав BotFather
bot = telebot.TeleBot(TOKEN)
chat_id = 836948105 # Введи ID чату (@userinfobot)

def convert_unit(value, from_units, to_units):
    conversions ={
        "чашки": {"мілілітри":240},
        "столові_ложки": {"мілілітри": 15},
        "чайні_ложки": {"мілілітри":5},
        "склянки": {"мілілітри":250}
    }
    if from_units in conversions and to_units in conversions[from_units]:
        return value * conversions[from_units][to_units]
    else:
        return None
@bot.message_handler(commands=["start"])
def send_hello(message):
    bot.send_message(message.chat.id, "Привіт! Я допоможу тобі конвертувати задану кількість чашок, ложок, склянок у мілілітри.\
        Напиши в такому форматі: 5 чашки в мілілітри.")
@bot.message_handler(func=lambda message: True)
def hanle_message(message):
    text = message.text.lower()
    try:
        parts = text.split(" в ")
        value_and_from_unit = parts[0].split()
        to_unit = parts[1]
        value = float(value_and_from_unit[0])
        from_unit = value_and_from_unit[1]
        result = convert_unit(value, from_unit, to_unit)
        if result is not None:
            bot.send_message(message.chat.id, f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            bot.send_message(message.chat.id, "перепрошую, спробуйте ще раз")
    except Exception as e:
        bot.send_message(message.chat.id, "Все погано у тебе помилка в коді!")

bot.polling() """


"""
import telebot
import random

TOKEN = '8179890010:AAFwchBdpwhE3kSVADDJqsxFneuIOL3NGpo'
bot = telebot.TeleBot(TOKEN)

# Шлях до папки, де зберігаються меми
UPLOAD_FOLDER = r"C:\memes"

# Список, де ми зберігатимемо назви файлів з мемами
memes = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg", "11.jpg", "12.jpg", "13.jpg", 
         "14.jpg", "15.jpg", "16.jpg", "17.jpg", "18.jpg", "19.jpg", "20.jpg"]

@bot.message_handler(content_types=['photo'])
def receive_meme(message):

# Дістаємо інформацію про надісланий файл із мемом
    file_info = bot.get_file(message.photo[-1].file_id)

# Завантажуємо файл з мемом
    downloaded_file = bot.download_file(file_info.file_path)
# Зберігаємо мем на комп'ютері під унікальним іменем
    file_name = str(len(memes) + 1) + ".jpg"
    with open(UPLOAD_FOLDER + file_name, 'wb') as new_file:

        new_file.write(downloaded_file)

# Додаємо назву мема в список memes
    memes.append(file_name)

    bot.reply_to(message, "Мем отримано і збережено!")

@bot.message_handler(commands=['meme'])
def send_random_meme(message):

    if memes:
        meme = random.choice(memes)
        with open(UPLOAD_FOLDER + meme, 'rb') as photo:

            bot.send_photo(message.chat.id, photo)

    else:

        bot.reply_to(message, "Мемів поки немає :(")

bot.polling()
"""

"""import telebot
import requests
TELEGRAM_BOT_TOKEN = "8179890010:AAFwchBdpwhE3kSVADDJqsxFneuIOL3NGpo"
COHERE_API_KEY = "tVr39gH3rv4KliCVInUmdgMC5T7C1xhV0xNZWKRl"
COHERE_API_URL = "https://api.cohere.ai/generate"
RESPONSE_MODE = "коротко"
RESPONSE_STYLE = "серйозний"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
# Функція для генерації тексту через Cohere API
def generate_text(prompt):
    if RESPONSE_STYLE == "жартівливий":
        prompt = f"Зроби цю відповідь веселою: {prompt}"
        # Стиль "серйозний" нічого не змінює в prompt
        data = {
            "model": "command-xlarge-nightly",
            "prompt": prompt,
            "max_tokens": 150,
        }
    headers = {
        "Authorization": f"Bearer {COHERE_API_KEY}",
        "Content-Type": "application/json",
    }
    max_tokens = 50 if RESPONSE_MODE == "коротко" else 150
    data = {
    "model": "command-xlarge-nightly", # Використовується модель для генерації тексту
    "prompt": prompt,
    "max_tokens": max_tokens, # Максимальна кількість токенів
    }
    try:
        response = requests.post(COHERE_API_URL, json=data, headers=headers)
        if response.status_code == 200:
            response_data = response.json() 
            generation = response_data["text"]
            return generation
    except Exception as e:
        return f"Помилка: {e}"
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Напиши мені текст, і я спробую продовжити його за допомогою Cohere API.")

@bot.message_handler(commands=["mode"])
def select_mode(message):
    bot.reply_to(message, "Обери режим відповіді: коротко або детально.")
    bot.register_next_step_handler(message, set_mode)

def set_mode(message):
    global RESPONSE_MODE
    if message.text.lower() == "коротко":
        RESPONSE_MODE = "коротко"
        bot.reply_to(message, "Режим встановлено: коротка відповідь.")
    elif message.text.lower() == "детально":
        RESPONSE_MODE = "детально"
        bot.reply_to(message, "Режим встановлено: детальна відповідь.")
    else:
        bot.reply_to(message, "Невідомий режим. Спробуйте ще раз.")

@bot.message_handler(commands=["style"])
def select_style(message):
    bot.reply_to(message, "Обери стиль відповіді: жартівливий або серйозний.")
    bot.register_next_step_handler(message, set_style)
def set_style(message):
    global RESPONSE_STYLE
    if message.text.lower() == "жартівливий":
        RESPONSE_STYLE = "жартівливий"
        bot.reply_to(message, "Стиль встановлено: жартівливий.")
    elif message.text.lower() == "серйозний":
        RESPONSE_STYLE = "серйозний"
        bot.reply_to(message, "Стиль встановлено: серйозний.")
    else:
        bot.reply_to(message, "Невідомий стиль. Спробуйте ще раз.")

# Обробка текстових повідомлень
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    bot.reply_to(message, "Генерую відповідь, зачекайте...")
    generated_text = generate_text(user_input)
    bot.send_message(message.chat.id, generated_text)

if __name__ == "__main__":
    print("Бот запущено!")
    bot.polling()
"""