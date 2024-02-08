def rat(movie):
    return movie["imdb"]>5.5

mysal = {
    "name": "Usual Suspects", 
    "imdb": 5.0,
    "category": "Thriller"
}

result = rat(mysal)
print(result) 