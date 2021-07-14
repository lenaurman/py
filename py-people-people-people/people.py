import pandas as pd

p1 = {
    'name' : 'Haruki Murakami',
    'titles' : ['writer'],
    'creations' : ['Man in the Taxi','The Wind-Up Bird Chronicle'],
    'creations_year' : [2000,1998]  #need a check
}

p2 = {
    'name' : 'David Lynch',
    'titles' : ['filmmaker'],
    'creations' : ['Lost Highway'],
    'creations_year' : [1997] #need a check
}

p3 = {
    'name' : 'Michelle Gurevich',
    'titles' : ['singer'],
    'creations' : ['Party Girl'],
    'creations_year' : [2010] #need a check
}

#
## add p4 please
#
# DataFrame from list pf dicts
ppd = pd.DataFrame([p1, p2, p3])

print()
print('---------- People you must know dataset ----------------')
print()
print(ppd)
ppd.to_csv('people_you_must_know.csv')
print('Saved to csv.. i hope..')
print()

print("Add p4 please")
print()