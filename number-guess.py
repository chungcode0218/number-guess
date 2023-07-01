#產生一個1~100的隨機整數(不用印出來)
#讓使用者重複輸入數字去猜
#猜錯要告訴她比答案大/小，猜對的話印出"你猜對了!"
import random
print('數字猜猜樂')
print('6次內猜中即獲勝!')
down = input('請先決定隨機數字範圍下限:')
up = input('請先決定隨機數字範圍上限:')
down = int(down)
up = int(up)
r = random.randint(down,up)
time = 1
while time <= 6:
	chance = 6-time
	R = input('請輸入您猜的數字:')
	R = int(R)
	if R == r:
		print('恭喜答對!將獲得獎品')
		break
	elif R >= r and R <= up:
		if chance == 0:
			print('Game Over，正確答案為', r)
			break
		else:
			print('答錯，比', R,'小，您剩下', chance, '次機會' )
	elif R <= r and R >= down:
		if chance == 0:
			print('Game Over，正確答案為', r)
			break
		else:
			print('答錯，比', R,'大，您剩下', chance, '次機會')
	else:
		print('您輸入的數字不在範圍內，請重新操作')
		break
	time = time + 1
