from flask import Flask
import random

app = Flask(__name__)
chosen_number = random.randint(0, 9)
print(chosen_number)


@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWoyeTF4d2dvbzIxNjAwNnI4ZXppc3dueWxjampyMW1hazN6YzFhYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tU2mV8ALzJEdXAAwRo/giphy.gif" width="300">'


@app.route("/<int:number>")
def check_number(number):
    if number == chosen_number:
        return '<h1 style="color: green;">You found me!</h1>' \
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExenFxdHgwajJndnl4NTR5YWlwcWUwOHRwdTFmbnI0d280a3ljbnlraCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fDbzXb6Cv5L56/giphy.gif" width="300">'
    elif number > chosen_number:
        return '<h1 style="color: purple;">To high, try again!</h1>' \
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3VjamM4YTlnNG16NHNoaTkzNXg1NDY0Zm5oODFreGY4NWk1c2dsbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6BZaFXBVPBtok/giphy.gif" width="300">'
    else:
        return '<h1 style="color: red;">To low, try again!</h1>' \
               '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWNwbzV5N3I3cTkyMGN3ZDE1NGRlZ202MnJhMHR2N3hyNTY2Y2V1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LkuPxRS0F6gmc/giphy.gif" width="300">'


if __name__ == "__main__":
    app.run(debug=True)

