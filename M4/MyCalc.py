class MyCalc:
    def __init__(self):
        # psk 10/14/2023 Initialize the calculator with an initial answer value of 0.
        self.ans = 0

    def _is_float(self, val):
        # psk 10/14/2023 Check if a given value can be converted to a floating-point number.
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        # psk 10/14/2023 Check if a given value can be converted to an integer.
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        # psk 10/14/2023 Convert a given value to a numeric type (either int or float).
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise ValueError("Not a valid number")

    def add(self, num1, num2):
        # psk 10/14/2023 Perform addition of two numbers or numeric values and update the answer.
        num1 = self._as_number(num1)
        num2 = self._as_number(num2)
        self.ans = num1 + num2
        return self.ans

    def sub(self, num1, num2):
        # psk 10/14/2023 Perform subtraction of two numbers or numeric values and update the answer.
        num1 = self._as_number(num1)
        num2 = self._as_number(num2)
        self.ans = num1 - num2
        return self.ans

    def multiply(self, num1, num2):
        # psk 10/14/2023 Perform multiplication of two numbers or numeric values and update the answer.
        num1 = self._as_number(num1)
        num2 = self._as_number(num2)
        self.ans = num1 * num2
        return self.ans

    def divide(self, num1, num2):
        # psk 10/14/2023 Perform division of two numbers or numeric values and update the answer,
        # while also handling the case where the divisor is zero.
        num1 = self._as_number(num1)
        num2 = self._as_number(num2)
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        self.ans = num1 / num2
        return self.ans

# psk 10/14/2023 Main logic to run when the program runs
if __name__ == "__main":
    calc = MyCalc()
    while True:
        user_input = input("Enter a calculation (e.g., 2 * 2 or ans + 5): ")
        if user_input.lower() == "exit":
            break
        try:
            if "ans" not in user_input:
                result = eval(user_input)
                calc.ans = result
            else:
                result = eval(user_input, {"ans": calc.ans})
                calc.ans = result
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {str(e)}")