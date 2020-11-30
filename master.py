from modelling import *
from risk_estimation import *
from functions import *

average_transfer_chance=

import input

data=read('student_list.csv')
people=data[0]
filled_data=data[1]

mapping=model_data_to_weighted_dyadic_relationships(people,filled_data )
list_of_first_degree_connections=mapping[0]
risk_mapping=mapping[1]




for person in people:
    
    relative_mapping = relative_map(None,[person],list_of_first_degree_connections)
    contacts=people.get(person)
    
    for contact in contacts:

        analysis=estimate_risk( source , contact , relative_mapping  , risk_mapping ,2)
        risk.update({contact:analysis[0]})
        paths.update({contact:analysis[1]})



import output











