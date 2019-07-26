# 01Hangman
运用for循环创建扑克牌
suits = ["spades","hearts","diamonds","clubs"]    #扑克牌的花色
values = [None,None,"2","3","4","5","6","7","8","9","10","Jcak","Queen","King","Ace"]
#values列表前面加两个None，是为了让索引值和扑克牌点数对得上
cards=[]
for i in range(2,15):
  for j in range(4):
    cards.append(suits[j]+values[i])
