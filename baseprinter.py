import string, operator

def listadd(*ls):
     return map(lambda *l: sum(l), *ls)

def listmul(*ls):
     return map(lambda *l: reduce(operator.mul,l), *ls)

def partition(l, n):
    return [l[i:i+n] for i in xrange(0, len(l), n)]

class BasePrinter(object):

    xscale = 3
    yscale = 5

    hspace = 2
    vspace = 2

    origin = (0, 0) # of character
    position = (0, 0) # relative to origin

    def __init__(self):
        self.up()

    def realpos(self, x=0, y=0):
        return listmul(
            listadd(self.origin, (x, y)),
            (self.xscale, self.yscale))

    def _to(self, x, y):
        raise NotImplementedError

    def to(self, x, y):
        self._to(*self.realpos(x, y))
        self.position = (x, y)

    def toandfro(self, x, y):
        p = self.position
        self.to(x, y)
        self.to(*p)

    def up(self, x, y):
        raise NotImplementedError

    def down(self, x, y):
        raise NotImplementedError

    def next(self):
        self.up()
        self.origin = listadd(self.origin, (10 + self.hspace, 0))
        position = (0, 0)

    def newline(self):
        self.up()
        self.origin = (0, self.origin[1] + 10 + self.vspace)
        position = (0, 0)

    def char(self, ch):
        getattr(self, ch)()
        self.next()

    def write(self, text, linewidth=80):
        for line in partition(text, linewidth):
            for ch in line:
                if ch in string.ascii_lowercase:
                    self.char(ch)
                else:
                    self.next()
            self.newline()
        
    #  0123456789
    # 0*   x     0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5  x    x  5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789
    def a(self):
        self.to(0, 9)
        self.down()
        self.to(2, 5)
        self.to(4, 0)
        self.to(7, 5)
        self.toandfro(2, 5)
        self.to(9, 9)

    #  0123456789
    # 0x     x   0
    # 1          1
    # 2         x2
    # 3          3
    # 4x     x   4
    # 5          5
    # 6          6
    # 7         x7
    # 8          8
    # 9x     x   9
    #  0123456789

    def b(self):
        self.to(0, 0)
        self.down()
        self.to(0, 9)
        self.to(6, 9)
        self.to(9, 7)
        self.to(6, 4)
        self.toandfro(0, 4)
        self.to(9, 2)
        self.to(6, 0)
        self.to(0, 0)

    #  0123456789
    # 0*  x     x0
    # 1          1
    # 2          2
    # 3x         3
    # 4          4
    # 5          5
    # 6x         6
    # 7          7
    # 8          8
    # 9   x     x9
    #  0123456789

    def c(self):
        self.to(9, 0)
        self.down()
        self.to(3, 0)
        self.to(0, 3)
        self.to(0, 6)
        self.to(3, 9)
        self.to(9, 9)

    #  0123456789
    # 0x    x    0
    # 1          1
    # 2          2
    # 3         x3
    # 4          4
    # 5          5
    # 6         x6
    # 7          7
    # 8          8
    # 9x    x    9
    #  0123456789

    def d(self):
        self.to(0, 0)
        self.down()
        self.to(0, 9)
        self.to(5, 9)
        self.to(9, 6)
        self.to(9, 3)
        self.to(5, 0)
        self.to(0, 0)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5x        x5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def e(self):
        self.to(0, 0)
        self.down()
        self.toandfro(9, 0)
        self.to(0, 5)
        self.toandfro(9, 5)
        self.to(0, 9)
        self.toandfro(9, 9)



    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5x        x5
    # 6          6
    # 7          7
    # 8          8
    # 9x         9
    #  0123456789

    def f(self):
        self.to(0, 0)
        self.down()
        self.toandfro(9, 0)
        self.to(0, 5)
        self.toandfro(9, 5)
        self.to(0, 9)

    #  0123456789
    # 0*    x   x0
    # 1          1
    # 2          2
    # 3x         3
    # 4          4
    # 5     x   x5
    # 6x         6
    # 7         x7
    # 8          8
    # 9     x    9
    #  0123456789

    def g(self):
        self.to(9, 0)
        self.down()
        self.to(5, 0)
        self.to(0, 3)
        self.to(0, 6)
        self.to(5, 9)
        self.to(9, 7)
        self.to(9, 5)
        self.to(5, 5)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5x        x5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def h(self):
        self.to(0, 0)
        self.down()
        self.to(0, 5)
        self.toandfro(0, 9)
        self.to(9, 5)
        self.toandfro(9, 9)
        self.toandfro(9, 0)

    #  0123456789
    # 0*  x x x  0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9   x x x  9
    #  0123456789

    def i(self):
        self.to(3, 0)
        self.down()
        self.to(5, 0)
        self.toandfro(7, 0)
        self.to(5, 9)
        self.toandfro(3, 9)
        self.toandfro(7, 9)

    #  0123456789
    # 0*   x    x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7  x      x7
    # 8          8
    # 9      x   9
    #  0123456789

    def j(self):
        self.to(4, 0)
        self.down()
        self.to(9, 0)
        self.to(9, 7)
        self.to(6, 9)
        self.to(2, 7)


    #  0123456789
    # 0x      x  0
    # 1          1
    # 2          2
    # 3          3
    # 4x         4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def k(self):
        self.to(0, 0)
        self.down()
        self.to(0, 4)
        self.toandfro(0, 9)
        self.toandfro(7, 0)
        self.toandfro(9, 9)

    #  0123456789
    # 0x         0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def l(self):
        self.to(0, 0)
        self.down()
        self.to(0, 9)
        self.to(9, 9)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9x   x    x9
    #  0123456789

    def m(self):
        self.to(0, 9)
        self.down()
        self.to(0, 0)
        self.to(4, 9)
        self.to(9, 0)
        self.to(9, 9)


    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def n(self):
        self.to(0, 9)
        self.down()
        self.to(0, 0)
        self.to(9, 9)
        self.to(9, 0)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def o(self):
        self.to(0, 0)
        self.down()
        self.to(0, 9)
        self.to(9, 9)
        self.to(9, 0)
        self.to(0, 0)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5x        x5
    # 6          6
    # 7          7
    # 8          8
    # 9x         9
    #  0123456789

    def p(self):
        self.to(0, 0)
        self.down()
        self.to(9, 0)
        self.to(9, 5)
        self.to(0, 5)
        self.toandfro(0, 0)
        self.to(0, 9)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5x        x5
    # 6          6
    # 7          7
    # 8          8
    # 9         x9
    #  0123456789

    def q(self):
        self.to(9, 0)
        self.down()
        self.to(0, 0)
        self.to(0, 5)
        self.to(9, 5)
        self.toandfro(9, 0)
        self.to(9, 9)

    #  0123456789
    # 0x    x    0
    # 1          1
    # 2         x2
    # 3          3
    # 4          4
    # 5x    x    5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def r(self):
        self.to(0, 9)
        self.down()
        self.to(0, 0)
        self.to(5, 0)
        self.to(9, 2)
        self.to(5, 5)
        self.toandfro(0, 5)
        self.to(9, 9)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5x        x5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def s(self):
        self.to(9, 0)
        self.down()
        self.to(0, 0)
        self.to(0, 5)
        self.to(9, 5)
        self.to(9, 9)
        self.to(0, 9)

    #  0123456789
    # 0x    x   x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9     x    9
    #  0123456789

    def t(self):
        self.to(0, 0)
        self.down()
        self.to(5, 0)
        self.toandfro(5, 9)
        self.to(9, 0)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def u(self):
        self.to(0, 0)
        self.down()
        self.to(0, 9)
        self.to(9, 9)
        self.to(9, 0)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9     x    9
    #  0123456789

    def v(self):
        self.to(0, 0)
        self.down()
        self.to(5, 9)
        self.to(9, 0)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5    x     5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def w(self):
        self.to(0, 0)
        self.down()
        self.to(0, 9)
        self.to(4, 5)
        self.to(9, 9)
        self.to(9, 0)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def x(self):
        self.to(0, 0)
        self.down()
        self.to(9, 9)
        self.up()
        self.to(9, 0)
        self.down()
        self.to(0, 9)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5    x     5
    # 6          6
    # 7          7
    # 8          8
    # 9x         9
    #  0123456789

    def y(self):
        self.to(9, 0)
        self.down()
        self.to(4, 5)
        self.toandfro(0, 0)
        self.to(0, 9)

    #  0123456789
    # 0x        x0
    # 1          1
    # 2          2
    # 3          3
    # 4          4
    # 5          5
    # 6          6
    # 7          7
    # 8          8
    # 9x        x9
    #  0123456789

    def z(self):
        self.to(0, 0)
        self.down()
        self.to(9, 0)
        self.to(0, 9)
        self.to(9, 9)
