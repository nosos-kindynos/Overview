

This project is completely open source and we look forward to your suggestions regarding any errors or logical fallacies overlooked, and regarding general scope for improvement. As a user might base his judgements on these statistics, inaccurate results would compromise their safety, thus defeating the whole intention of this project.

This project is only a prototype and has not been designed for mass use. Rather, it conveys an idea which we hope will provide an incentive to furthering development along these lines, thus progressing society as a whole.


# Disease Risk Estimation

#### Infectious disease transmission risk estimation by modelling disease transmission dynamics through user updated social interactions.

This project is designed for estimating risks based on social connections of a population assuming relatively simple and ideal one to one transmission dynamics, also assuming that the necessary protocols such as hygiene, social distancing, wearing surgical face masks, etc. are being followed. It may not be capable of analysing large social gatherings where transmission dynamics get more advanced and relatively chaotic, making parameters that are insignificant here important enough to produce a significantly different result,  requiring more advanced and sophisticated methods.

The project does not possess an autonomous input system and relies on user inputted data for analysing social dynamics to predict the risk a compromised person provides to the user. Since the population is assumed not to be a closed ecosystem, we rely on and expect a user to update us when their health has been compromised, based on which we estimate the risk the user provides to other users in the population.

Once we estimate the risk of all users, we can segregate users and suggest which users should isolate themselves, which friends the users should avoid to reduce their own risk, or if they pose a risk to some other user - as a whole, an effort to slightly morph the social dynamics in order to reduce the spread of the disease.

It provides the user with information that will enable them to make the necessary judgements.

With all good hope, we wish that it can make some difference and avoid something unwanted from happening.

                          _______________________________________________________________________________



# Workflow

### User input -----------> Modelling data into a one on one risk mapping -----------> Computing net risk of the user based mapping -----------> Return data to user


An example of the process may provide an incentive of the algorithmic flow for computing the net risk.

                          _______________________________________________________________________________

## Example

Assuming social relationship of 5 people namely A,B,C,D and E with their individual relationships given is given a one on one transfer chance and is modelled graphically as follows:
                    
                              B
                            /   \
                      0.5  /     \ 0.5 
                          /       \      0.5 
                         A         D - - - - - - E 
                          \       /   
                     0.5   \     /  0.5   
                            \   /         
                              C
                              
                              
                              
Assuming user A's health has been compromised and the information is based on a medical confirmation, user E wishes to know the risk A poses to him.
Intuitively we may see that both B and C possess 0.5 chance of contracting the disease throough paths (A,B) and (A,C) respectively and so D has 0.25 chance of contecting the disease from B and C each.

We have assumed the chances of contracting of a disease from different sources to be independent of each other, since transmssion dynamics vary from disease to disease and we are not very well aware of their mechanism.

So the risk of user D can be calculated by taking a set union of both the probabilities , which is 0.25 + 0.25 - (0.25 x 0.25) = 0.4375
A different approach is to calculate the chance of D NOT contracting the disease from either B or C , and then taking the conjugate of the same , which is 
(1 - 0.25) x (1 - 0.25) = 0.5625 chance of NOT contracting , hence a 1 - 0.5625 = 0.4375 chance of contracting.

So since D has a 0.4375 chance of contracting , the chance of user E contecting is a set intersection of the chance of D contracting it and D transferring it , since assumed to be independent , the intersection can be treated as a binary multiplication. 

Hence user E has a 0.4375 x 0.5 = **0.21875** chance of contracting the given infectious disease.


In the above risk calculation, we have only estimated the risk of E and the intermediate values cannot be asserted as the risks for other users.
Again, as a case in the above example, we calculated user B to only have a 0.5 chance of contracting , but that is only directly from A and is not to be mistaken as the total risk A poses to B , as it is not necessary that only B can infect D.

So B has a 0.5 chance of contracting it from A , and a ( 0.5 x 0.5 x 0.5 ) of contracting it from D , hence making it a total of 
 0.5 + ( 0.5 x 0.5 x 0.5 ) - 0.5 x ( 0.5 x 0.5 x 0.5 ) = 0.6625 chance and not a 0.5 chance.
 
We also assume here than the disease cannot infect a user who is already part of the chain we are currently using to reach a user , as we are assumming an infection to have a binary state of existence here. So to estimate the risk of a certain user, we need to find all the paths through which a disease can reach the user and return the combined risk factor.

So the ways through which E may be infected are (A-->B-->D-->E) and (A-->C-->D-->E). We can find the set union of the risks from both the paths, but keeping in mind that there may be common relations in all possible paths which may be considered multiple times during calculation - in this case D to E is common.

Hence by the laws of set theory , the relations are independent events and for a disease to progress through a path , it has to infect all previous users in the path , hence a path may be treated as a set intersection of all the possible events and the net risk can be treated as a set union of all paths.

Hence in this case , the result being (where the event/relation is represented by the 2 users connected by it):

( (A,B) ∩ (B,D) ∩ (D,E) )    U    ( (A,C) ∩ (C,D) ∩ (D,E) )

= ( (A,B) x (B,D) x (D,E) ) + ( (A,C) x (C,D) x (D,E) ) -    ( (A,B) ∩ (B,D) ∩ (D,E) )    ∩    ( (A,C) ∩ (C,D) ∩ (D,E) )

= ( (A,B) x (B,D) x (D,E) ) + ( (A,C) x (C,D) x (D,E) ) -    ( (A,B) x (B,D) x (D,E) x (A,C) x (C,D)  )

= ( 0.5^3 + 0.5^3 - 0.5^5 ) = 0.125 + 0.125 - 0.03125 = **0.21875 chance**


We hope that the above example provided an incentive and clarity on the idea.    

               _______________________________________________________________________________
                          
                          
So after modelling the social interaction into a risk mapping , the compuatation can be done by finding all possible paths from a source to a target and then calculating the risk by taking the internal events in the paths as an intersection and then a whole union of all the possible paths , and then substituting the independent chances once a suitable expression has been obatined.


               _______________________________________________________________________________
               

The individual subsections of this project can be found in their respective repositories.






        
