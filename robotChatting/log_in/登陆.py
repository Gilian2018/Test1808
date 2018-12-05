import tkinter as tk
from mysql_connect.mysqlpython import Mysqlpython

window = tk.Tk()
window.title('welcome')
window.geometry('640x480')

# welcome image
canvas = tk.Canvas(window, height=480, width=640)
image_file = tk.PhotoImage(file='./we.png')
image = canvas.create_image(0,0,anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name:', font=('Arial', 15)).place(x=125, y=300)
tk.Label(window, text='Password:', font=('Arial', 15)).place(x=125, y=350)

var_usr_name = tk.StringVar()
var_usr_passwd = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=275, y=300)
entry_usr_passwd = tk.Entry(window, textvariable=var_usr_passwd)
entry_usr_passwd.place(x=275, y=350)


# begin 增加登录和注册 by 20181120
#登录函数
def usr_login():
    #获取账号和密码
    username = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    #获取存储的账户信息
    db=Mysqlpython("test")
    sel="select name,password from user where name='%s' or password='%s'"%(str(username),str(usr_pwd))
    r=db.all(sel)
    print(r)

    if not r:
        tk.messagebox.showerror(message="对不起输入错误请重试！")

    if r:
        pwd = r[0][1]
        if usr_pwd == pwd:
            tk.messagebox.showinfo(title="Welcome to 智能之星-Robot",
                                message=username+"：欢迎来到智能之星"  )
            window.destroy()
            menu1.menu(username, s)#登录之后运行的函数或者窗口

def user_sign_up():
    # def sign_to_Pyhon():
    np = new_pwd.get()
    npc = new_pwd_confirm.get()
    nn = new_name.get()

    db=Mysqlpython("test")
    sel="select name from user where name='%s'"%str(nn)
    s=db.all(sel)
    print(s)

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
        # except:
        #     tk.messagebox.showerror("注册失败")
        #     window_sign_up.destroy()
# end 增加登录和注册 by 20181120

# login and sign up button
def usr_login():
    pass
    # usr_name = var_usr_name.get()
    # usr_passwdd = var_usr_passwdd.get()
    # usr_login()
	



def usr_sign_up():
    window.destroy()
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('注册')
    window_sign_up.geometry('350x200')
    # user_sign_up()


btn_login = tk.Button(window, height=2, width=10, text='登陆', command=usr_login)
btn_login.place(x=175, y=420)
btn_sign_up = tk.Button(window, height=2, width=10, text='注册', command=usr_sign_up)
btn_sign_up.place(x=350, y=420)

window.mainloop()
