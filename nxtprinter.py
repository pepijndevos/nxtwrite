from baseprinter import BasePrinter
from nxt import locator, motor, motcont
from multiprocessing.pool import ThreadPool
from time import sleep

class NxtPrinter(BasePrinter):

    xscale = 10
    yscale = -20

    power = 50

    def __init__(self, brick, xmotor, ymotor, penmotor):
        self.brick = brick
        self.xmotor = xmotor
        self.ymotor = ymotor
        self.penmotor = penmotor

        mc = motcont.MotCont(brick)
        mc.start()
        self.motcont = mc
        
        self.calib()

        pool = ThreadPool()

        def submit(*moves):
            pool.map(self.turn, moves)

        self.move = submit
   
    def calib(self):
        m = motor.Motor(self.brick, self.penmotor)
        m.run(-60)
        sleep(1)
        m.idle()
	self.downtacho = m.get_tacho().tacho_count
        self.up()

    def turn(self, args):
        motor = args[0]
        steps = args[1]
        self.motcont.move_to(motor, self.power, steps)
        while(not self.motcont.is_ready(motor)):
            pass

    def up(self):
        self.turn([self.penmotor, 0])

    def down(self):
        self.turn([self.penmotor, self.downtacho])

    def _to(self, x, y):
        vertial = (self.ymotor, y)
        horizontal = (self.xmotor, x)
        self.move(vertial, horizontal)
