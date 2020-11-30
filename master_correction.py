from modelling import *
from risk_estimation import *
from functions import *

average_transfer_chance=0.14

source=[6097]

##import input

data=read('master.csv')
people=data[0]
filled_data=data[1]

mapping=model_data_to_weighted_dyadic_relationships(people,filled_data)
list_of_first_degree_connections=mapping[0]
risk_mapping=mapping[1]

risk={}
paths={}

for person in people:
    
    relative_mapping = relative_map(None,[person],list_of_first_degree_connections)
    contacts=list_of_first_degree_connections.get(person)
    
    for contact in contacts:

        if contact==6097:
            continue

        analysis=estimate_risk( source , contact , relative_mapping  , risk_mapping ,2)
        print('analysis',analysis)
        risk.update({contact:analysis[0]})
        paths.update({contact:analysis[1]})

#print(risk)

##import output











