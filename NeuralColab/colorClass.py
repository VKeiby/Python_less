class Color:
    red = 0
    green = 0
    blue = 0

    def __init__(self, r, g, b,):
        self.red = r
        self.green = g
        self.blue = b

    def toHex(self):
        return '#%02x%02x%02x' % (red, green, blue)
class ColorAlpha(Color):
    alpha = 1

    def __init__(self, r, g, b, a):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a


gray = ColorAlpha(80,54,34,.5)
red = Color(255,0,0)
