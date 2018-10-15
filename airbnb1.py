'''
Created on 14-Oct-2018

@author: User
'''
from test import test_platform
def simulate_diplomacy(input_arr):
    '''
    input_arr  : is an array of strings
    '''
    teams = [x[0] for x in input_arr]
    team_strength = {}
    for i in teams:
        team_strength[i]=1
    #print team_strength
    places={}
    status = {}
    for x in input_arr:
        if "Supports" in x:
            a=x.split(" ")
            a=a[3]
            team_strength[a] = team_strength.get(a, 1) + 1
    print team_strength
    for x in input_arr:
        a = x.split(" ")
        if a[1] in places:
            places[a[1]].append(a[0])
        else:
            places[a[1]]=[a[0]]
    print places
    for x in input_arr:
        a=x.split(" ")
        team = a[0]
        flag = 0
        if "Move" in x:
            new_place=a[3]
            if new_place in places:
                conflict = places[new_place]
                print conflict,team
                for i in conflict:
                    if team_strength[team]>team_strength[i]:
                        flag +=1
                        status[i] = "Dead"
                    elif team_strength[team] == team_strength[i]:
                        status[team] = "Dead"
                        status[i] = "Dead"
                if flag == len(conflict):
                    status[team]="Moves to %s "%new_place
                else:
                    status[team] = 'Dead'
        if "Supports" in x :
            place = a[1]
            if team not in status:
                status[team]="Supports from %s"%place
        if "Stays" in x:
            place =a[1]
            if team not in status:
                status[team] = "Stays in %s"%place
    for k,v in status.items():
        print k,v
a=["A London Move Paris","B Paris Stays","C Paris Supports A","D Paris Supports B"]
simulate_diplomacy(a)
        
    