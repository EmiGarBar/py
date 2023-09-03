from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text="Serie Fibonacci:  ")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
    label_flower['text'] = "La flor está completamente florecida"
    label_spiral["text"] = "Los espirales en la dirección derecha son " + str(first_no) + " y los espirales en la dirección izquierda son " + str(second_no) + "\n El total de espirales es " + str(sum)

btn = Button(root, text="Mostrar la serie Fibonacci", command=Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()