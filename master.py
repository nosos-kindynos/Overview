from modelling import *
from risk_estimation import *
from functions import *

average_transfer_chance=0.14

sources=[6097]

##import input

data=read('master.csv')
people=data[0]
filled_data=data[1]

mapping = model_data_to_weighted_dyadic_relationships(average_transfer_chance , people, filled_data)
list_of_first_degree_connections=mapping[0]
risk_mapping=mapping[1]
full_analysis={}
for person in people:

    if person not in sources:
        
        risk=[]
        contacts_risk = []
        paths = {}

        relative_mapping = relative_map(None,[person],list_of_first_degree_connections)
        contacts=list_of_first_degree_connections.get(person)

        for contact in contacts:
            analysis=estimate_risk( sources , contact , relative_mapping  , risk_mapping ,2)
            posed_risk=analysis[0]*(get_risk((contact,person),risk_mapping))
            contacts_risk.append((contact,posed_risk))
            risk.append(posed_risk)
            paths.update({contact:analysis[1]})
        

        net_risk=union(risk)
        analysed_data=[net_risk, contacts_risk ]
        full_analysis.update({person:analysed_data})


di={}
for i in people:
    di.update({i:[]})
for i in full_analysis:
    for j in full_analysis.get(i)[1]:
        k=di.get(j[0])
        k.append((i,j[1]))
        di.update({j[0]:k})

for person in people:
    if person not in sources:
        k=di.get(person)
        l = full_analysis.get(person)
        report=l+[k]
        # write report for person in file














