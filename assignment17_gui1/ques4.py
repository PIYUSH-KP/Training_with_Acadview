# entry_widget.py
from tkinter import Tk, Entry, Button, INSERT
root4 = Tk()
#place window of 550x350 at (50,50)
root4.geometry("550x350+100+100")

# Create single line text entry box
entry = Entry(root4)
entry.pack()


entry.insert(INSERT, "input:")

# Print the input in entry widget console
def print_input():
    print(entry.get())

# Button that will print the contents of the entry
button = Button(root4, text='Print input', command=print_input)
button.pack()


exit_button = Button(root4, text='Exit Program', command=root4.destroy)
exit_button.pack()

root4.mainloop()
