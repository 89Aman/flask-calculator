from flask import Flask, render_template, request

app = Flask(__name__)

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["task"]

            if operation == "+":
                result = Calculator.add(num1, num2)
            elif operation == "-":
                result = Calculator.subtract(num1, num2)
            elif operation == "*":
                result = Calculator.multiply(num1, num2)
            elif operation == "/":
                result = Calculator.divide(num1, num2)

        except ValueError:
            result = "Invalid input"
        except ZeroDivisionError:
            result = "Cannot divide by zero"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
