from nxt import locator, motor
import nxtprinter
b = locator.find_one_brick()
ym = motor.Motor(b, motor.PORT_B)
xm = motor.Motor(b, motor.PORT_A)
pm = motor.Motor(b, motor.PORT_C)
p = nxtprinter.NxtPrinter(xm, ym, pm)
p.write("hallo wereld", 3)
