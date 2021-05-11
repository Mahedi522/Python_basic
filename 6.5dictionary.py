data={1:'Mahedi',2:'Evan',3:'Romman'}
print(data)

print(data[3])

print(data.get(1))
print(data.get(4))


print(data.get(4,'new data'))

print(data)

keys=['Mahedi','Evan','Romman']
values=['python','java','js']

data1=dict(zip(keys,values))

print(data1)

print(data1['Mahedi'])

data1['Moni']='c'

print(data1)

del data1['Moni']

print(data1)