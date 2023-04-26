class Queen:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
 
    def set_position(self, a, b):
        self.a = a
        self.b = b
 
    def char(self):
        return 'Q'
 
    def get_color(self):
        return self.c
 
    def can_move(self, a, b):
        if not (0 <= a < 8 and 0 <= b < 8):
            return False
        if abs(a - self.a) == abs(b - self.b):
            return True
        if self.a != a and self.b != b:
            return False
        return True
