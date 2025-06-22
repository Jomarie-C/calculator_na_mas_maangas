class Calculator:
    def __init__(self):
        self.first_operand = "0"
        self.second_operand = None
        self.operator = None
        self.operation_symbols = ["÷", "×", "-", "+", "="]
        self.control_symbols = ["AC", "+/-", "%"]

    def reset(self):
        self.first_operand = "0"
        self.second_operand = None
        self.operator = None

    def calculate_result(self):
        try:
            operand1 = float(self.first_operand)
            operand2 = float(self.second_operand)

            if self.operator == "+":
                return operand1 + operand2
            elif self.operator == "-":
                return operand1 - operand2
            elif self.operator == "×":
                return operand1 * operand2
            elif self.operator == "÷":
                return operand1 / operand2
        finally:
            self.reset()