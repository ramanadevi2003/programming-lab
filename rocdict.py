students = {
    "Anu": [85,90,78],
    "Gowri": [72,88,91],
    "Vishnu":[95,880,85]
}
for name,mark in students.items():
    total = sum(mark)
    average = sum(mark) / len(mark)
    print(f"Student:{name}")
    print(f"Marks:{mark}")
    print(f"Total marks:{total}")
    print(f"Avarage Marks: {average:.2f}")
    print("." * 20)