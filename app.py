from flask import Flask, render_template
app = Flask(__name__)
@app.route("/fizzbuzz")

def fizzbuzz():
    numbers = []

    for number in range(1,100 + 1):
        if (number % 3 == 0) and (number % 5 == 0):
            numbers.append("FizzBuzz")
        elif number % 3 == 0:
            numbers.append("Fizz")
        elif number % 5 == 0:
            numbers.append("Buzz")
        else:
            numbers.append(number)

    return render_template("fizzbuzz.html", numbers=numbers)

if __name__ == "__main__":
    app.run()