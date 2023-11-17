dictionary = {1:'Pranjal',2:'Dubey',3:'Ram',4:'shaym'}
print(dictionary[1])

person = {}

person['fname'] ='Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['ralph','Betty','Joe']
person['pets'] = {'dog':'Fido','cat':'milo'}

print(person['pets']['cat'])

# restriction on dictinary keys

foo = {42:'aaa',2.78:'bbb',True:'ccc'}
print(foo[1])

# operators and builtin functions


MBL_team = {
    'Colorado':'Rockies',
    'Boston':'Red Sox',
    'Minnesota':'Twins',
    'seattle':'Mariners'
}

# membership verification

print('Milwakuee' in MBL_team)
print('Toronto' not in MBL_team)

# instace verification 'is'

# short-circuit evaluation

print('Toronto' in MBL_team and MBL_team['Toronto'])
# how to get number of key value pairs in dictionary

print(len(MBL_team))