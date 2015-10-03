# Patrol the village entrances.
# Build a "fire-trap" when you see an ogre.
# Don't blow up any peasants!

loop:
    self.moveXY(43, 50)
    topEnemy = self.findNearestEnemy()
    if topEnemy:
        self.buildXY('fire-trap', 43, 50)
        
    self.moveXY(25, 34)
    leftEnemy = self.findNearestEnemy()
    if leftEnemy:
        self.buildXY("fire-trap", 25, 35)
    
    self.moveXY(43, 21)
    leftEnemy = self.findNearestEnemy()
    if leftEnemy:
        self.buildXY("fire-trap", 43, 20)

