# Use a loop to both move and attack.
loop:
    self.moveRight()
    self.moveUp()
    self.attack(self.findNearestEnemy())
    self.attack(self.findNearestEnemy())
    self.moveRight()
    self.moveDown()
    self.moveDown()
    self.moveUp()
