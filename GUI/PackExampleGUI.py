import tkinter as tk

root = tk.Tk()

# A wide label that fills horizontally
lbl = tk.Label(root, text="I'm at the top, filling X", bg="lightblue")
lbl.pack(side="top", fill="x", padx=5, pady=5)

# A button on the left that fills vertically
btn_left = tk.Button(root, text="Left")
btn_left.pack(side="left", fill="y", ipadx=10, ipady=10)

# A button on the right that just sits there
btn_right = tk.Button(root, text="Right")
btn_right.pack(side="right", padx=20, pady=20)

root.mainloop()