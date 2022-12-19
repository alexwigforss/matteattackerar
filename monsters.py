class Monster:
  def __init__(self,size,dist_ground,dist_tower):
    self.size = size
    self.dist_ground = dist_ground
    self.dist_tower = dist_tower
    grounded = False
    state = 0

  def __str__(self):
    return f"{self.size}({self.dist_ground})({self.dist_tower})"

  def myfunc(s):
    print("Im the monster ")

if __name__ == "__main__":
    p1 = Monster(36,200,100)
    p1.myfunc()