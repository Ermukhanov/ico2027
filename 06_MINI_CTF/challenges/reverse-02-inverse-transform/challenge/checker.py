# Программа сравнивает преобразованные символы со списком.
expected = [133, 127, 131, 87, 73, 100, 90, 99, 115, 74, 102, 89, 115, 98, 99, 99, 78, 81]
def transform(text):
    return [((ord(c) ^ 0x35) + 9) & 0xff for c in text]
if transform(input("token: ")) == expected:
    print("accepted")
else:
    print("no")
