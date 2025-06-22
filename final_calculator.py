from tkinter import Tk
from user_interface import CalculatorUI

if __name__ == "__main__":
    window = Tk()
    calculator_ui = CalculatorUI(window)
    calculator_ui.run()