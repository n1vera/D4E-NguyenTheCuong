sheep_flock = [5, 7, 300, 90, 24, 50, 75]
print('hello my name is Cuong and these are my ship sizes')
print(sheep_flock)
a = max(sheep_flock)
vitri = sheep_flock.index(a)
print('con cuu lon nhat là', a)
sheep_flock[vitri] = 8
print('after sheering, here is my  flock',sheep_flock)
