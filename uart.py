import utime
from machine import UART

u1_tx = UART(1, 400000)
u2_rx = UART(2, 400000)

u1_tx.init(400000, bits=8, parity=None, stop=1, tx=10)
u2_rx.init(400000, bits=8, parity=None, stop=1, rx=16)

while True:
	u1_tx.write("u1_HELLO WORLD!!")
	print(u2_rx.read())
	utime.sleep(1)
	
