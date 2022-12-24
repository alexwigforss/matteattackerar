import slumpfabrik

# TODO Bäst tror jag om monster importerar en modul som är rummet
#   som sköter hur dem rellaterar till varandra och canvas.

monstersizes = [3, 4, 6, 7, 10]
w_unit = 0

class Monster:
  def __init__(self,size,dist_ground,dist_tower):
    # index # declared internal
    
    self.size = size # size index
    self.dist_ground = dist_ground
    self.dist_tower = dist_tower
    self.width = int(w_unit * monstersizes[self.size])
    # troligtvis
    # monster_w = int(w_unit * monstersizes[sizeind])
    # eventuella
    onRow = -1 #på vilken rad bor den (om minus ingen)
    # grounded = False # kanske inte nödvändig

  def __str__(self):
    return f"{self.size}({self.dist_ground})({self.dist_tower})"

  def myfunc(s):
    print("Im the monster ")

if __name__ == "__main__":
    p1 = Monster(36,200,100)
    p1.myfunc()

# Beroende på talets storlek tilldela Typ
def getSizeInd(nr):
    if nr < 11:
        si = 0
    elif nr < 31:
        si = 1
    elif nr < 51:
        si = 2
    elif nr < 71:
        si = 3
    else:
        si = 4
    return si

def DropBlock():
    global rowFilled
    # TODO packa alla variabler här i en lista (eller tuple)
    # i objektet monster ist...
    #   dvs [numberis, sizeind, monster_w]
    numberis = slumpfabrik.getRand()
    sizeind = getSizeInd(numberis)
    monster_w = int(w_unit * monstersizes[sizeind])

    if rowFilled + monster_w > canvas_w:
        rowsFilled.append([[rowFilled],[True]])
        # print(rowsFilled)
        rowFilled = 0
        xpos = canvas_x
    else:
        xpos = canvas_x + rowFilled

    rowFilled = rowFilled + monster_w

    for r in range(0, 1):
        # TODO skapa en instans av monster här ist för rektangel.
        rect = pygame.Rect(xpos, -100, monster_w, gui.btn_h)
        monster_list.append(rect)
        num_list.append(numberis)
        if len(monster_list) > 30:
            # global g.gameOver
            g.gameOver = True
