import tkinter as tk
import requests
import json

def sumar():
    cantidad1 = float(entry1.get())
    cantidad2 = float(entry2.get())
    response = requests.post("http://localhost:5000/sumar", json={"cantidad1": cantidad1, "cantidad2": cantidad2})
    result = response.json()
    if "resultado" in result:
        result_label.config(text=f"Resultado: {result['resultado']}")
    else:
        result_label.config(text=f"Error: {result['error']}")

window = tk.Tk()
window.title("Sumar")

entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

sumar_button = tk.Button(window, text="Sumar", command=sumar)
sumar_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()