import random
import string
from collections import Counter
a= random.randint(1,100)

def random_string_generator(str_size, allowed_chars):  
  return ''.join(random.choice(allowed_chars) for x in range(str_size))

chars = string.ascii_letters + string.punctuation 
size = a



Mylist={
  'Anna':random_string_generator(size, chars),
  'Ivan':random_string_generator(size, chars),
  'Roma':random_string_generator(size, chars),
  'Sasha':random_string_generator(size, chars),
  'Kolya':random_string_generator(size, chars),
  'Borys':random_string_generator(size, chars),
  'Kaytlin':random_string_generator(size, chars),
  'Vi':random_string_generator(size, chars),
  'Rick':random_string_generator(size, chars),
  'Morty':random_string_generator(size, chars),
  'Kakr':random_string_generator(size, chars),
  'Alan':random_string_generator(size, chars)
  }
MyList=str([Mylist])
print (Mylist)


MyFile = open ('output.txt', 'w')

for element in MyList:
     MyFile.write(element)
     MyFile.write('')
MyFile.close()

