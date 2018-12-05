import tkinter as tk
from tkinter import *
import time
from tkinter import messagebox
 
'''
定义消息发送函数：
1、在<消息列表分区>的文本控件中实时添加时间；
2、获取<发送消息分区>的文本内容，添加到列表分区的文本中；
3、将<发送消息分区>的文本内容清空。
'''
def chat(username,s):
    def msgsend():
        send_data = txt_msgsend.get('0.0', END)
        send_msg = username + ' ' + send_data
        msg1 = username + " " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
        txt_msglist.insert(END, msg1, 'green')  # 添加时间
        txt_msglist.insert(END, send_data+'\n')  # 获取发送消息，添加文本到消息列表
        txt_msgsend.delete('0.0', END)  # 清空发送消息

        s.send(send_msg.encode())
        recv_data = s.recv(1024).decode() + '\n\n'
        msg2 = '小优 ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        txt_msglist.insert(END, msg2, 'green')
        txt_msglist.insert(END, recv_data)
        txt_msglist.see(END)
        txt_msglist.mark_set('insert', 0.0)

        '''定义取消发送 消息 函数'''
    def cancel():
        txt_msgsend.delete('0.0',END) #取消发送消息，即清空发送消息


        '''绑定键UP'''
    def msgsendEvent(event):
        if event.keysym == 'Up':
            msgsend()
    
   
    def quit():
        if messagebox.askokcancel(title='返回主菜单', message='确定退出聊天窗口，并返回主菜单吗？'):
            window.destroy()
            from menu1 import menu
            menu(username,s)


    window= Tk()
    window.title('聊天窗口')
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
    window.protocol("WM_DELETE_WINDOW", on_closing)
                

    '''创建分区'''

    f_msglist = Frame(height = 200,width = 340) #创建<消息列表分区 >  
    f_msgsend = Frame(height = 400,width = 340) #创建<发送消息分区 >
    f_floor = Frame(height =480,width = 300)   #创建<按钮分区>
    f_right = Frame(height = 400,width = 300)   #创建<图片分区>



    '''创建控件'''
    txt_msglist = Text(f_msglist) #消息列表分区中创建文本控件
    txt_msglist.tag_config('green',foreground = 'blue') #消息列表分区中创建标签
    txt_msgsend = Text(f_msgsend) #发送消息分区中创建文本控件
    txt_msgsend.bind('<KeyPress-Up>',msgsendEvent) #发送消息分区中，绑定‘UP’键与消息发送。
    '''txt_right = Text(f_right) #图片显示分区创建文本控件'''
    button_send = Button(f_floor,text = 'Send',command = msgsend) #按钮分区中创建按钮并绑定发送消息函数
    button_cancel = Button(f_floor,text = 'Cancel',command = cancel) #分区中创建取消按钮并绑定取消函数
    button_quit = Button(f_floor,text = 'Quit',command = quit)

    photo = PhotoImage(file = r'./Frame.png')
    label = Label(f_right,image = photo) #右侧分区中添加标签（绑定图片）
    label.image = photo

    '''分区布局'''
    f_msglist.grid(row = 0,column = 0 ) #消息列表分区
    f_msgsend.grid(row = 1,column = 0)  #发送消息分区
    f_floor.grid(row = 2,column = 0)    #按钮分区
    f_right.grid(row = 0,column = 1,rowspan = 3) #图片显示分区
    txt_msglist.grid()  #消息列表文本控件加载
    txt_msgsend.grid()  #消息发送文本控件加载
    button_send.grid(row = 0,column = 0,sticky = W)   #发送按钮控件加载
    button_cancel.grid(row = 0,column = 1,sticky = W) #取消按钮控件加载
    button_quit.grid(row = 0, column = 2 ,sticky = W)


    label.grid() #右侧分区加载标签控件

    txt_msglist.insert(END, 'Hello，我是机器人小优，终于等到你和我聊天啦！\n我可以陪聊哦,我知道天气、菜单、新闻资讯、快递、股票、列车等信息呢！\n\n', 'red')
    
    window.mainloop()

if __name__=="__main__":
    chat("Tom", None)