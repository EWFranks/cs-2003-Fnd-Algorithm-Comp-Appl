file = open("../Lab3/Project1.txt", "r")

lines = file.readlines()

with open("../Lab3/Project1.txt", "r") as file:
    row = file.readline()
    array = row.split()  # ["1","3","8","-5"]

   # while row == '':
      #  if array[0] == 'P':
         #   print("polygon", array[1])
      #  elif array[0] == 'r':
        #    print("rectangle", array[1])
      #  else:
    print(array)
    print(int(array[0]), int(array[1]))


    row = file.readline()
