monstersizes = [3, 4, 6, 7, 10]
w_unit = 0

class Monster:
  def __init__(self,size,dist_ground,dist_tower):
    # index # declared internal
    
    self.size = size # size index
    self.dist_ground = dist_ground
    self.dist_tower = dist_tower
    self.width = int(w_unit * monstersizes[sizeind])   
    # troligtvis
    # monster_w = int(w_unit * monstersizes[sizeind])

    # eventuella
    onRow = -1 #på vilken rad bor den (om minus ingen)
    # grounded = False

  def __str__(self):
    return f"{self.size}({self.dist_ground})({self.dist_tower})"

  def myfunc(s):
    print("Im the monster ")

if __name__ == "__main__":
    p1 = Monster(36,200,100)
    p1.myfunc()