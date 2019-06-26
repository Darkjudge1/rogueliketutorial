class Entity:
    """
    A generic object used to represent players, entity, items, etc.
    """
def _init_ (self, x, y, char, color):
    self.x = x
    self.y = y
    # char is the player object
    self.char = char
    # color is the player object color.
    self.color = color

def move (self, dx, dy):
    #move the entity by a given amount
    self.x += dx
    self.y += dy

