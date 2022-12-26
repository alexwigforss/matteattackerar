import slumpfabrik

# TODO Bäst tror jag om monster importerar en modul som är rummet
#   som sköter hur dem rellaterar till varandra och canvas.
#   eller om monster själv ska ha funktioner fast statiskt utanför klassen
monstersizes = [3, 4, 6, 7, 10]
w_unit = 0
INDEX = 0

class Monster:
  def __init__(self,dist_ground,dist_tower):
    global INDEX
    self.index = INDEX# declared internal
    INDEX += 1
    self.dist_ground = dist_ground  # Avstånd till mark
    self.dist_tower = dist_tower    # Avstånd till torn
    self.numberis = slumpfabrik.getRand()   # Akillesnummret
    self.size = getSizeInd(self.numberis)   # Breddens multiplikationskoficient
    self.width = int(w_unit * monstersizes[self.size])  # Blockets bredd i pixel
    # eventuella
    # onRow = -1 #på vilken rad bor den (om minus ingen)
    # grounded = False # kanske inte nödvändig
    monsterBornMsg = "Index: {0} Dist_G: {1} Dist_T: {2} Nr: {3} Size: {4} Width: {5}."
    print(monsterBornMsg.format(self.index, self.dist_ground, self.dist_tower, self.numberis, self.size, self.width))
    #print("index: " + str(self.index))

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

# TODO Falling
# TODO Searchforgap
# TODO Spaceing
"""
PSEUDO GAPSEARCH
För varje rad
    Om lucka finns
        Tills Match är över Gap
            I raden ovan om match finns & fri lejd
                Gå mot lucka
            Annars om lucka finns & ej fri lejd
                Klossarna under går mot lucka
        Sedan när Math är över Gap
            Fall ned i luckan
"""