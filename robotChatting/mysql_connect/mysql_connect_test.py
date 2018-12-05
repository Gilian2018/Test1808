from mysqlpython import Mysqlpython
db=Mysqlpython("test")

sele="select keywords,count(keywords) from keywords group by keywords  order by count(keywords) desc "
s=db.all(sele)
print(s)
