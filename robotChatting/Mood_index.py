import tkinter as tk
from tkinter import *
import sys
import Mood_index_data

def mood(username,s):

    # begin 当用户段连接时，刷新热搜榜和心情指数by_zoujiayan_20181104
    # keywords.main()
    Mood_index_data.main()
    # end 当用户端连接时，刷新热搜榜和心情指数 by_zoujiayan_20181104

    window = tk.Tk()
    window.title('心情分析')
    window.geometry('640x480')
    canvas = tk.Canvas(window, height=480, width=640)
    image_file = tk.PhotoImage(file='./mood.png')
    image = canvas.create_image(0,0,anchor='nw', image=image_file)
    canvas.pack(side='top')
    # Button(window,text='实时更新').pack()


   
    def find():
        if messagebox.askokcancel(title='退出', message='确定退出登录吗？'):
            window.destroy()
            sys.exit("tuchuxiton")
    
    def b():   #返回menu1
        window.destroy()
        import menu1
        menu1.menu(username,s)
    

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
    window.protocol("WM_DELETE_WINDOW", on_closing)

    
    btn_find= tk.Button(window, height=2, width=10,bg='red', text='退出系统', command=find)
    btn_find.place(x=175, y=420)
    btn_b = tk.Button(window, height=2, width=10,bg='red', text='返回主菜单', command=b)
    btn_b.place(x=400, y=420)


    window.mainloop()


if __name__=="__main__":
    mood(username,s)

