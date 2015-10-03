# Patrol the village entrances.
# If you find an enemy, attack it.
loop:
    self.moveXY(35, 34)
    leftEnemy = self.findNearestEnemy()
    if leftEnemy:
        self.attack(leftEnemy)
        self.attack(leftEnemy)
    # Now move to the right entrance.
    # Use "if" to attack if there is an enemy.
    self.moveXY(60, 34)
    leftEnemy = self.findNearestEnemy()
    if leftEnemy:
        self.attack(leftEnemy)
        self.attack(leftEnemy)

