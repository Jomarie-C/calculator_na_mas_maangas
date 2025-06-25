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
                result = self.calculator.evaluate_expression()
                self.display_label["text"] = Format.format_number(result) if result != "Error" else result
            elif button_value == "√":
                try:
                    value = float(self.display_label["text"])
                    square_root = math.sqrt(value)
                    self.display_label["text"] = Format.format_number(square_root)
                    self.calculator.expression_string = self.display_label["text"]
                except ValueError:
                    self.display_label["text"] = "Error"
                    self.calculator.reset()
            else:
                if not self.calculator.last_input_was_operator:
                    self.calculator.append_to_expression(button_value)
                    self.display_label["text"] = self.calculator.get_expression()

        elif button_value in self.calculator.control_symbols:
            if button_value == "AC":
                self.calculator.reset()
                self.display_label["text"] = "0"
            elif button_value == "+/-":
                try:
                    inverted = float(self.display_label["text"]) * -1
                    self.display_label["text"] = Format.format_number(inverted)
                    self.calculator.expression_string = self.display_label["text"]
                except ValueError:
                    self.display_label["text"] = "Error"
                    self.calculator.reset()
            elif button_value == "%":
                try:
                    percentage = float(self.display_label["text"]) / 100
                    self.display_label["text"] = Format.format_number(percentage)
                    self.calculator.expression_string = self.display_label["text"]
                except ValueError:
                    self.display_label["text"] = "Error"
                    self.calculator.reset()

        elif button_value == ".":
            if "." not in self.display_label["text"].split()[-1]:
                self.calculator.append_to_expression(".")
                self.display_label["text"] = self.calculator.get_expression()

        elif button_value.isdigit():
            self.calculator.append_to_expression(button_value)
            self.display_label["text"] = self.calculator.get_expression()