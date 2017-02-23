#! python
import sys
sys.stdout.write("hello from Python %s\n" % (sys.version,))
a = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
b = [' ' * 2 * (7 - i) + 'very' * i for i in a]
for line in b:
   print (line)