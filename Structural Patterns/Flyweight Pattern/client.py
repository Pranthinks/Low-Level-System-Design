from factory import BulletFactory

class Bullet:
    def __init__(self, name: str, pos: int, image: str):
        self.name = name          # extrinsic
        self.pos = pos            # extrinsic
        self.flyweight = BulletFactory.get_flyweight(image)

    def draw(self):
        self.flyweight.render(self.name, self.pos)
bullets = []

for i in range(3):
    bullets.append(Bullet("Red", i, "Saaho.png"))

for i in range(3):
    bullets.append(Bullet("Green", i, "Green.png"))

for b in bullets:
    b.draw()
