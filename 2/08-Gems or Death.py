# The commands below an if statement only run when the if's condition is true.
# Fix all the if-statements to beat the level.

# == means "is equal to".
if 1 + 1 + 2 == 3:  # ∆ Make this false.
    self.moveXY(5, 15)  # Move to the first mines.

if 2 + 2 == 4:  # ∆ Make this true.
	self.moveXY(15, 40)  # Move to the first gem.

# != means "is not equal to".
if 2 + 2 != 40:  # ∆ Make this true.
	self.moveXY(25, 15)  # Move to the second gem.
	
# < means "is less than".
if 2 + 2 < 30:  # ∆ Make this true.
    enemy = self.findNearestEnemy()
    self.attack(enemy)

if 20 < 4:  # ∆ Make this false.
	self.moveXY(40, 55)

if False:  # ∆ Make this false.
	self.moveXY(50, 10)

if True:  # ∆ Make this true.
	self.moveXY(55, 25)
