class Calculator:
    def __init__(self):
        self.reset()
        self.operation_symbols = ["÷", "×", "-", "+", "=", "√"]
        self.control_symbols = ["AC", "+/-", "%"]

    def reset(self):
        self.expression_string = "0"
        self.last_input_was_operator = False
        self.operand_count = 0

    def append_to_expression(self, value):
        if value.isdigit():
            if self.expression_string == "0":
                self.expression_string = value
                self.operand_count = 1
            else:
                if self.last_input_was_operator:
                    if self.operand_count >= 8:
                        return
                    self.operand_count += 1
                self.expression_string += value
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