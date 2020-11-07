import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Make a Graph')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)


label2 = tk.Label(root, text='Give me a URL or FILE PATH')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)





def getSquareRoot ():
    
    root.update()
    label3 = tk.Label(root, text='PROCESSING')
    label3.config(font=('helvetica', 15))
    canvas1.create_window(200, 250, window=label3)
    root.update()
    x1 = entry1.get()
    df = pd.read_csv(x1)
    df = df.sort_values('Timestamp')
    fig = px.line(df, x = 'Timestamp', y = 'Value(DEC)', color='Name', title='CANBus Data Values', render_mode="webgl")
    fig.show()
    root.quit()
    

button1 = tk.Button(text='Get a Graph', command=getSquareRoot, bg='blue', fg='black', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)
root.update()
root.mainloop()
