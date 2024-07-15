import os 
import tkinter as tk


if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')



def change_text():
    label.config(text="Text Changed!")

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Project")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height)
print("###################################")
print(screen_width)
root.geometry("800x480")
# Create a label widget
label = tk.Label(root, text="Click the button to change this text!")
label.pack(pady=10)

# Create a button widget
button = tk.Button(root, text="Change Text", command=change_text)
button.pack()

# Run the Tkinter event loop
root.mainloop()