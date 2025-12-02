import flet as ft
import math


def main(page: ft.Page):
    # Настройка страницы
    page.title = "Инженерный калькулятор"
    page.window.width = 500
    page.window.height = 700
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Переменные калькулятора
    current_input = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        width=440,
        height=70,
        text_size=28,
    )

    memory_value = 0

    #     ОБРАБОТЧИКИ

    def button_click(e):
        if current_input.value == "0" or current_input.value == "Error":
            current_input.value = e.control.text
        else:
            current_input.value += e.control.text
        page.update()

    def clear_click(e):
        current_input.value = "0"
        page.update()

    def clear_entry_click(e):
        current_input.value = "0"
        page.update()

    def backspace_click(e):
        if current_input.value not in ["0", "Error"]:
            if len(current_input.value) > 1:
                current_input.value = current_input.value[:-1]
            else:
                current_input.value = "0"
        page.update()

    def equals_click(e):
        try:
            expression = current_input.value
            expression = expression.replace('π', str(math.pi))
            expression = expression.replace('e', str(math.e))
            expression = expression.replace('^', '**')
            expression = expression.replace('√', 'math.sqrt')
            expression = expression.replace('sin', 'math.sin')
            expression = expression.replace('cos', 'math.cos')
            expression = expression.replace('tan', 'math.tan')
            expression = expression.replace('log', 'math.log10')
            expression = expression.replace('ln', 'math.log')

            result = eval(expression)
            current_input.value = str(result)
        except:
            current_input.value = "Error"

        page.update()

    def scientific_function(e):
        try:
            value = float(current_input.value)
            function = e.control.text

            if function == "sin":
                result = math.sin(math.radians(value))
            elif function == "cos":
                result = math.cos(math.radians(value))
            elif function == "tan":
                result = math.tan(math.radians(value))
            elif function == "√":
                result = math.sqrt(value)
            elif function == "x²":
                result = value ** 2
            elif function == "x³":
                result = value ** 3
            elif function == "1/x":
                result = 1 / value
            elif function == "log":
                result = math.log10(value)
            elif function == "ln":
                result = math.log(value)
            elif function == "π":
                result = math.pi
            elif function == "e":
                result = math.e
            else:
                result = value

            current_input.value = str(result)
        except:
            current_input.value = "Error"

        page.update()

    def memory_add(e):
        nonlocal memory_value
        try:
            memory_value += float(current_input.value)
        except:
            pass

    def memory_subtract(e):
        nonlocal memory_value
        try:
            memory_value -= float(current_input.value)
        except:
            pass

    def memory_recall(e):
        current_input.value = str(memory_value)
        page.update()

    def memory_clear(e):
        nonlocal memory_value
        memory_value = 0

    #     СТИЛИ КНОПОК

    green_bright_button = ft.ButtonStyle(bgcolor="#00cc44", color="#ffffff")  # для C, CE
    green_dark_button = ft.ButtonStyle(bgcolor="#145a32", color="#ffffff")
    green_accent_button = ft.ButtonStyle(bgcolor="#1e8449", color="#ffffff")  # для "="

    btn_width = 80
    btn_height = 55

    #     КОНФИГУРАЦИЯ КНОПОК

    buttons = [
        [
            ft.ElevatedButton("MC", on_click=memory_clear, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("MR", on_click=memory_recall, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("M+", on_click=memory_add, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("M-", on_click=memory_subtract, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("CE", on_click=clear_entry_click, width=btn_width, height=btn_height, style=green_bright_button),
        ],
        [
            ft.ElevatedButton("sin", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("cos", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("tan", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("√", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("C", on_click=clear_click, width=btn_width, height=btn_height, style=green_bright_button),
        ],
        [
            ft.ElevatedButton("x²", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("x³", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("1/x", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("⌫", on_click=backspace_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("/", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
        ],
        [
            ft.ElevatedButton("7", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("8", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("9", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("log", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("*", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
        ],
        [
            ft.ElevatedButton("4", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("5", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("6", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("ln", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("-", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
        ],
        [
            ft.ElevatedButton("1", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("2", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("3", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("π", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("+", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
        ],
        [
            ft.ElevatedButton("0", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton(".", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("e", on_click=scientific_function, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("^", on_click=button_click, width=btn_width, height=btn_height, style=green_dark_button),
            ft.ElevatedButton("=", on_click=equals_click, width=btn_width, height=btn_height, style=green_accent_button),
        ],
    ]

    #      ОСНОВНОЙ ИНТЕРФЕЙС

    calculator = ft.Container(
        width=460,
        padding=20,
        bgcolor="#0d261a",
        border_radius=15,
        content=ft.Column(
            [
                ft.Container(
                    width=440,
                    height=80,
                    padding=15,
                    bgcolor="#001a0d",
                    border_radius=10,
                    content=current_input,
                ),
                *[ft.Row(
                    row_buttons,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    spacing=5
                ) for row_buttons in buttons],
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    page.add(calculator)

if __name__ == "__main__":
    ft.app(target=main)