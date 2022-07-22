# Code by @AmirMotefaker

# Temperature Conversion

import tkinter as tk

window = tk.Tk()

lbl_fahrenheit = tk.Label(
    master=window,
    text='Fahrenheit: ',
)
ent_fahrenheit = tk.Entry(
    master=window,
    width=50,
)
btn_calc = tk.Button(
    master=window,
    text='Calc',
)

lbl_fahrenheit.grid(row=0, column=0, padx=10, pady=10)
ent_fahrenheit.grid(row=0, column=1)
btn_calc.grid(row=0, column=2, padx=10, pady=10)

lbl_celsius = tk.Label(
    master=window,
    text='Celsius:',
)
lbl_result = tk.Label(
    master=window,
    text='Enter your number...'
)

lbl_celsius.grid(row=1, column=0, pady=(10, 20))
lbl_result.grid(row=1, column=1, pady=(10, 20))

window.mainloop()