import tkinter as tk
from tkinter import *
import sys
from tkinter import messagebox
import keywords

def rank(username,s):

    # begin 当用户段连接时，刷新热搜榜和心情指数by_zoujiayan_20181104
    keywords.main()
    # mood_data.Mood_index.main()
    # end 当用户端连接时，刷新热搜榜和心情指数 by_zoujiayan_20181104

    window = tk.Tk()
    window.title('热搜榜')
    window.geometry('640x480')
    canvas = tk.Canvas(window, height=480, width=640)
    # image_file = tk.PhotoImage(file='./rank_data/rank.png')
    # 此处暂时为绝对路径
    image_file = tk.PhotoImage(file=r'./rank.png')

    image = canvas.create_image(0,0,anchor='nw', image=image_file)
    canvas.pack(side='top')
    # Button(window,text='实时更新').pack()



    def rank_a():
        if messagebox.askokcancel(title='退出', message='确定退出登录吗？'):
            window.destroy()
            sys.exit("tuchuxiton")
            window.destroy()
            import menu1
            menu1.menu(username,s)
            
           

    def rank_b():
        window.destroy()
        import menu1
        menu1.menu(username,s)
        
          
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
    window.protocol("WM_DELETE_WINDOW", on_closing)
   
      


    btn_rank_a= tk.Button(window, height=1, width=10,bg='green', text='退出系统', command=rank_a)
    btn_rank_a.place(x=175, y=450)
    btn_rank_b= tk.Button(window, height=1, width=10,bg='green', text='返回主菜单', command=rank_b)
    btn_rank_b.place(x=400, y=450)


    window.mainloop()
if __name__=="__main__":
    rank(username,s)
