from tkinter import Frame, Label, Button
from button_handling import ButtonClickHandler

class CalculatorUI:
    def __init__(self, root_window):
        self.root_window = root_window
        self.root_window.title("OOP Calculator")
        self.root_window.resizable(False, False)

        self.button_layout = [
            ["AC", "+/-", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "√", "="]
        ]
        self.operation_buttons = ["÷", "×", "-", "+", "=", "√"]
        self.control_buttons = ["AC", "+/-", "%"]
        self.total_rows = len(self.button_layout)
        self.total_columns = len(self.button_layout[0])

        self.color_theme = {
            "light_gray": "#D4D4D2",
            "black": "#1C1C1C",
            "dark_gray": "#505050",
            "orange": "#FF9500",
            "white": "white"
        }

        self.main_frame = Frame(self.root_window)
        self.display_label = Label(
            self.main_frame, text="0", font=("Arial", 45),
            background=self.color_theme["black"],
            foreground=self.color_theme["white"],
            anchor="e", width=self.total_columns
        )
        self.display_label.grid(row=0, column=0, columnspan=self.total_columns, sticky="we")

        self.button_click_handler = ButtonClickHandler(self.display_label)

        self.create_buttons()
        self.main_frame.pack()
        self.center_window()

    def create_buttons(self):
        for row_index, row in enumerate(self.button_layout):
            for column_index, button_text in enumerate(row):
                button = Button(
                    self.main_frame, text=button_text, font=("Arial", 30),
                    width=self.total_columns - 1, height=1,
                    command=lambda value=button_text: self.button_click_handler.handle_click(value)
                )

                if button_text in self.control_buttons:
                    button.config(foreground=self.color_theme["black"], background=self.color_theme["light_gray"])
                elif button_text in self.operation_buttons:
                    button.config(foreground=self.color_theme["white"], background=self.color_theme["orange"])
                else:
                    button.config(foreground=self.color_theme["white"], background=self.color_theme["dark_gray"])

                button.grid(row=row_index + 1, column=column_index)

    def center_window(self):
        self.root_window.update()
        width = self.root_window.winfo_width()
        height = self.root_window.winfo_height()
        screen_width = self.root_window.winfo_screenwidth()
        screen_height = self.root_window.winfo_screenheight()
        position_x = (screen_width // 2) - (width // 2)
        position_y = (screen_height // 2) - (height // 2)
        self.root_window.geometry(f"{width}x{height}+{position_x}+{position_y}")

    def run(self):
        self.root_window.mainloop()