marks = {
    "Ap" : 100,
    "Kisan" : 42,
     "Meet": 22,
     0 : "Hp"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ap":90, "Meeta": 45})
print(marks)
print(marks.get("Kisan"))