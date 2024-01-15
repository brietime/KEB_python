univ = "Inha university"

print(univ)
print(univ[5])

# univ[5] = 'U' //immutable
# print(univ) #변경안됨

subjects = ['python','c++', 'linux', 'data structure', 'database']
print(subjects)
print(subjects[3])

subjects[3] = 'data structure & algorithm' #mutable
print(subjects)

# frozenset is not mutable 

# print(0.1)
# print(1e-1)
# print(21000)