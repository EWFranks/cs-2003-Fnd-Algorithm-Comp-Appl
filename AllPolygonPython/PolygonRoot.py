from Polygon import Polygon

mypolygon=Polygon()

print ("the four vertices of the 'hard-coded' mypolygon...")
print(mypolygon)

print ("translating mypolygon by (2.0,3.0)...")
mypolygon.translate(2.0,3.0)
print(mypolygon)

print ("translating mypolygon by (-2.0,-3.0)...")
mypolygon.translate(-2.0,-3.0)
print(mypolygon)

print ("scaling mypolygon by (0.5,0.5)...")
mypolygon.scale(0.5,0.5)
print(mypolygon)

print ("scaling mypolygon by (2.0,2.0)...")
mypolygon.scale(2.0,2.0)
print(mypolygon)

print ("rotating mypolygon by 60 degrees...)")
mypolygon.rotate(60)
print(mypolygon)

print ("rotating mypolygon by -60 degrees...")
mypolygon.rotate(-60)
print(mypolygon)

print("perimeter of mypolygon is ...")
print(mypolygon.perimeter())


