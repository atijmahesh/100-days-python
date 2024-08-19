from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

n = randint(0, 9)

@app.route("/<int:guess>")
def display(guess):
    if guess < n:
        return '<h1 style="color:red">Too low, try again</h1>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnlzenRvZ3o4ZmR5YWQ4ZmIzNTh4c2FrMjdsNzJzM3cwZ3hkeWhwdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif">'
    elif guess > n:
        return '<h1 style="color:blue">Too high, try again</h1>' \
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTRsNHltZzd2dWp5dzd3c2xwaW5pd294NWwycjAzbjAzbXd2NGFleCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wHB67Zkr63UP7RWJsj/giphy.gif">'
    else:
        return '<h1 style="color:blue">Your guess was correct!</h1>' \
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmZjZXFycXBlNG50dDRrMGs5NjkwOWZxeTJjNWJjbng3aWI5c3ducCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26tknCqiJrBQG6bxC/giphy.gif">'
    
    

if __name__ == "__main__":
    app.run(debug=True)