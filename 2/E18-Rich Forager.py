# Use "if" and "else if" to handle any situation.
# Put it all together to defeat enemies and pick up coins!
# Make sure you bought great armor from the item shop! 400 health recommended.

loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()

    if enemy:
        # What happens when I find an enemy?
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
        
    elif item:
        # What happens when I find an item?
        p = item.pos
        self.moveXY(p.x, p.y)
    elif flag:
        # What happens when I find a flag?
        p = flag.pos
        self.moveXY(p.x, p.y)
        self.pickUpFlag(flag)
