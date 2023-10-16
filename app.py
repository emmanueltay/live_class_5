from flask import Flask, render_template
app = Flask(__name__)

@app.route('/fizzbuzz')
def fizzbuzz():
    digits = []
    for i in range(1,101):
        digits.append(i)

    outcome = []

    for digit in digits:
        if digit % 3 == 0 and digit % 5 == 0:
            outcome.append("FizzBuzz")
        elif digit % 3 == 0:
            outcome.append("Fizz")
        elif digit % 5 == 0:
            outcome.append("Buzz")
        else:
            outcome.append(digit)

    return render_template('FizzBuzz_template.html', outcome = outcome)

if __name__ == '__main__':
    app.run()