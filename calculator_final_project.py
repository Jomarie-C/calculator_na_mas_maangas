import tkinter

button_layout = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

operation_symbols = ["÷", "×", "-", "+", "="]
control_symbols = ["AC", "+/-", "%"]

total_rows = len(button_layout)
total_columns = len(button_layout[0])

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500"
color_white = "white"

calculator_window = tkinter.Tk()
calculator_window.title("Calculator")
calculator_window.resizable(False, False)

main_frame = tkinter.Frame(calculator_window)
display_label = tkinter.Label(
    main_frame, text="0", font=("Arial", 45),
    background=color_black, foreground=color_white,
    anchor="e", width=total_columns
)

display_label.grid(row=0, column=0, columnspan=total_columns, sticky="we")

for row_index in range(total_rows):
    for column_index in range(total_columns):
        button_text = button_layout[row_index][column_index]
        button = tkinter.Button(
            main_frame, text=button_text, font=("Arial", 30),
            width=total_columns-1, height=1,
            command=lambda val=button_text: on_button_click(val)
        )

        if button_text in control_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif button_text in operation_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)

        button.grid(row=row_index + 1, column=column_index)

main_frame.pack()

first_operand = "0"
current_operator = None
second_operand = None

def reset_calculator():
    global first_operand, second_operand, current_operator
    first_operand = "0"
    current_operator = None
    second_operand = None

def format_number(value):
    return str(int(value)) if value % 1 == 0 else str(value)

def on_button_click(value):
    global display_label, first_operand, second_operand, current_operator

    if value in operation_symbols:
        if value == "=":
            if first_operand is not None and current_operator is not None:
                second_operand = display_label["text"]
                result = perform_calculation(float(first_operand), float(second_operand), current_operator)
                display_label["text"] = format_number(result)
                reset_calculator()
        else:
            if current_operator is None:
                first_operand = display_label["text"]
                display_label["text"] = "0"
                second_operand = "0"
            current_operator = value

    elif value in control_symbols:
        if value == "AC":
            reset_calculator()
            display_label["text"] = "0"
        elif value == "+/-":
            inverted_value = float(display_label["text"]) * -1
            display_label["text"] = format_number(inverted_value)
        elif value == "%":
            percentage_value = float(display_label["text"]) / 100
            display_label["text"] = format_number(percentage_value)

    elif value == ".":
        if "." not in display_label["text"]:
            display_label["text"] += value

    elif value in "0123456789":
        current_text = display_label["text"]
        display_label["text"] = value if current_text == "0" else current_text + value

def perform_calculation(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "×":
        return operand1 * operand2
    elif operator == "÷":
        return operand1 / operand2

calculator_window.update()
window_width = calculator_window.winfo_width()
window_height = calculator_window.winfo_height()
screen_width = calculator_window.winfo_screenwidth()
screen_height = calculator_window.winfo_screenheight()

center_x = int((screen_width / 2) - (window_width / 2))
center_y = int((screen_height / 2) - (window_height / 2))

calculator_window.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
calculator_window.mainloop()
