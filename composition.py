class Door:
  color = 'white'

  def __init__(self, number, status):
    self.number = number
    self.status = status

  def open(self):
    return 'door open'


class SecurityDoor:
    locked = True

    def __init__(self, number, status):
        self.door = Door(number, status)

    def open(self):
        if self.locked:
            return 'closed door!'
        return self.door.open()
    # if attribute is not found in self it will look at door 
    def __getattr__(self, attr):
        return getattr(self.door, attr)




class Animal():
  def __init__(self, move_behavior):
    self.move_behavior = move_behavior
  # All animals feeds themselves in some way or another
  def feed(self):
    print("I' feed myself in a general way")
      
  # Supposing animals could move just in one way to simplify things
  def move(self):
    return self.move_behavior()
 	

class WalkBehavior():
  def walk(self):
    print("I'm walking")

class FlyBehavior():
  def fly(self):
    print("I'm flying")


class Dog(Animal):
  def __init__(self):
    super().__init__(WalkBehavior().walk)
	
class Bird(Animal):
  def __init__(self):
    super().__init__(FlyBehavior().fly)

  def feed(self):	
    print("I’m eating in an special way")




class Animal():
  def feed(self):
    print("I' feed myself in a general way")
	def fly(self):
    print("i can fly!")
  
class Dog(Animal):
	def fly(self):
    print("ups I can’t fly...") 	

class Bird(Animal):
	def feed():
		print("I’m eating in an special way")
