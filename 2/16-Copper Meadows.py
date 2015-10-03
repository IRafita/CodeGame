# Collect all the coins in each meadow.
# Use flags to move between meadows.
# Press Submit when you are ready to place flags.
loli = 0
loop:
    flag = self.findFlag()
    if flag:
        # pass is a placeholder, it has no effect.
        # Pick up the flag.
        self.pickUpFlag(flag)
        self.moveXY(15, 27)
        
    else:
        # Automatically move to the nearest item you see.
        item = self.findNearestItem()
        if item:
            position = item.pos
            x = position.x
            y = position.y
            self.moveXY(x, y)
        else:
            if loli == 0:
                self.moveXY(15, 27)
            else if loli == 1:
                self.moveXY(54, 26)
            else if loli == 2:
                self.moveXY(94, 52)
            else if loli == 3:
                self.moveXY(89, 76)
            loli += 1

