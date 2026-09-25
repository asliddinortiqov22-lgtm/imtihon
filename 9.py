import json

student = [
    {"ism": "Ali", "yosh": 20, "baho": 85},
    {"ism": "Vali", "yosh": 22, "baho": 90},
    {"ism": "Hasan", "yosh": 21, "baho": 75},
    {"ism": "Husan", "yosh": 20, "baho": 88},
    {"ism": "Dilorom", "yosh": 23, "baho": 95},
] 


max = 0
min = 0
for x in student("baho"):
    if x > max:
        max = x
    elif x<min:
        min = x
        


print(max, min)                
        





