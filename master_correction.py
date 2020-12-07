from modelling import *
from risk_estimation import *
from functions import *
import csv
import pygame.gfxdraw
import time
import random
import time
pygame.init()
window = pygame.display.set_mode((1500, 800))
capt = pygame.display.set_caption("Shortest Path")
window.fill((100, 100, 100))
pygame.display.update()

def join(p, q):
    pygame.draw.line(window, (0, 255, 0), p, q, 4)
    pygame.display.update()
accuracy=2
average_transfer_chance=0.14
top_num_of_paths=10

sources=[]

with open('master.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        if not row==[]:
           if row[1].endswith('*'):
              sources.append(int(row[0]))


data=read('master.csv')
people_who_filled_data=data[0]
filled_data=data[1]

mapping = model_data_to_weighted_dyadic_relationships(average_transfer_chance, filled_data)
list_of_first_degree_connections=mapping[0]
risk_mapping=mapping[1]
full_analysis={}
people=mapping[2]
paths=[]
combos=[]

for person in people:

    if person not in sources:
        
        risk=[]
        contacts_risk = []

        relative_mapping = relative_map(None,[person],list_of_first_degree_connections)
        contacts=list_of_first_degree_connections.get(person)

        for contact in contacts:
            analysis=estimate_risk_of_target( sources , contact , relative_mapping  , risk_mapping ,accuracy , top_num_of_paths)
            posed_risk=analysis*(get_risk((contact,person),risk_mapping))
            contacts_risk.append((contact,posed_risk))
            risk.append(posed_risk)


        net_risk=union(risk)
        analysed_data=[net_risk, contacts_risk ]
        full_analysis.update({person:analysed_data})


dominancy_values=estimate_risk_of_relation_infection_in_social_network(people,list_of_first_degree_connections,risk_mapping)
dominancy_values=sort_values(dominancy_values)
    
print(dominancy_values)





di={}
for i in people:
    di.update({i:[]})
for i in full_analysis:
    for j in full_analysis.get(i)[1]:
        k=di.get(j[0])
        k.append((i,j[1]))
        di.update({j[0]:k})


write(people,full_analysis,di,'master.csv',sources)


temp={}
for i in people:
    pos1=random.randint(50,1450)
    pos2 = random.randint(50, 750)
    pos=(pos1,pos2)
    temp.update({i:pos})

k = temp.get(7959)
l=temp.get(7623)

pygame.gfxdraw.filled_circle(window, k[0], k[1], 15, (255, 0, 0))
pygame.gfxdraw.filled_circle(window, l[0], l[1], 15, (0, 0, 255))

for i in risk_mapping:
    x=temp.get(i[0])
    y=temp.get(i[1])
    join(x,y)
    time.sleep(0.01)


run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
