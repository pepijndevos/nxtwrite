from turtle import *
from baseprinter import BasePrinter

class DummyPrinter(BasePrinter):

    def _to(self, x, y):
        goto(x, y * -1)

    def up(self):
        up()

    def down(self):
        down()
