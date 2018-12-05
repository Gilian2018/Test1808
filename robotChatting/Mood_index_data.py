from snownlp import SnowNLP
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
from mysql_connect.mysqlpython import Mysqlpython

# 解决中文字乱码
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

def main():
	# 连接数据库，获取数据
	db=Mysqlpython("test")
	sele="select * from keywords"
	s=db.all(sele)
	data=[x[2] for x in s]
	data2='，'.join(data)

	# 情感分析
	s = SnowNLP(data2)
	n=0    #问题个数统计
	mood_index=0 #代表每个问题的心情指数
	for sentence in s.sentences:
		n+=1
		mood_index+=float(SnowNLP(sentence).sentiments)

	index_number=mood_index/n  #根据用户今天问的所有问题计算平均心情指数
	# index_number = round(index_number, 4)
	# print(index_number)



	# 当心情指数大于0.5时，为积极
	if index_number>=0.5:
		lena = mpimg.imread('./mood_images/positive.jpg')  # 读取和代码处于同一目录下的 图片
	else:
		lena = mpimg.imread('./mood_images/negative.jpg')  # 读取和代码处于同一目录下的 图片

	plt.imshow(lena)
	plt.xticks([])
	 # 显示图片
	plt.axis('off') # 不显示坐标轴
	# plt.title('您今天的心情积极指数为：{}%'.format(round(index_number,4)*100),fontsize='xx-large',fontweight='black')
	plt.title("您今天的心情积极指数为:%.2f%%"%(index_number*100),fontsize='xx-large',fontweight='black')

	# 将图片保存至本地
	plt.savefig(r'mood.png')
	plt.show()

if __name__=="__main__":
	main()