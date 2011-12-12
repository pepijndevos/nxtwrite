from nxt import locator, motor
import nxtprinter
b = locator.find_one_brick()
p = nxtprinter.NxtPrinter(b, motor.PORT_B, motor.PORT_A, motor.PORT_C)
p.write(raw_input("print: "), 15)
