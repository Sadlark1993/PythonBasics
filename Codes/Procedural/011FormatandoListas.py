#ManipulandoListas

a = [1, 2, 3, 4]
a.append(5)
print(a)

a.extend([6,7,8])
print(a)

a.insert(0, 'inicio')
print(a)

a.remove('inicio')
print(a)

a.pop(0)
print(a)

print(a.count(2))

print(a[::-1])
