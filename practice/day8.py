def greet(name):
    print(f"Hello {name}!")
    print(f"{name} you rock!")
    print("Bye.")

greet("Anne")

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"{name}, how's the weather in {location}!")
    print(f"{location} fucking sucks")

greet_with("Anne", "London")
greet_with(location = "Colombia", name = "Jorge")