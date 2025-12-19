from bullet_intrinsic import Bullet_type
class BulletFactory:
    _flyweights = {}

    @classmethod
    def get_flyweight(cls, image: str) -> Bullet_type:
        if image not in cls._flyweights:
            cls._flyweights[image] = Bullet_type(image)
            print(f"[Factory] Created new flyweight for image: {image}")
        return cls._flyweights[image]
