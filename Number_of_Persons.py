# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:59:17 2019

@author: saw-b
"""

def number(merkmale):

    number_of_persons = 0
    
    weights = [2, 3, 3, 3, 3, 3, 3]
    max_weights = 0
    for x in range(0, len(weights)):
        max_weights += weights[x]
    max_weights /= len(weights)
    
    number_of_persons = []
    for x in range(1, len(merkmale)):
        number = 0
        for y in range(0, len(merkmale[x])):
            number += merkmale[x][y] * weights[y]
        number /= max_weights
        number_of_persons.append(number)
    
    anzahl = 0
    for z in range(0, len(number_of_persons)):
        anzahl += number_of_persons[z]
    anzahl /= len(number_of_persons)
    
    return anzahl    
        