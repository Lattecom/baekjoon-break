from sys import stdin

color_list = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 
              'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7,
              'grey': 8, 'white': 9}

f = input()
s = input()
t = input()

print( (color_list[f] * 10 + color_list[s]) * (10 ** color_list[t]) )
