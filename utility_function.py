class Format:
    @staticmethod
    def format_number(number_value):
        return str(int(number_value)) if number_value % 1 == 0 else str(number_value)