import tkinter as tk
import Frame
import Mood_index
from tkinter import messagebox
import Rank
def menu(username,s):

    window = tk.Tk()    
    window.title('welcome')
    # w = window.winfo_screenwidth()
    # h = window.winfo_screenheight()
    window.geometry('640x480')
    # top.tk.eval('package require Tix') 
    # def resize(ev=None):
    #     label.config(font='Helvetica -%d bold' % scale.get())
    # scale = Scale(top, from_=10, to=40,orient=HORIZONTAL, command=resize)  #缩放比例尺
    # scale.set(12)  #初始值
    # scale.pack(fill=X, expand=1) 



    # welcome image
    canvas = tk.Canvas(window, height=480, width=640)
    image_file = tk.PhotoImage(file=r'./menu1.png')
    image = canvas.create_image(0,0,anchor='nw', image=image_file)
    canvas.pack(side='top')


    def find():
        window.destroy()
        Frame.chat(username,s)#私人助手进入聊天室
    


    def b():
        window.destroy()  #热搜榜
        Rank.rank(username,s)
           
    

    def c():   #心情指数
        window.destroy()
        Mood_index.mood(username,s)

    
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
    window.protocol("WM_DELETE_WINDOW", on_closing)


    btn_find= tk.Button(window, height=2, width=10, bg='tomato',text='私人助手', command=find)
    btn_find.place(x=140, y=420)
    btn_b = tk.Button(window, height=2, width=10,bg='yellow', text='热搜榜', command=b)
    btn_b.place(x=280, y=420)

    btn_c = tk.Button(window, height=2, width=10, bg='darkseagreen',text='心情指数', command=c)
    btn_c.place(x=420, y=420)
    window.mainloop()


if __name__=="__main__":
    menu(username,s)

