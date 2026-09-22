import tkinter as tk
from calculator.calculator import calculateResult


def createWindow():

    window = tk.Tk()
    window.title("Calculator")
    window.geometry("300x450")
    window.configure(bg="#202020")

    numberField = tk.Entry(
        window,
        width=20,
        font=("Consolas", 20, "bold"),
        bg="#3D3D3D",
        fg="#F8FAFC",
    )
    numberField.pack(pady=20, padx=20, ipady=10)

    def calculate():
        calculation = numberField.get()
        result = calculateResult(calculation)

        # Delete calculation from text field
        numberField.delete(0, tk.END)

        # insert result into text field
        numberField.insert(0, result)

    def insertInput(input):
        numberField.insert(tk.END, input)

    def clearNumbers():
        numberField.delete(0, tk.END)

    def deleteNumber():

        if numberField.get():
            numberField.delete(len(numberField.get()) - 1, tk.END)

    def calculatePercent():
        insertInput("/100")
        calculate()

    # Number buttons

    buttonFrame = tk.Frame(window, bg="#202020")
    buttonFrame.pack()

    ButtonNum0 = tk.Button(
        buttonFrame,
        text="0",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("0"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum0.grid(
        row=4,
        column=1,
        pady=2,
        padx=2,
    )

    ButtonNum1 = tk.Button(
        buttonFrame,
        text="1",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("1"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum1.grid(
        row=1,
        column=0,
        pady=2,
        padx=2,
    )

    ButtonNum2 = tk.Button(
        buttonFrame,
        text="2",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("2"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum2.grid(
        row=1,
        column=1,
        pady=2,
        padx=2,
    )

    ButtonNum3 = tk.Button(
        buttonFrame,
        text="3",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("3"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum3.grid(
        row=1,
        column=2,
        pady=2,
        padx=2,
    )

    ButtonNum4 = tk.Button(
        buttonFrame,
        text="4",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("4"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum4.grid(
        row=2,
        column=0,
        pady=2,
        padx=2,
    )

    ButtonNum5 = tk.Button(
        buttonFrame,
        text="5",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("5"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum5.grid(
        row=2,
        column=1,
        pady=2,
        padx=2,
    )

    ButtonNum6 = tk.Button(
        buttonFrame,
        text="6",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("6"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum6.grid(
        row=2,
        column=2,
        pady=2,
        padx=2,
    )

    ButtonNum7 = tk.Button(
        buttonFrame,
        text="7",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("7"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum7.grid(
        row=3,
        column=0,
        pady=2,
        padx=2,
    )

    ButtonNum8 = tk.Button(
        buttonFrame,
        text="8",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("8"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum8.grid(
        row=3,
        column=1,
        pady=2,
        padx=2,
    )

    ButtonNum9 = tk.Button(
        buttonFrame,
        text="9",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("9"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    ButtonNum9.grid(
        row=3,
        column=2,
        pady=2,
        padx=2,
    )

    # other Buttons

    buttonPlus = tk.Button(
        buttonFrame,
        text="+",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("+"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    buttonPlus.grid(
        row=3,
        column=3,
        pady=2,
        padx=2,
    )

    buttonMinus = tk.Button(
        buttonFrame,
        text="-",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("-"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    buttonMinus.grid(
        row=2,
        column=3,
        pady=2,
        padx=2,
    )

    buttonMultiply = tk.Button(
        buttonFrame,
        text="X",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("*"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    buttonMultiply.grid(
        row=1,
        column=3,
        pady=2,
        padx=2,
    )

    buttonDivide = tk.Button(
        buttonFrame,
        text="÷",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("/"),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    buttonDivide.grid(
        row=0,
        column=3,
        pady=2,
        padx=2,
    )

    buttonDelete = tk.Button(
        buttonFrame,
        text="⌫",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: deleteNumber(),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    buttonDelete.grid(
        row=0,
        column=2,
        pady=2,
        padx=2,
    )

    buttonComma = tk.Button(
        buttonFrame,
        text=".",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: insertInput("."),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    buttonComma.grid(row=4, column=2, pady=2, padx=2)

    buttonPercent = tk.Button(
        buttonFrame,
        text="%",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: calculatePercent(),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    buttonPercent.grid(row=0, column=0, pady=2, padx=2)

    buttonClear = tk.Button(
        buttonFrame,
        text="C",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: clearNumbers(),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    buttonClear.grid(row=0, column=1, pady=2, padx=2)

    calculateButton = tk.Button(
        buttonFrame,
        text="=",
        width=5,
        height=2,
        font=("Consolas", 15),
        command=lambda: calculate(),
        bg="#323232",
        fg="#F2F2F2",
        activebackground="#3D3D3D",
        activeforeground="#FFFFFF",
        relief="flat",
        borderwidth=0
    )
    calculateButton.grid(row=4, column=3, pady=2, padx=2)

    return window
