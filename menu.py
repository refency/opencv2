from tkinter import Tk, StringVar, Frame, Radiobutton, Button, Label

from func import open_file, connect_webcam, highlight_red_intensity, sharpen_image, draw_green_line

def main_menu():
    # Определяем объект tkinter'а для пользовательского интерфейса
    root = Tk()

    # Название формы
    root.title("Выбор изображения")

    # Устанавливаем минимальные размеры окна
    root.minsize(1024, 768)

    # Добавляем стилизацию окна
    root.configure(bg = 'lightblue')

    # Переменная для хранения выбранного канала
    channel = StringVar()
    channel.set("rgb")

    # Создаем фрейм для радиокнопок
    radio_frame = Frame(root, bg = 'lightblue')
    radio_frame.pack(pady=20)

    # Создаем радиокнопки для выбора канала
    Radiobutton(radio_frame, text = "RGB", variable = channel, value = "rgb",
                font = ("Arial", 14), bg = 'lightblue').pack(anchor = 'w')
    Radiobutton(radio_frame, text = "Красный", variable = channel, value = "red",
                font = ("Arial", 14), bg = 'lightblue').pack(anchor = 'w')
    Radiobutton(radio_frame, text = "Зеленый", variable = channel, value = "green",
                font = ("Arial", 14), bg = 'lightblue').pack(anchor = 'w')
    Radiobutton(radio_frame, text = "Синий", variable = channel, value = "blue",
                font = ("Arial", 14), bg = 'lightblue').pack(anchor='w')

    # Создаем фрейм для кнопок основного функционала
    button_frame = Frame(root, bg='lightblue')
    button_frame.pack(pady=20)

    Button(button_frame, text = "Выбрать и загрузить изображение",
            command = lambda: open_file(channel.get(), root), font = ("Arial", 14),
            bg = 'white', fg = 'black', width = 40, height = 2).pack(pady = 10)
    Button(button_frame, text = "Подключиться к веб-камере и сделать с нее фотоснимок",
            command = lambda: connect_webcam(channel.get(), root), font = ("Arial", 14),
            bg = 'white', fg = 'black', width = 40, height = 3, wraplength = 300).pack(pady = 10)

    # Создаем фрейм для кнопок дополнительного функционала
    additional_frame = Frame(root, bg='lightblue')
    additional_frame.pack(pady=20)

    label_additional_menu = Label(additional_frame, text="Дополнительный функционал",
                    font = ("Arial", 14), bg = 'lightblue', fg = 'black')
    label_additional_menu.pack()

    Button(additional_frame, text = "Выделить части изображения с высокой интенсивностью красного",
            command = lambda: highlight_red_intensity(root), font = ("Arial", 14),
            bg = 'white', fg = 'black', width = 40, height = 3, wraplength = 300).pack(pady = 10)
    Button(additional_frame, text = "Повысить резкость изображения",
            command = lambda: sharpen_image(root), font = ("Arial", 14),
            bg = 'white', fg = 'black', width = 40, height = 2, wraplength = 300).pack(pady = 10)
    Button(additional_frame, text = "Нарисовать зеленую линию на изображении",
            command = lambda: draw_green_line(root), font = ("Arial", 14),
            bg = 'white', fg = 'black', width = 40, height = 2, wraplength = 300).pack(pady = 10)

    # Запускаем главный цикл обработки событий
    root.mainloop()
