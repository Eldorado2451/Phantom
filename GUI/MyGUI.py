"""
This is a program written using the tutorial https://www.youtube.com/watch?v=ibf5cx221hk&t=11s&ab_channel=NeuralNine
"""

import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("MyGUI")

label = tk.Label(root, text="Hello World", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)

button = tk.Button(root, text="Click me!", font=('Arial', 18))
button.pack(padx=10, pady=10)

root.mainloop()
