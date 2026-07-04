nrOfBlocksDroped = 0
nrOfBlocks = 0
DropRate = 6000
gameOver = False
paused = False

def pauseSwap():
    global paused
    if not paused:
        paused = True
    else:
        paused = False