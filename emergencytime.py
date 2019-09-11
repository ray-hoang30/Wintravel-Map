# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 11:56:26 2019

@author: Ray
"""
# importing required libraries 
import csv
import requests, json 
from pyproj import Transformer


letransform = Transformer.from_crs("epsg:3347", "epsg:4326")

hospitalcoords = {'Met': {"lat":42.301318,"lng":-82.999226},
                  'Megahospital' : { "lat":42.270184,"lng":-82.928170},
                  'Ouelette': {"lat":42.308185,"lng":-83.030759},
                  'Leamington':{"lat":42.0486634,"lng":-82.6166188}}


#reads api key
f=open("key.txt", "r")
if f.mode == 'r':
    api_key = f.read()


 

# url variable store url  
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

temptime = {}
final = []

#opens and reads files
with open('center of mass.csv', mode='r') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=',')
    for row in spamreader:
        #checks if it's not the first row
        if row[1] != 'MEAN_X':
            #transforms the coordinate into longitude + laditute
            source = letransform.transform(float(row[1]),float(row[2])) 
            source = str(source[0]) + "," + str(source[1])
            
            for locations in hospitalcoords:
                dest = str(hospitalcoords[locations]['lat']) + ',' + str(hospitalcoords[locations]['lng']) 
                
                # Get method of requests module 
                # return response object 
                r = requests.get(url + 'origins=' + source +
                                   '&destinations=' + dest +
                                   '&key=' + api_key) 
                                     
                # json method of response object 
                # return json format result 
                x = r.json() 
                # bydefault driving mode considered
                # saves the time as a temperary dictionary
                temptime[locations] =   x['rows'][0]['elements'][0]['duration']['value']
            
            #calculates the difference in time
            old = min(temptime['Met'],temptime['Ouelette'],temptime['Leamington'])
            new = min(temptime['Megahospital'],temptime['Leamington'])
            timedifference = new - old
            print (timedifference)
            row.append(str(timedifference))
            final.append(row)
    #writes the file into a new file called 'emresults.csv'
    with open('emresults.csv','w') as writeFile:
        writer = csv.writer(writeFile,dialect='excel')
        writer.writerows(final)
    writeFile.close()