from baseprinter import BasePrinter
from nxt import locator, motor
from multiprocessing.pool import ThreadPool
from time import sleep

class NxtPrinter(BasePrinter):

    xscale = 10
    yscale = -20

    power = 20

    def __init__(self, xmotor, ymotor, penmotor):
        self.xmotor = xmotor
        self.ymotor = ymotor
        self.penmotor = penmotor
        
        self.calib()

        pool = ThreadPool()

        def submit(*moves):
            pool.map(self.turn, moves)

        self.move = submit
   
    def calib(self):
        self.penmotor.run(-60)
        sleep(1)
        self.penmotor.idle()
	self.downtacho = self.penmotor.get_tacho().tacho_count
        self.up()

    def turn(self, args):
        motor = args[0]
        steps = args[1]
        if steps != 0:
            # make steps positive, put the sign on power
            power = self.power * cmp(steps, 0)
            motor.turn(power, abs(steps))

    def up(self):
        steps = 0 - self.penmotor.get_tacho().tacho_count
        self.turn([self.penmotor, steps])

    def down(self):
        steps = self.downtacho - self.penmotor.get_tacho().tacho_count
        self.turn([self.penmotor, steps])

    def _to(self, x, y):
        xtacho = self.xmotor.get_tacho().tacho_count
        ytacho = self.ymotor.get_tacho().tacho_count
        vertial = (self.ymotor, y - ytacho)
        horizontal = (self.xmotor, x - xtacho)
        self.move(vertial, horizontal)
