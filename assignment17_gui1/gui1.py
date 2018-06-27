from tkinter import  *

root = Tk()
#place window of 550x350 at (50,50)
root.geometry("550x350+100+100")


# Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
print("__"*10,"question1","__"*20)
my_text = Label(root, text='Hello, world!')
my_text.pack()

exit_button = Button(root, text='Exit Program', command=root.destroy)
exit_button.pack()

#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
print("__"*10,"question2","__"*20)

def something():
    print("\n\nJust had to write something according to question2")  #to print on console

print_button = Button(root, text='Q2 button 1 for console', command=something)
print_button.pack()


def something2():    #wite on gui window
    lbl = Label(root, text="Had to write somrthing on gui window")
    lbl.pack()


print_button2= Button(root, text="Q2. button 2 for gui", command=something2)
print_button2.pack()
root.mainloop()
