from gpiozero import *
from time import sleep

globalCounter = 0

def printCounter():
	print(str(globalCounter))

motor1 = PWMOutputDevice(17, frequency = 1000)

try:
	while True:
		motor1.off()
		sleep(3)
		motor1.on()
		sleep(3)
		globalCounter = globalCounter +1
		# Number of pulses to test
		if(globalCounter == 10):
			printCounter()
			break
except KeyboardInterrupt:
	motor1.close()
	print("Exited through keyboard interupt")

motor1.close()

