#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd

# install conda
get_ipython().system(' conda install -c conda-forge folium')
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values
# import the library
import folium

def createPPD():
    p1 = {
        'name' : 'Haruki Murakami',
        'titles' : ['writer'],
        'creations' : ['Man in the Taxi','The Wind-Up Bird Chronicle'],
        'creations_year' : [2000,1998], 
        'place' : ['Tokio, Japan']  #need a check
    }

    p2 = {
        'name' : 'David Lynch',
        'titles' : ['filmmaker'],
        'creations' : ['Lost Highway'],
        'creations_year' : [1997], 
        'place' : ['Los Angeles, United States'] #need a check
    }

    p3 = {
        'name' : 'Michelle Gurevich',
        'titles' : ['singer'],
        'creations' : ['Party Girl'],
        'creations_year' : [2010], 
        'place' : ['Toronto, Canada'] #need a check
    }

    #
    ## add p4 please
    #

    p4 = {
        'name' : 'Salvador Dali',
        'titles' : ['artist'],
        'creations' : ['A Couple with Their Heads Full of Clouds', 'Apparition of Face and Fruit Dish on a Beach', 
                       'The Disintegration of the Persistence of Memory'],
        'creations_year' : [1936, 1938, 1954], 
        'place' : ['Port Lligat, Spain'] #need a check
    }

    p5 = {
        'name' : 'Antoni Gaudí',
        'titles' : ['architect'],
        'creations' : ['Casa Batlló'],
        'creations_year' : [1906], 
        'place' : ['Barcelona, Spain'] #need a check
    }

#     DataFrame from list pf dicts
    ppd = pd.DataFrame([p1, p2, p3, p4])
    ppd = ppd.append(p5, ignore_index = True)

    print('\n ---------- People you must know dataset ---------------- \n')
    
    return ppd


# print(ppd,'\n')
# ppd.to_csv('people_you_must_know.csv')
# print('Saved to csv.. i hope.. \n')

# print("p4 added \n")

# display(ppd)


# In[10]:


# Define a user_agent ---> ny_explorer
geolocator = Nominatim(user_agent="ny_explorer")

# Make an empty map
m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2.2)

# Create Data Frame
ppd = createPPD()
ppd.set_index('name', drop = True, inplace = True)
display(ppd)

for name in ppd.index:
    
#     display(name, ppd.loc[[name],['titles', 'creations', 'creations_year']], list(ppd.loc[[name],:].transpose().index))

    #  Get persons location
    address = ppd.loc[[name],:].transpose()[name].values[3][0]
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    
#     print('The geograpical coordinate of {} are {}, {}.'.format(name, latitude, longitude))
    
    # get persons feachers
    features = ppd.loc[[name],:].transpose()[name]

    # Make Markers with Lables on the map
    description = ''
    for i in range(len(features.values[1])):
        description += str(features.values[1][i]) + ' ('  + str(features.values[2][i]) + ')' + '<br>'  
    
    label = folium.IFrame(str(name) + ' - ' + str(features.values[0][0]) + '<br>' + str(address) + '<br>'  + description)
    
    marker = folium.Marker(
        [latitude, longitude],
        radius=5,
        popup = folium.Popup(label, min_width=250, max_width=500)
    ).add_to(m)
    

    # Show the map
m


# In[ ]:





# In[35]:


# install conda
get_ipython().system(' conda install -c conda-forge folium')
# import the library
import folium

# Make an empty map
m = folium.Map(location=[20,0], tiles="OpenStreetMap", zoom_start=2)

# Show the map
m


# In[38]:


get_ipython().system('pip install geocoder')
get_ipython().system('conda install -c conda-forge geopy --yes')
#import geocoder
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values


# In[39]:


address = 'Barcelona, Spain'

geolocator = Nominatim(user_agent="ny_explorer") # In order to define an instance of the geocoder, one need to define a user_agent ---> ny_explorer
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude

print('The geograpical coordinate of Barcelona are {}, {}.'.format(latitude, longitude))


# In[ ]:




