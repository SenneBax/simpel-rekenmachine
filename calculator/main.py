import tkinter as tk
import math
import cmath

calculation = ""


def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)


def evaluate():
    global calculation
    try:
        # controleer op vectoriaal
        if '!' in calculation:
            number_str = calculation[:-1]  # nummer voor de '!' opnemen
            number = int(number_str)  # omzetten naar een integer
            result = math.factorial(number)
            calculation = str(result)


        #trigonometrische functies

        elif 'cos' in calculation or 'sin' in calculation or 'tan' in calculation:
            if 'cos' in calculation:
                parts = calculation.split('cos')
                number = float(parts[1])  # nummer na cos
                result = cmath.cos(number)
                calculation = str(result)
            elif 'sin' in calculation:
                parts = calculation.split('sin')
                number = float(parts[1])  # nummer na sin
                result = cmath.sin(number)
                calculation = str(result)
            elif 'tan' in calculation:
                parts = calculation.split('tan')
                number = float(parts[1])  # nummer na tan
                result = cmath.tan(number)
                calculation = str(result)

        # Handle 'e' and 'π'
        elif 'e' in calculation:
            calculation = str(math.e)  #  'e' vervangen met math.e
            result = str(eval(calculation))

        elif 'π' in calculation:
            calculation = str(math.pi)  # 'π' vervangen met math.pi
            result = str(eval(calculation))

        else:
            # gebruik eval voor de simppele berekeningen
            result = str(eval(calculation))  # Safe eval
        calculation = ""
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, result)
    except Exception as error:
        # Handle any error gracefully
        clearField()
        text_result.insert(1.0, f"Error: {str(error)}")


def clearField():
    global calculation
    calculation = ""
    text_result.delete(1.0, tk.END)


root = tk.Tk()
root.title("Rekenmachine")

# Set background and general styling
root.config(bg="#2E3B4E")

# Text result configuration
text_result = tk.Text(root, height=2, width=20, font=("Helvetica", 32), bg="#1E2A37", fg="white", bd=5, relief="ridge",
                      wrap="word")
text_result.grid(columnspan=5, padx=20, pady=20)

# Button style configuration
button_style = {
    'width': 4,
    'height': 2,
    'font': ("Helvetica", 24),
    'bg': "#62978f",
    'fg': "white",
    'relief': "flat",
    'bd': 2,
    'activebackground': "#FF7043",
    'activeforeground': "white"
}


def create_button(text, row, column, command):
    return tk.Button(root, text=text, command=command, **button_style).grid(row=row, column=column, padx=10, pady=10)


# Buttons
create_button("1", 2, 1, lambda: addToCalculation("1"))
create_button("2", 2, 2, lambda: addToCalculation("2"))
create_button("3", 2, 3, lambda: addToCalculation("3"))
create_button("4", 3, 1, lambda: addToCalculation("4"))
create_button("5", 3, 2, lambda: addToCalculation("5"))
create_button("6", 3, 3, lambda: addToCalculation("6"))
create_button("7", 4, 1, lambda: addToCalculation("7"))
create_button("8", 4, 2, lambda: addToCalculation("8"))
create_button("9", 4, 3, lambda: addToCalculation("9"))
create_button("0", 5, 2, lambda: addToCalculation("0"))
create_button("(", 5, 1, lambda: addToCalculation("("))
create_button(")", 5, 3, lambda: addToCalculation(")"))
create_button("+", 2, 4, lambda: addToCalculation("+"))
create_button("*", 3, 4, lambda: addToCalculation("*"))
create_button("/", 4, 4, lambda: addToCalculation("/"))
create_button("-", 5, 4, lambda: addToCalculation("-"))
create_button("π", 6, 4, lambda: addToCalculation(str(math.pi)))
create_button("Cos", 6, 1, lambda: addToCalculation("cos"))
create_button("Sin", 6, 2, lambda: addToCalculation("sin"))
create_button("Tan", 6, 3, lambda: addToCalculation("tan"))
create_button("=", 7, 1, lambda: evaluate())
create_button("!", 7, 4, lambda: addToCalculation("!"))
create_button("e", 7, 3, lambda: addToCalculation("e"))
create_button("Clear", 7, 2, lambda: clearField())

# Auto-update de grootte van de window om zich aan te passen aen de hoeveelhijd/grootte van de buttons
root.update()

# de main loop
root.mainloop()
