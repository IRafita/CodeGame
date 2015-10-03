# Put flags where you want to build traps.
# When you're not building traps, pick up coins!

#self.buildXY("fire-trap", 30, 45)
#self.buildXY("fire-trap", 30, 31)
#self.buildXY("fire-trap", 30, 16)

loop:
    flag = self.findFlag()
    if flag:
        # How do we get fx and fy from the flag's pos?
        # (Look below at how to get x and y from items.)
        flagPos = flag.pos
        fx = flagPos.x
        fy = flagPos.y
        self.buildXY("fire-trap", fx, fy)
        self.pickUpFlag(flag)
    else:
        item = self.findNearestItem()
        if item:
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            self.moveXY(itemX, itemY)
