from Rectangle import Rectangle

myrectangle=Rectangle()

print ()
print ("the four vertices of the 'hard-coded' myrectangle are ...")
print(myrectangle)
print ("the manually computed length of myrectangle is ... 6")
print ("the manually computed width of myrectangle is ... 4")
print ()

print ("translating myrectangle by (2.0,3.0)...")
myrectangle.translate(2.0,3.0)
print(myrectangle)

print ("translating myrectangle by (-2.0,-3.0)...")
myrectangle.translate(-2.0,-3.0)
print(myrectangle)

print ("scaling myrectangle by (0.5,0.5)...")
myrectangle.scale(0.5,0.5)
print(myrectangle)

print ("scaling myrectangle by (2.0,2.0)...")
myrectangle.scale(2.0,2.0)
print(myrectangle)

print ("rotating myrectangle by 60 degrees...)")
myrectangle.rotate(60)
print(myrectangle)

print ("rotating myrectangle by -60 degrees...")
myrectangle.rotate(-60)
print(myrectangle)

print ("perimeter of myrectangle is ...")
print (myrectangle.perimeter())
