import tkinter as tk
from calculator.calculator import calculateResult

def createWindow():

    window = tk.Tk()
    window.title("Calculator")
    window.geometry("800x600")
    
    numberField = tk.Entry(
        window, 
        width=20,
        font=("Terminal", 20, "bold")
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
        
        
    # buttons
    
    buttonFrame = tk.Frame(window)
    buttonFrame.pack()
    
    ButtonNum1 = tk.Button(buttonFrame, text="1", width=5, height=2, font=("Terminal", 15), command=lambda: insertInput("1"))
    ButtonNum1.grid(row=1, column=0)
    
    ButtonNum2 = tk.Button(buttonFrame, text="2", width=5, height=2, font=("Terminal", 15), command=lambda: insertInput("2"))
    ButtonNum2.grid(row=1, column=1)
    
    ButtonNum3 = tk.Button(buttonFrame, text="3", width=5, height=2, font=("Terminal", 15), command=lambda: insertInput("3"))
    ButtonNum3.grid(row=1, column=2)
    
    ButtonNum4 = tk.Button(buttonFrame, text="4", width=5, height=2, font=("Terminal", 15), command=lambda: insertInput("4"))
    ButtonNum4.grid(row=2, column=0)
    
    ButtonNum5 = tk.Button(buttonFrame, text="5", width=5, height=2, font=("Terminal", 15), command=lambda: insertInput("5"))
    ButtonNum5.grid(row=2, column=1)
    
    ButtonNum6 = tk.Button(buttonFrame, text="6", width=5, height=2, font=("Terminal", 15), command=lambda: insertInput("6"))
    ButtonNum6.grid(row=2, column=2)
    
    
    
    calculateButton = tk.Button(
        window, 
        text="Calculate",
        width= 10,
        height= 2,
        font=("arial", 20, "bold"),
        command=lambda: calculate()
    )
    calculateButton.pack()



    return window