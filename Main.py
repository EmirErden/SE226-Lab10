import tkinter as tk

root = tk.Tk()
root.title("File Read")
root.geometry("400x400")

def read_text():
    text.delete(1.0, tk.END)
    file = open("C:\\Users\\Emir\\OneDrive\\Masaüstü\\Marvel.txt", "r")
    data = file.read()
    text.insert(tk.END, data)
    file.close()


def calculateFreqs():
    text.delete(1.0, tk.END)
    file = open("C:\\Users\\Emir\\OneDrive\\Masaüstü\\Marvel.txt", "r")
    data = file.read()
    data = data.split()
    list = []

    for i in data:
        list.append(i)

    for i in list:
        x = str("Frequency of " + str(i) + ":" + str(list.count(i)) + "\n")
        text.insert(tk.END, x)


text = tk.Text(root, width=65, height=15)
text.pack(pady=20)

button1 = tk.Button(text = "READ", command = read_text)
button1.pack()

button2 = tk.Button(text = "CALCULATE", command = calculateFreqs)
button2.pack()

root.mainloop()
