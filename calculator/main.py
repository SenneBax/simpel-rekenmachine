import tkinter as tk
import math

calculation = ""

def addToCalculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, tk.END)
    text_result.insert(1.0, calculation)

def evaluate():
    global calculation
    try:
        # Als de berekening een faculteit bevat, verwerken we dat apart
        if '!' in calculation:
            parts = calculation.split('!')
            number = int(parts[0])  # Haal het getal voor de ! op
            result = math.factorial(number)  # Bereken de faculteit
            calculation = str(result)
        else:
            # Als er geen ! in de berekening zit, gebruik dan eval
            result = str(eval(calculation))  # str erbij voor veiligheidsredenen
        calculation = ""
        text_result.delete(1.0, tk.END)
        text_result.insert(1.0, result)
    except Exception as e:
        # Foutmelding met een beetje meer info over de fout
        clearField()
        text_result.insert(1.0, f"Error: {str(e)}")

def clearField():
    global calculation
    calculation = ""
    text_result.delete(1.0, tk.END)

root = tk.Tk()
root.title("Rekenmachine")

# Achtergrondkleur en algemene stijl van het venster
root.config(bg="#2E3B4E")

# Textresultaat instellen
text_result = tk.Text(root, height=2, width=20, font=("Helvetica", 32), bg="#1E2A37", fg="white", bd=5, relief="ridge", wrap="word")
text_result.grid(columnspan=5, padx=20, pady=20)

# Button stijl
button_style = {
    'width': 4,
    'height': 2,
    'font': ("Helvetica", 24),
    'bg': "#62978f",  # kleur van de buttons
    'fg': "white",
    'relief': "flat",
    'bd': 2,
    'activebackground': "#FF7043",  # Lichte oranje bij klikken
    'activeforeground': "white"
}

def create_button(text, row, column, command):
    return tk.Button(root, text=text, command=command, **button_style).grid(row=row, column=column, padx=10, pady=10)

# Knoppen
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
create_button("=", 6, 1, lambda: evaluate())
create_button("!", 6, 4, lambda: addToCalculation("!"))
create_button("Clear", 6, 2, lambda: clearField())

create_button("π", 6, 3, lambda: addToCalculation(str(math.pi)))

# Update de grootte van het venster automatisch op basis van de inhoud
root.update()

# Root window loop
root.mainloop()
