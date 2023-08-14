import tkinter as tk
import ttkbootstrap as ttk


def convert():
       mile_input=entryInt.get()
       km_output=mile_input*1.6093
       output_string.set(km_output)


 #window
window = ttk.Window(themename="superhero")
window.title('demo')
window.geometry('600x400')
#title
title_lable=ttk.Label(master=window,text='Miles To kilometers',font='colibri 24 bold')
title_lable.pack()
#input filed
input_frame=ttk.Frame(master=window)
entryInt=tk.IntVar()
entry=ttk.Entry(master=input_frame,textvariable=entryInt)
btn=ttk.Button(master=input_frame,text='Convert',command=convert)
entry.pack(side='left',padx=10)
btn.pack(side='left')
input_frame.pack(pady=10)
#output
output_string=tk.StringVar()
output=ttk.Label(master=window,
                 text='Output',
                 font='colibri 24',
                 textvariable=output_string)
output.pack(pady=5)


#run
window.mainloop()