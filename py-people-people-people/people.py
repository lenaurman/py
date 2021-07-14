import pandas as pd

p1 = {
    'name' : 'Haruki Murakami',
    'titles' : ['writer'],
    'creations' : ['Man in the Taxi']
}

p2 = {
    'name' : 'David Lynch',
    'titles' : ['filmmaker'],
    'creations' : ['Lost Highway']
}

p3 = {
    'name' : 'Michelle Gurevich',
    'titles' : ['singer'],
    'creations' : ['Party Girl']
}
## add p4 please
pp = [p1, p2, p3]
ppd = pd.DataFrame(pp)


ppd.to_csv('people_you_must_know.csv')
print(ppd)
print("Add p4 please")
