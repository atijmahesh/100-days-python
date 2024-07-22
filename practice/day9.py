prog_dict = {
    "Bug": "an error",
    "Function": "a func",
    "Loop": "a repeat",
}
#retrieving items
print(prog_dict["Loop"])

#adding new + edit
prog_dict["Key"] = "Value"
prog_dict["Bug"] = "an insect"
print(prog_dict)

#looping thru
for key in prog_dict:
    print(key)
    print(prog_dict[key])

caps = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Nice", "Monaco"], "total visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Munich", "Hamburg"], "total_visits": 5}
}

travel_log2 = {
    {
    "country": "France",
     "cities_visited": ["Paris", "Nice", "Monaco"], 
     "total visits": 12
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Munich", "Hamburg"], 
    "total_visits": 5
    }
}
