import math

print("Which side would you like to calculate")
print("Opposite / Adjacent / Hypotenuse")
print("1 / 2 / 3")
x = input("input: ")

if x == "1":
    H = float(input("Hypotenuse length: "))
    A = float(input("Adjacent length: "))
    print("Opposite length:", math.sqrt(H**2 - A**2))
if x == "2":
    H = float(input("hypotenuse Length: "))
    O = float(input("Adjacent Length: "))
    print("Opposite length:", math.sqrt(H**2 - O**2))
if x == "3":
    O = float(input("Opposite Length: "))
    A = float(input("Adjacent Length: "))
    print("Hypotenuse Length", math.sqrt(O**2 + A**2))
