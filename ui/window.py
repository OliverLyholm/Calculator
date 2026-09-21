import tkinter as tk


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

    return window