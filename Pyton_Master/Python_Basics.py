# Basic Syntax
# 1. Comments - comment are line that are ignored by python interperter

# single line and """ multi line """

# 2. Variables and Data Types
# Variables - used to store data in containertype based on value
# Data Type - Type data Primary Data type = int ,flat ,boolen, str - Container DataType = list ,tuples ,dictonery ,sets, 

lst = [1,3,5,7] # Mutable(Changable) and Unordered

tup = (1,2,3,4,5) # immutable and Ordered

Dict = {
    'key': "value",
    'key1':"value1"
}

st = {20,30,10} # unordered and unique

# 3. Operators

for i in range(100):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
