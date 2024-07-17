import random

a = random.randint(100, 200) #100 to 200 inclusive
print(a)

#between 0-0.99999
ranFloat = random.random()
print(ranFloat)

#randFloat between 0-4.999
print(ranFloat*5)

states = ["Deleware", "California", "Alaska"]
print(states[0])
print(states[-1])
print(states[-2])
states[0] = "Florida"
states.append("Hawaii")
states.extend(["North Carolina", "South Carolina"])
print(states)