#dict1={11:'varun',15:'Arun'}
#print(dict1.get(15))

#captains={}
#type(captains)
#print(type(captains))

captains={'india':'virat','pakistan':'babar','sri lanka':'dimuth'}
print(captains)

print(captains['pakistan'])

print(captains.keys())

print(captains.values())

captains['england']='root'
print(captains)

for team in captains:
    print(team)



for team in captains:
    print(team,'==>',captains[team])

print('autralia' in captains)

print('\n')
print('pakistan' in captains)

print("\n ", captains['sri lanka'] )

print(captains.get('sri lanka'))

#print(captains['australia'])

print(captains.get('india','NULL'))

#creating an empty disctionary and adding values later on

emp={}
emp['name']='Ali'
emp['age']=21
emp['id']=45
print(emp)

#clear dictionary
captains.clear()
print(captains)