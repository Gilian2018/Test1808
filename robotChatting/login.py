import tkinter as tk
from tkinter import messagebox
from mysql_connect.mysqlpython import Mysqlpython
import menu1

def do_login(s):
    # 设置窗口居中
    def window_info():
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenwidth()
        x = (ws / 2)-200
        y = (hs / 2)-200
        # print("%d,%d" % (ws,hs))
        return x,y
    #设置登录窗口属性
    window = tk.Tk()
    window.title("欢迎使用智能之星Robot")
    a,b = window_info()
    window.geometry("450x300+%d+%d"%(a,b))

    #登录界面信息
    tk.Label(window,text = "智能之星Robot",font = ("宋体",32)).place(x=80,y=50)
    tk.Label(window,text = "账号：").place(x=120,y=150)
    tk.Label(window,text = "密码：").place(x=120,y=190)

    #显示输入框
    var_usr_name = tk.StringVar()

    #显示默认账号
    var_usr_name.set('aid1808')
    entry_usr_name = tk.Entry(window,textvariable = var_usr_name)
    entry_usr_name.place(x = 190,y = 150)
    var_usr_pwd = tk.StringVar()
    #设置输入密码后显示*
    entry_usr_pwd = tk.Entry(window,textvariable = var_usr_pwd,show = "*")
    entry_usr_pwd.place(x = 190,y = 190)

    #登录函数
    def usr_login():
        #获取账号和密码
        username = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        #获取存储的账户信息
        db=Mysqlpython("test")
        sel="select name,password from user where name='%s' or password='%s'"%(str(username),str(usr_pwd))
        r=db.all(sel)
        # print(r)

        pwd = r[0][1]

        if usr_pwd != pwd:
            tk.messagebox.showerror(message="对不起输入错误请重试！")

        elif usr_pwd == pwd:
            tk.messagebox.showinfo(title="Welcome to 智能之星-Robot",
                                message=username+"：欢迎来到智能之星"  )
            window.destroy()
            menu1.menu(username, s)#登录之后运行的函数或者窗口

    def usr_sign_up():
        # def sign_up():
        # window.destroy()
        #创建top窗口作为注册窗口
        window_sign_up = tk.Toplevel(window)
        window_sign_up.geometry('350x200')
        window_sign_up.title('注册')
        
        new_name = tk.StringVar()
        # new_name.set('aid1808')
        tk.Label(window_sign_up,text = "账号：").place(x=80,y = 10)
        entry_new_name = tk.Entry(window_sign_up,textvariable = new_name)
        entry_new_name.place(x = 150,y = 10)
        
        new_pwd = tk.StringVar()
        tk.Label(window_sign_up,text = "密码：").place(x=80,y=50)
        entry_usr_pwd = tk.Entry(window_sign_up,textvariable = new_pwd,show = "*")
        entry_usr_pwd.place(x = 150,y = 50)
        
        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up,text = "确认密码：").place(x = 80,y = 90)
        entry_usr_pwd_again = tk.Entry(window_sign_up,textvariable = new_pwd_confirm,show = "*")
        entry_usr_pwd_again.place(x = 150,y = 90)
              


        
        # 保存新注册用户信息至数据库
        def regist_to_mysql():
            np = new_pwd.get()
            npc = new_pwd_confirm.get()
            nn = new_name.get()

            db=Mysqlpython("test")
            sel="select name from user where name='%s'"%str(nn)
            s=db.all(sel)
            # print(s)

            if s:
                tk.messagebox.showerror('对不起，此账号已存在！')
            elif np != npc:
                tk.messagebox.showerror('对不起',"两次密码输入不一致!")
            else:
                # try:
                db=Mysqlpython("test")
                ins="insert into user (name,password) values ('%s','%s')"%(str(nn),str(np))
                db.zhixing(ins)
                tk.messagebox.showinfo("Welcome","您已注册成功")

                window.destroy()
                menu1.menu(nn, s)    #注册之后运行的函数或者窗口


        btn_again_sign_up = tk.Button(window_sign_up,text = "注册",command = regist_to_mysql)
        btn_again_sign_up.place(x=180,y = 130)




    #登录注册按钮
    btn_login = tk.Button(window,text = '登录',command = usr_login)
    btn_login.place(x = 190,y = 230)
    btn_sign_up = tk.Button(window,text = "注册",command = usr_sign_up)
    btn_sign_up.place(x = 280,y = 230)

    window.mainloop()

if __name__=="__main__":
    do_login(s)










































