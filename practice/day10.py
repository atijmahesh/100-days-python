#funcs with outputs

def format_name(first, last):
    return first.title() + " " + last.title()

print(format_name(input("First name: "), input("Last name: ")));