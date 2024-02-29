import tkinter as tk

def soma ():
    n1 = float(input_entry.get())
    n2 =  float(input_entry2.get())
    resultado1 =  n1 + n2
    resultado['text'] = f' Resultado da soma =  {resultado1}'

def subtração ():
    n1 = float(input_entry.get())
    n2 =  float(input_entry2.get())
    resultado1 =  n1 - n2
    resultado['text'] = f' Resultado da soma =  {resultado1}'

def multiplicação ():
    n1 = float(input_entry.get())
    n2 =  float(input_entry2.get())
    resultado1 =  n1 * n2
    resultado['text'] = f' Resultado da soma =  {resultado1}'

def divisão ():
    n1 = float(input_entry.get())
    n2 =  float(input_entry2.get())
    resultado1 =  n1 / n2
    resultado['text'] = f' Resultado da soma =  {resultado1}'


root = tk.Tk()
root.geometry('500x500')

label1 =  tk.Label(root, text='Calculadora do Jaca', fg='black', bg='skyblue', font='Arial', width='50')
label1.pack()

label_n1 = tk.Label(root, text = 'Digite o número 1')
label_n1.pack()
input_entry =  tk.Entry(root, width=10)
input_entry.pack(padx=50, pady=10)

label_n1 = tk.Label(root, text = 'Digite o número 2')
label_n1.pack()
input_entry2 =  tk.Entry(root, width=10)
input_entry2.pack(padx=0, pady=10)


btn = tk.Button(root, text='Soma', fg='white', bg='skyblue', width= 12, height=2, command=soma)
btn.pack(pady=20)

btn = tk.Button(root, text='Subtração', fg='white', bg='skyblue', width= 12, height=2, command=subtração)
btn.pack(pady=20)

btn = tk.Button(root, text='Mutiplicação', fg='white', bg='skyblue', width= 12, height=2, command=multiplicação)
btn.pack(pady=20)

btn = tk.Button(root, text='Divisão', fg='white', bg='skyblue', width= 12, height=2, command=divisão)
btn.pack(pady=20)



resultado =  tk.Label(root, text= ' ', font='Arial', bg='skyblue', fg = 'black')
resultado.pack()


root.mainloop()