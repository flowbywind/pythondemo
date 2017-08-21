
class Bird(object):
    have_feather=True
    way_of_reproduction='egg'
    def move(self,dx,dy):
        position=[0,0]
        position[0]=position[0]+dx
        position[1]=position[1]+dy
        return position

class Chicken(Bird):
    way_of_move='walk'
    possible_in_KFC=True

class Swan(Bird):
    way_of_move='fly'
    possible_in_KFC=False

chicken=Chicken()
print(chicken.have_feather)
print(chicken.move(5,5))
print(type(chicken))
print(type(Bird))