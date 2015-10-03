self.moveRight()

# You should recognize this from the last level.
enemy1 = self.findNearestEnemy()
# Now attack enemy1.
self.attack(enemy1)

self.moveRight()
self.attack(self.findNearestEnemy())
self.moveRight()

