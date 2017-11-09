import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text= "Choose math operation!")
greeting.pack()

operation = Tkinter.Entry(window)
operation.pack()



# prva spremenljivka
prva_text = Tkinter.Label(window, text="Choose x")
prva_text.pack()

# vpis prve spremenljivke
prva = Tkinter.Entry(window)
prva.pack()

# druga spremenljivka
druga_text = Tkinter.Label(window, text="Choose y")
druga_text.pack()

# vpis druge spremenljivke
druga = Tkinter.Entry(window)
druga.pack()


def calculate():
    if (operation.get()) == "+" :
       result_text = int(prva.get()) + int(druga.get())

    elif(operation.get()) == "-" :
       result_text = int(prva.get()) - int(druga.get())

    elif (operation.get()) == "*":
        result_text = int(prva.get()) * int(druga.get())

    elif (operation.get()) == "/":
        result_text = int(prva.get()) * int(druga.get())

    else:
        result_text = "Error"

    tkMessageBox.showinfo("Result", result_text)



submit = Tkinter.Button(window, text="Submit", command=calculate)  # check_guess, not check_guess()
submit.pack()
window.mainloop()











