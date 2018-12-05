from socket import *
import menu1
import login

def main():
    s=socket()
    HOST = '127.0.0.1'
    PORT = 8888
    ADDR = (HOST, PORT)
    s.connect(ADDR)
    #进入登录注册界面程序
    login.do_login(s)

    # username='Tom'#待赵健返回username,这只是个假设，假设已经登录成功
    # menu1.menu(username,s) #登录成功后调用该选择菜单函数

if __name__=="__main__":
    main()
