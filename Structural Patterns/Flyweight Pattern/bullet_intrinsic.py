# bullet_intrinsic.py
class Bullet_type:
    def __init__(self, image):
        self.image = image
    
    # accept extrinsic state
    def render(self, name: str, pos: int):
        print(f"Bullet '{name}' at position {pos} using image '{self.image}'")
