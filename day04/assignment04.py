# in (T,F)
# copy :shallow,deep
# list mutable: copy 
# 과제 -  책205p ~8.10

# 01
e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)

# 02
print(e2f['walrus'])

# 03
f2e = {french:eng for eng, french in e2f.items()}

# 04
print(f2e['chien'])

# 05
# print(list(e2f.keys()))
print(e2f.keys())

# 06
animals= {'cats':'Henri','octopi':'Grumpy','emus':'Lucy'}
plants =[]
other = []
tuple_of_lists = animals, plants, other
list_of_lists = ['cats','octopi','emus'],[],[]
life = {'animals': animals, 'plants': plants, 'other': other}
life

# 07
print(life.keys())

# 08
print(life['animals'].keys())

# 09
print(life['animals']['cats'])

# 10
squares = {number: number*number for number in range(10)}
squares

# 11
squares_odds = {number: number*number for number in range(10) if number%2 != 0}
squares_odds

# 12 
word = 'Got'
for i in range(10):
    