from calculator_core import Calculator
from utility_function import format_number

class ButtonClickHandler:
    def __init__(self, display_label):
        self.display_label = display_label
        self.calculator = Calculator()
    
    def handle_click(self, button_value):
        if button_value in self.calculator.operation_symbols:
            if button_value == "=":
                self.calculator.second_operand = self.display_label["text"]
                result = self.calculator.calculate_result()
                self.display_label["text"] = format_number(result)
            else:
                self.calculator.first_operand = self.display_label["text"]
                self.calculator.operator = button_value
                self.display_label["text"] = "0"

        elif button_value in self.calculator.control_symbols:
            if button_value == "AC":
                self.calculator.reset()
                self.display_label["text"] = "0"
            elif button_value == "+/-":
                inverted = float(self.display_label["text"]) * -1
                self.display_label["text"] = format_number(inverted)
            elif button_value == "%":
                percent = float(self.display_label["text"]) / 100
                self.display_label["text"] = format_number(percent)

        elif button_value == ".":
            if "." not in self.display_label["text"]:
                self.display_label["text"] += "."

        elif button_value.isdigit():
            if self.display_label["text"] == "0":
                self.display_label["text"] = button_value
            else:
                self.display_label["text"] += button_value