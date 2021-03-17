
def point(self, x, y):
    self._x = x
    self._y = y


def getPosX(self):
    return self._x

def setPosX(self, x):
    self._x = x

def getPosY(self):
    return self._y

def setPosY(self, y):
    self._y = y
    
def toString(self):
    return "(" + self.getPosX() + ", " + self.getPosY() + ")"