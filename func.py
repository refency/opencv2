import cv2
import matplotlib.pyplot as plt

from tkinter import simpledialog
from tkinter.filedialog import askopenfilename

import numpy

def open_file(channel, root):
    file_path = file_name()
    if not file_path:return

    withdraw_window(root)

    try:
        # Изображение разбирается как матрица на отдельные пиксели
        # и создается массив для его чтения компьютером
        image = cv2.imread(file_path, cv2.IMREAD_COLOR)

        # Переключаем цветовое пространство из BGR в RGB для Matplotlib
        reversed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Выбираем канал изображения на основе пользовательского выбора
        if channel == 'red':
            reversed_image = reversed_image[:, :, 0]
        elif channel == 'green':
            reversed_image = reversed_image[:, :, 1]
        elif channel == 'blue':
            reversed_image = reversed_image[:, :, 2]
        else:
            reversed_image = reversed_image

        # Создаем окно для отображения изображения
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)

        # Отрисовываем изображение
        if channel in ['red', 'green', 'blue']:
            ax.imshow(reversed_image, cmap='gray')
        else:
            ax.imshow(reversed_image)

        # Выводим изображение в отдельном окне
        plt.show()
        
        deinconify_window(root)
    except Exception as e:
        print(f"При загрузке изображения произошла ошибка: {e}")

def connect_webcam(channel, root):
    withdraw_window(root)

    try:
        # Подключаемся к первой камере устройства 
        cap = cv2.VideoCapture(0)

        # Делаем снимок экрана
        # ret - возвращает true/false при успешном считывании кадра
        # frame - кадр в виде многомерного массива, в формате BGR
        ret, frame = cap.read()

        # Освобождаем ресурсы
        cap.release()

        # Переключаем цветовое пространство из BGR в RGB для Matplotlib
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Выбираем канал изображения на основе пользовательского выбора
        if channel == 'red':
            frame_rgb = frame_rgb[:, :, 0]
        elif channel == 'green':
            frame_rgb = frame_rgb[:, :, 1]
        elif channel == 'blue':
            frame_rgb = frame_rgb[:, :, 2]

        # fig - объект фигуры(окно или область, содержащий график), содержащий несколько осей
        # ax - объект оси, область графика куда наносятся данные
        # Создаем окно для отображения изображения
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)

        # Отрисовываем изображение
        if channel in ['red', 'green', 'blue']:
            ax.imshow(frame_rgb, cmap='gray')
        else:
            ax.imshow(frame_rgb)

        # Выводим изображение в отдельном окне
        plt.show()

        # Конвертируем в BGR для сохранения, поскольку изображение прошло обработку
        frame_rgb_cv2 = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)  

        # Сохраняем кадр в указанный файл
        cv2.imwrite("./pictures/screenshot.jpg", frame_rgb_cv2)
        print("Кадр сохранен в корневой папке, под названием: screenshot.jpg")
    except Exception as e:
        print(f"Произошла ошибка создании фотоснимка с камеры: {e}")
        
    deinconify_window(root)


def highlight_red_intensity(root):
    file_path = file_name()
    if not file_path:return
    
    withdraw_window(root)
    
    try:
        # Запрашиваем пороговое значение у пользователя
        threshold = simpledialog.askinteger(
            "Пороговое значение",
            "Введите пороговое значение для красного канала (0-255):",
            minvalue=0, maxvalue=255
        )

        if threshold is None: return

        image = cv2.imread(file_path, cv2.IMREAD_COLOR)

        reversed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Выделяем части изображения с интенсивностью красного цвета выше заданного порога
        red_channel = reversed_image[:, :, 0]
        mask = red_channel > threshold

        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)

        ax.imshow(mask, cmap='gray')

        plt.show()
        
        deinconify_window(root)
    except Exception as e:
        print(f"При загрузке изображения произошла ошибка: {e}")
        
def sharpen_image(root):
    file_path = file_name()
    if not file_path:return

    withdraw_window(root)

    try:
        image = cv2.imread(file_path, cv2.IMREAD_COLOR)

        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Применяем фильтр для повышения резкости
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
        sharpened_image = cv2.filter2D(rgb_image, -1, kernel)

        # Показываем изображение до и после обработки с использованием Matplotlib
        fig, axes = plt.subplots(1, 2, figsize=(12, 6))
        axes[0].imshow(rgb_image)
        axes[0].set_title('Исходное изображение')
        axes[0].axis('off')

        axes[1].imshow(sharpened_image)
        axes[1].set_title('Улучшенное изображение (повышение резкости)')
        axes[1].axis('off')

        plt.tight_layout()
        plt.show()
        
        deinconify_window(root)
    except Exception as e:
        print(f"При загрузке или обработке изображения произошла ошибка: {e}")

def draw_green_line(root):
    file_path = file_name()
    if not file_path:return

    withdraw_window(root)

    try:
        # Загрузка изображения
        image = cv2.imread(file_path)

        # Запрашиваем координаты начала и конца линии
        x1 = simpledialog.askinteger("Координаты линии", "Введите x1:")
        y1 = simpledialog.askinteger("Координаты линии", "Введите y1:")
        x2 = simpledialog.askinteger("Координаты линии", "Введите x2:")
        y2 = simpledialog.askinteger("Координаты линии", "Введите y2:")

        # Запрашиваем толщину линии
        thickness = simpledialog.askinteger("Толщина линии", "Введите толщину линии:")

        # Рисуем зеленую линию на изображении
        # Зеленый цвет в формате BGR
        color = (0, 255, 0)  
        cv2.line(image, (x1, y1), (x2, y2), color, thickness)

        # Отображаем изображение с нарисованной линией
        plt.imshow(image[:,:,::-1])
        plt.show()
        
        deinconify_window(root)
    except Exception as e:
        print(f"При рисовании линии произошла ошибка: {e}")
        
def file_name():
    # Открываем диалоговое окно для выбора файла и разрешаем пользователю выбрать файл изображения
    file_path = askopenfilename(filetypes=[("Файлы изображений", "*.jpg;*.png;")])

    return file_path

def withdraw_window(root):
    # Прячем основное окно
    root.withdraw()
    
def deinconify_window(root):
    # Закрываем основное окно tkinter
    root.deiconify()