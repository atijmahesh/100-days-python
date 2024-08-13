# from flask import Flask
# app = Flask(__name__)



# @app.route("/")
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!</h1>' \
#             '<p>paragraph</p>' \
#             '<img src ="https://letsenhance.io/static/73136da51c245e80edc6ccfe44888a99/1015f/MainBefore.jpg" width=200>'

# @app.route("/bye")
# @make_bold
# @make_emphasis
# @make underlined
# def bye():
#     return "<b>Bye!<b>"

# @app.route("/<name>/<int:number>")
# def greet(name, number):
#     return f"Hello {name}, you are number {number}!"



# if __name__ == "__main__":
#     app.run(debug=True)



# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     return nested_function

# inner_function = outer_function()
# inner_function()

# ## Simple Python Decorator Functions
# import time

# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         #Do something before
#         function()
#         function()
#         #Do something after
#     return wrapper_function

# @delay_decorator
# def say_hello():
#     print("Hello")

# #With the @ syntactic sugar
# @delay_decorator
# def say_bye():
#     print("Bye")

# #Without the @ syntactic sugar
# def say_greeting():
#     print("How are you?")
# decorated_function = delay_decorator(say_greeting)
# decorated_function()

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_auth_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_auth_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
    

new_user = User("Angela")
new_user.is_logged_in = True
create_blog_post(new_user)