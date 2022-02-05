from tkinter import *

def miles_to_kilometer():
    miles = miles_input.get()
    km = round(float(miles) * 1.609)
    value_label.config(text=f"{str(km)}")

window = Tk()
window.title('Mile to Kilometer Converter')
window.config(padx=20, pady=20, height=500, width=300)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row= 0)

equal_label = Label(text='is equal to')
equal_label.grid(column=0, row=1)

value_label = Label(text='0')
value_label.grid(column=1, row=1)

km_label = Label(text='km')
km_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=miles_to_kilometer)
calculate_button.grid(column=1, row=3)


window.mainloop()