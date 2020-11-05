

This project is completely open source and we look forward to considering your suggestions about any error we might have overlooked or any logical fallacy we might have not been able to figure out , or even a scope for improvement as a user's actions and judgements concerning their own safety might use these statistics as a dominant parameter and giving them inaccurate results might lead to a compromise of their safety , contradicting the whole intention of this project.

This project is just a prototype and has not been designed to fully  be put to mass use , but rather to just convey an idea , which we hope can provide an incentive in the development of further ideas thus progressing society as a whole.


# Disease Risk Estimation

#### Infectious disease transmission risk estimation by modelling disease transmission dynamics through user updated social interactions.

This project is designed for estimating risks based on social connections of a population assumming relatively simple and ideal one to one transmission dynamics with the hope that the necessarry protocols such as hygiene,social distancing, wearing surgical face masks, etc. are being followed and may not be capable of analysing large social gatherings or physical contacts where transmission dynamics get more advanced and relatively chaotic , making parameters assumed insignificant here dominant enough to produce a significantly different result ,  thus require more advanced and sophesticated methods.

The project does not posses an autonomous input system and relies user inputed data for analysing social dynamics to predict the risk a compromised person provides to a user. Since the population is assumed to not be a closed ecosystem , we rely and expect a user to update us when their health has been compromised and they might act as a potential carrier of the infectious disease , based on which we estimate the risk the user provides to other users in the population.

Once we estimate the risk of all users , we can segregate users and suggest which users should isolate themselves , which friends should users avoid to reduce their own risk or if they pose a risk to some other user , in a whole an effort to slightly morph the social dynamics to reduce the spread of the disease.

It cannot take action, all it can do is give people information with the hope that they will take the right necessarry actions,as people should know what they are dealing with.


With all good hope, we wish that it can make some difference and avoid something unwanted from happening.




# Workflow

### User input -----------> Modelling data into a one on one risk mapping -----------> Computing net risk of the user based mapping -----------> Return data to user


An example of the process may provide an incentive of the algorithmic flow for computing the net risk.
## Example

Assuming soical relationship of 5 people namely A,B,C,D and E with their induvidual relationships given is given a one on one transfer chance and is modelled graphically as follows:
                    
                              B
                            /   \
                      0.5  /     \ 0.5 
                          /       \      0.5 
                         A         D - - - - - - E 
                          \       /   
                     0.5   \     /  0.5   
                            \   /         
                              C
                              
                              
                              
Assumming user A updates on the compromisation of his health based on a medical confirmation , user E wishes to know the risk A poses to him.
Intuitively we may see that both C and D posses 0.5 chance of contracting the disease throough paths (A,B) and (A,C) respectively and so D has 0.25 chance of contecting the disease from B and C each.

We assume the chances contracting of a disease from different sources to be independent , since transmssion dynamics vary from disease to disease and we are not very well informed on their mechanism.

So the risk of user D can be calculated by taking a set union of both the probabilities , which is 0.25 + 0.25 - (0.25 x 0.25) = 0.4375
A different view may be to calulate the chance of D NOT contracting the disease from either B or C , and then taking the conjugate of the same , which is 
(1 - 0.25) x (1 - 0.25) = 0.5625 chance of NOT contracting , hence a 1 - 0.5625 = 0.4375 chance of contracting.

So since D has a 0.4375 chance of contracting , the chance of user E contecting is a set intersection of the chance of D contracting it and D transferring it , since assumed to be independent , the intersection can be treated as a binary multiplication. 

Hence user E has a 0.4375 x 0.5 = 0.21875 chance of conteacting the given infectious disease.









        
