import tkinter as tk

def on_press(event):
    # Change the circle’s fill to green
    canvas.itemconfig(indicator, fill='green')

def on_release(event):
    # Change it back to gray
    canvas.itemconfig(indicator, fill='gray')

# Set up main window
root = tk.Tk()
root.title("Hold-to-Light Indicator")

# Create a canvas with a circle indicator
canvas = tk.Canvas(root, width=60, height=60, highlightthickness=0)
indicator = canvas.create_oval(10, 10, 50, 50, fill='gray', outline='')
canvas.pack(padx=20, pady=10)

# Create a button and bind press/release events
btn = tk.Button(root, text="Hold to Light")
btn.pack(pady=(0,20))
btn.bind('<ButtonPress-1>', on_press)
btn.bind('<ButtonRelease-1>', on_release)

root.mainloop()