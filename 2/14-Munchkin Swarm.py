# If the ogres rush at you, cleave them!
# If they stay 10 meters away, attack the "Chest".

loop:
    enemy = self.findNearestEnemy()
    distance = self.distanceTo(enemy.pos)
    if distance < 10:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.shield()
    else:
        self.attack("Chest")
