from flask import Flask, render_template
app = Flask(__name__)

@app.route('/fizzbuzz')
def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            return render_template('FizzBuzz_template.html', item= "FizzBuzz")
        elif i % 3 == 0:
            return render_template('FizzBuzz_template.html', item= "Fizz")
        elif i % 5 == 0:
            return render_template('FizzBuzz_template.html', item= "Buzz")
        else:
            return render_template('FizzBuzz_template.html', name = i)