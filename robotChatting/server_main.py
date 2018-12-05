from select import select
from socket import *
import sys
from server_chatting import auto_chatting
import re
from mysql_connect.mysqlpython import Mysqlpython

def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    HOST = '0.0.0.0'
    PORT = 8888
    ADDR = (HOST,PORT)
    s.bind(ADDR)
    s.listen(5)

    rlist = [s]
    wlist = []
    xlist = [s]

    while True:
        rs, ws, xs = select(rlist, wlist, xlist)
        try:
            for r in rs:
                if r is s:
                    c, addr = r.accept()
                    print("Connect from: ", addr)
                    rlist.append(c)
                else:
                    msg=r.recv(1024).decode()
                    if not msg:
                        rlist.remove(r)
                        r.close()
                        continue
                    username=re.match(r"\S+",msg).group() #说这句话的用户名
                    data=re.findall(r'\w+\s(.*?)$',msg)[0] #用户说的信息，字符串形式
                    print(username)
                    print(data)
                    # begin 将用户端发送的数据保存至数据库 by_zoujiayan_20181104
                    db=Mysqlpython("test") # 连接数据库
                    ins="insert into keywords(userid,keywords,time) values('%s','%s',now())"%(username,data)
                    db.zhixing(ins)
                    # end 将用户端发送的数据保存至数据库 by_zoujiayan_20181104

                    auto_chatting(r,data)
        except Exception as e:
            print(e)
            rlist.remove(r)
            r.close
            continue


        for x in xs:
            x.close()
            print("服务端异常")

if __name__=="__main__":
    main()