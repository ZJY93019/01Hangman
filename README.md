# 01Hangman
运用for循环创建扑克牌

suits = ["spades","hearts","diamonds","clubs"]    #扑克牌的花色

values = [None,None,"2","3","4","5","6","7","8","9","10","Jcak","Queen","King","Ace"]

#values列表前面加两个None，是为了让索引值和扑克牌点数对得上

cards=[]

for i in range(2,15):

  for j in range(4):
    
    cards.append(suits[j]+values[i])

单号创造
import re

#利用正则表达式提取出符合字符串

nums = []

for i in range(100000000):
	
  result = re.match(r'([0,1,2,5,6,8,9]*)', str(i))
	
  num = result.group()
	
  nums.append(num)

#将字符串清洗为常数

changshu = []

for i in nums:
	
  if len(i) > 0:
		
    _ = int(i)
		
    changshu.append(_)

changshu= set(changshu)

#print(changshu)

#将不符合的数字补长

numstr = []

for i in changshu:
	
  if len(str(i)) < 8:
		
    k = 8-len(str(i))
		
    i = str(0)*k + str(i)
		
    numstr.append(i)
	
  else:
		
    numstr.append(i)

#print(numstr)	

for i in numstr:
	
  print(i)

#print(numstr)
