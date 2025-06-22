import math
from calculator_core import Calculator
from utility_function import Format

class ButtonClickHandler:
    def __init__(self, display_label):
        self.display_label = display_label
        self.calculator = Calculator()
    
    def handle_click(self, button_value):
        if button_value in self.calculator.operation_symbols:
            if button_value == "=":
                self.calculator.second_operand = self.display_label["text"]
                result = self.calculator.calculate_result()
                if isinstance(result, str):
                    self.display_label["text"] = result
                else:
                    self.display_label["text"] = Format.format_number(result)
            elif button_value == "√":
                try:
                    square_root = math.sqrt(float(self.display_label["text"]))
                    self.display_label["text"] = Format.format_number(square_root)
                except ValueError:
                    self.display_label["text"] = "Error"
            else:
                self.calculator.first_operand = self.display_label["text"]
                self.calculator.operator = button_value
                self.display_label["text"] = "0"

        elif button_value in self.calculator.control_symbols:
            if button_value == "AC":
                self.calculator.reset()
                self.display_label["text"] = "0"
            elif button_value == "+/-":
                try:
                    inverted = float(self.display_label["text"]) * -1
                    self.display_label["text"] = Format.format_number(inverted)
                except ValueError:
                    self.display_label["text"] = "Error"
            elif button_value == "%":
                try:
                    percentage = float(self.display_label["text"]) / 100
                    self.display_label["text"] = Format.format_number(percentage)
                except ValueError:
                    self.display_label["text"] = "Error"

        elif button_value == ".":
            if "." not in self.display_label["text"]:
                self.display_label["text"] += "."

        elif button_value.isdigit():
            if self.display_label["text"] == "0":
                self.display_label["text"] = button_value
            else:
                self.display_label["text"] += button_value
