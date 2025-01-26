from math import sqrt

print("Dit is een eenvoudige rekenmachine.")
operation = input("Welke operatie wil je doen? (+, -, *, /, sqrt, **, !): ")

if operation in ["sqrt", "**"]:  #lijsten zijn handiger om mee te werken dan or' of and's
    basegetal = float(input("Wat is het basis getal?: "))
    if operation == "**":
        exponent = float(input("Tot welke verheffing moet het?: "))
elif operation == "!":
    basegetal = int(input("Wat is het basis getal?: "))

else:
    getal1 = float(input("Wat is het eerste getal?: "))
    getal2 = float(input("Wat is het tweede getal?: "))


def add(getal1, getal2):
    return getal1 + getal2

def subtract(getal1, getal2):
    return getal1 - getal2

def multiply(getal1, getal2):
    return getal1 * getal2

def divide(getal1, getal2):
    if getal2 != 0:
        return getal1 / getal2
    else:
        return "Kan niet delen door nul!"

def machtsverhouding(basegetal, exponent):
    return pow(basegetal, exponent)

def root(basegetal):
    return sqrt(basegetal)

def factorial(basegetal):
    if basegetal == 0 or basegetal == 1:
        return 1
    mult = 1
    for i in range(1, basegetal + 1):
        mult *= i
    return mult

match operation:
    case "+":
        print("Het antwoord is", add(getal1, getal2))
    case "-":
        print("Het antwoord is", subtract(getal1, getal2))
    case "*":
        print("Het antwoord is", multiply(getal1, getal2))
    case "/":
        print("Het antwoord is", divide(getal1, getal2))
    case "!":
        print("Het antwoord is", factorial(basegetal))
    case "sqrt":
        print("Het antwoord is", root(basegetal))
    case "**":
        print("Het antwoord is", machtsverhouding(basegetal, exponent))
    case default:
        print("Ongeldige operatie!")

