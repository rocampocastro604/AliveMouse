from pynput.mouse import Button, Controller
import random
import time

def mouseketool():
	mouse=Controller()
	i = random.randint(100, 1000)
	j = random.randint(100, 1000)
	mouse.position =(500, 500)
	mouse.move(i,j)
	print(time.ctime())

def main():
	while True:
		mouseketool()
		time.sleep(2)


main()
