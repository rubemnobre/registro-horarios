import tkinter as tk
import datetime
import os

filename = 'log.txt'

class App:
    def __init__(self):
        self.window = tk.Tk(className=' Registro de Horário')
        self.window.geometry("300x100")
        self.label1 = tk.Label(text="Descrição")
        self.label2 = tk.Label(text="00:00:00")
        self.entry1 = tk.Entry()
        self.button1 = tk.Button(text='Start', command=self.start_handler)
        self.label1.pack()
        self.entry1.pack()
        self.button1.pack()
        self.label2.pack()
        self.started = False
        self.window.mainloop()

    def start_handler(self):
        if not self.started:
            self.start_time = datetime.datetime.now()
            self.window.after(1000, self.update_clock)
            self.button1.configure(text='End')
            self.started = True
        else:
            self.end_time = datetime.datetime.now()
            self.button1.configure(text='Start')
            self.started = False
            log = '%s;%s;%s;%s\n' % (self.entry1.get(), str(self.start_time)[:10], str(self.start_time)[11:19], str(self.end_time)[11:19])
            print(log)
            if os.path.exists(filename):
                arq = open(filename, 'ab')
                arq.write(log.encode('utf-8'))
            else:
                arq = open(filename, 'wb')
                arq.write(log.encode('utf-8'))

    def update_clock(self):
        if self.started:
            newstr = str(datetime.datetime.now() - self.start_time)
            self.label2.configure(text=newstr[:9])
            self.window.after(1, self.update_clock)

app = App()