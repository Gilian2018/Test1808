import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from mysql_connect.mysqlpython import Mysqlpython

# 解决中文字乱码
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def main():
	# 连接数据库，获取数据
	db=Mysqlpython("test")
	sele="select keywords,count from keywords_count  where time=date(now()) and keywords is not NULL order by count "
	s=db.all(sele)
	label=[x[0] for x in s]
	keywords_count=[x[1] for x in s]
	idx = np.arange(len(keywords_count))
	color = cm.jet(np.array(keywords_count)/len(keywords_count))
	# 绘制直方图
	plt.barh(idx, keywords_count, color=color)
	plt.yticks(idx+0.4,label)
	plt.grid(axis='keywords_count')
	plt.xlabel('访问量')
	plt.ylabel('访问词')
	plt.title('热搜榜',fontsize='xx-large',fontweight='black')

	# 将图片保存至本地
	plt.savefig(r'rank.png')
	plt.show()

if __name__=="__main__":
	main()