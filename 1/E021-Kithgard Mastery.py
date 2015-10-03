# Reach the end of the maze using move commands.
# Count how many gems you pick up, and then say the current count when near a fireball trap to disable it.
# The raven at the start will give you a password. Say the password near a door to open it.
# Kill ogres when you get near them.
# You can use a loop to repeat all of the instructions as needed.
# If you beat this level, you can skip to the Forest World!
loop:
    self.moveRight()
    self.moveUp()
    self.moveUp()
    a = self.findNearestEnemy()
    self.attack(a)
    self.attack(a)
    self.moveLeft()
    self.moveUp()
    self.moveUp()
    self.moveRight()
    self.moveRight()
    self.moveUp()
    self.moveDown()
    self.moveRight()
    self.moveDown()
    self.moveDown()
    self.moveDown()
    self.moveDown()
    self.say("Sesame")
