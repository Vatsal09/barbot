from gpiozero import *
from signal import pause

globalCounter = 0

def printCounter():
	print(str(globalCounter))

motor1 = PWMOutputDevice(17)

while True:
	motor1.on()
	sleep(1)
	globalCounter = globalCounter +1
	motor1.off()
	sleep(1)
	# Number of pulses to test
	if(globalCounter == 50):
		printCounter()
		break

motor1.close()
pause()
