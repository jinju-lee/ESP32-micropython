import utime
from machine import UART

u1_tx = UART(1, 400000)
u1_rx = UART(1, 400000)
u2_tx = UART(2, 400000)
u2_rx = UART(2, 400000)

u1_tx.init(400000, bits=8, parity=None, stop=1, tx=10)
u1_rx.init(400000, bits=8, parity=None, stop=1, rx=9)
u2_tx.init(400000, bits=8, parity=None, stop=1, tx=23)
u2_rx.init(400000, bits=8, parity=None, stop=1, rx=22)


while True:
	u1_tx.write("u1 HELLO WORLD!!")
	print(u2_rx.read())
	#u2_tx.write("u2 HELLO WORLD!!")
	print(u1_rx.read())
	utime.sleep(1)
	
