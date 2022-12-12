class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def speedUp(self, v):
        self.speed = self.speed + v
        return self.speed

    def speedDown(self, v):
        self.speed = self.speed - v
        return self.speed


c1 = Car('black', 50)
c2 = Car('red', 70)
print('Car c1 : color=%s, speed=%d ' % (c1.color, c1.speed))
print('Car c2 : color=%s, speed=%d ' % (c2.color, c2.speed))
c1.speedDown(10)
print('Car c1 : speed=%d' % c1.speed)
