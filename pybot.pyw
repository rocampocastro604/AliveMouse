from pynput.mouse import Button, Controller
import random
import time

def mouseketool():
	mouse=Controller()
	i = random.randint(100, 800)
	j = random.randint(100, 500)
	mouse.position =(i, j)
	#print(time.ctime())
	#print(x)
	#print(y)

def main():
	while True:
		mouseketool()
		time.sleep(2)


main()