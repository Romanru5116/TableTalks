#test key press
import tkinter as tk
 
def button1_click():
    label.config(text="Сервис1_заказан")

def button2_click():
    label.config(text="Сервис2_заказан")

root = tk.Tk()
root.title("примеры кнопок")
button1 = tk.Button(root,
                   text="Сервис1",
                   command=button1_click,
                   width=15,
                   height=2)

button2=tk.Button(root,
                 text="Сервис2",
                 command=button2_click,
                 width=15,
                 height=2)
# Размещаем кнопку в окне
button1.pack(pady=20)
button2.pack(pady=20)
# метка для отображения текста
label = tk.Label(root, text="")
label.pack()

root.mainloop()
