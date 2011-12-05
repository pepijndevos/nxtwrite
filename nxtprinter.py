from baseprinter import BasePrinter
from nxt import locator, motor
from multiprocessing.pool import ThreadPool
from time import sleep

class NxtPrinter(BasePrinter):

    xscale = 10
    yscale = -40

    power = 20

    def __init__(self, xmotor, ymotor, penmotor):
        self.xmotor = xmotor
        self.ymotor = ymotor
        self.penmotor = penmotor

        pool = ThreadPool()

        def submit(*moves):
            pool.map(self.turn, moves)

        self.move = submit
    
    def turn(self, args):
        motor = args[0]
        steps = args[1]
        if steps != 0:
            # make steps positive, put the sign on power
            power = self.power * cmp(steps, 0)
            motor.turn(power, abs(steps))

    def up(self):
        self.penmotor.run(60)
        sleep(0.5)
        self.penmotor.brake()


    def down(self):
        self.penmotor.run(-60)
        sleep(0.5)
        self.penmotor.brake()

    def _to(self, x, y):
        xtacho = self.xmotor.get_tacho().tacho_count
        ytacho = self.ymotor.get_tacho().tacho_count
        vertial = (self.ymotor, y - ytacho)
        horizontal = (self.xmotor, x - xtacho)
        self.move(vertial, horizontal)
