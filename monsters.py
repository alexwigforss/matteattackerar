from problemz import Problemz as p
monstersizes = [3, 4, 6, 7, 10]
INDEX = 0
class Monster:
  def __init__(self,dist_ground,dist_tower,height):
    w_unit = 15 # Multiplikator för förstoring
    global INDEX
    self.index = INDEX # declared internal
    INDEX = INDEX + 1 
    self.newborn = True
    self.out_of_index = False
    self.dist_ground = dist_ground  # Avstånd till mark Mby Obsolete
    self.dist_tower = dist_tower    # Avstånd till torn Mby Obsolete
    self.numberis = p.getRandomMulti(p)   # Akillesnummret
    self.size = getSizeInd(self.numberis)   # Breddens multiplikationskoficient
    self.width = int(w_unit*monstersizes[self.size])  # Blockets bredd i pixel
    self.height = int(height) # Blockets bredd i pixel
    self.onRow = -1 #på vilken rad bor den (om minus ingen)
    self.falling = True
    #monsterBornMsg = "Index: {0} Dist_G: {1} Dist_T: {2} Nr: {3} Size: {4} Width: {5} height: {6} Row: {7}."
    #print(monsterBornMsg.format(self.index, self.dist_ground, self.dist_tower, self.numberis, self.size, self.width,self.height, self.onRow))

  def __str__(self):
    return f"Index: {self.index} Dist_G: {self.dist_ground} Dist_T: {self.dist_tower} Nr: {self.numberis} Size: {self.size} Width: {self.width} Row: {self.onRow}."

  def setRow(self,row):
    self.onRow = row
    return self.onRow

  def updateRow(self,row):
    self.onRow += row
    return self.onRow

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

""" Mby
# TODO Searchforgap
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