class Calculator:
    def __init__(self):
        self.reset()
        self.operation_symbols = ["÷", "×", "-", "+", "=", "√"]
        self.control_symbols = ["AC", "+/-", "%"]

    def reset(self):
        self.expression_string = "0"
        self.last_input_was_operator = False

    def append_to_expression(self, value):
        current_length = len(self.expression_string.replace(" ", ""))
        if current_length >= 8:
            return

        if self.expression_string == "0" and value.isdigit():
            self.expression_string = value
        else:
            self.expression_string += value

        self.last_input_was_operator = value in self.operation_symbols

    def get_expression(self):
        return self.expression_string

    def evaluate_expression(self):
        try:
            safe_expression = (
                self.expression_string
                .replace("×", "*")
                .replace("÷", "/")
            )
            result = eval(safe_expression)
            self.reset()
            return result
        except Exception:
            self.reset()
            return "Error"