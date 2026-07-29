import modules
print(modules.add(10,20))
print(modules.sub(10,20))


from modules import add ,sub
print(add(10,20))
print(sub(10,20))



from modules import *
print(add(10,20))
print(sub(10,20))




import modules
print(modules.add(10,20))
print(modules.sub(10,20))


import modules as m
print(m.add(10,20))
print(m.sub(10,20))



import modules as m
if __name__ =='__name__':
    print(m.add(5,6))