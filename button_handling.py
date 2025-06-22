from calculator_core import Calculator
from utility_function import format_number

class ButtonClickHandler:
    def __init__(self, display_label):
        self.display_label = display_label
        self.calculator = Calculator()