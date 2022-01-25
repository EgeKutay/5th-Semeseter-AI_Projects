from simpleai.search.models import *
from simpleai.search.viewers import WebViewer
from simpleai.search.local import genetic,hill_climbing,hill_climbing_random_restarts
import random
from itertools import permutations




# UI 

print("Welcome to Knapsack Problem")
number_of_items=int(input("Number of Items: "))
knapsack_cap=int(input("Knapsack capacity: "))
items=[]



for x in range(number_of_items):
    wei=int(input("Weight of Item: "))
  
    val=int(input("Value of Item: "))
    item={
      "weight":wei,
      "value":val
    }
    items.append(item)
    
items=tuple(items)
print(items)
bag=[]
for i in range(number_of_items):
    bag.append(random.randint(0,1))
    
print(bag)

def swap(input,k):
    if(input[k]==0):
        input[k]=1
    else:
        input[k]=0
    return input

class KnapsackProblem(SearchProblem):
   def actions(self, state):
       arr=[]
       for i in range(number_of_items):
            arr.append(i)
       arr=list(arr)
       return arr

   def result(self, state, action):
       state = swap(list(state),int(action))
       return tuple(state)

   def value(self, state):
       sum_val=0
       sum_items=0
       for i in range(len(state)):
         if(state[i]==1):
               sum_items+=items[i]["weight"]
               if(sum_items>knapsack_cap):
                  return 0
               else:
                  sum_val+=items[i]["value"]
       return sum_val

   def generate_random_state(self):
        ranar=[]
        for i in range(number_of_items):
            ranar.append(random.randint(0,1))
        return  tuple(ranar)
 #####genetic part#######
   def crossover(self, state1, state2):
       cut_point = random.randint(0, number_of_items)
       child = state1[:cut_point] + state2[cut_point:]
       return tuple(child)

   def mutate(self, state):
        ranar=[]
        for i in range(number_of_items):
            ranar.append(random.randint(0,1))
        mutation=ranar
        mutation_point=random.randint(0,number_of_items)
        return tuple(mutation)
    

problem= KnapsackProblem(initial_state=tuple(bag))
result=genetic(problem,mutation_chance=0.3,population_size=50,viewer=WebViewer())
#result=hill_climbing(problem,0,viewer=WebViewer())
print(result)
  
    