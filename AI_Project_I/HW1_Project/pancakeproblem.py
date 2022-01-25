from simpleai.search import SearchProblem, astar, breadth_first, depth_first, uniform_cost, greedy, limited_depth_first, iterative_limited_depth_first
from simpleai.search.viewers import WebViewer
import random
#User interface
pancake_number=int(input('Enter number of pancakes (>2): '))
while(True):
  
  if(isinstance(pancake_number, int) and pancake_number>2):
    break
  else:
    pancake_number = int(input('Please enter Integer value (>2) : '))
  
decision=input("Do you want to enter ordering?(yes / no) : ")
cakelist = []
while(True):
 if(decision.lower()=="no"): 
    cakelist = list(range(pancake_number))
    random.shuffle(cakelist)
    
    break
 elif(decision.lower()=="yes"):
    print("Enter top to bottom ordering between [0-"+str(pancake_number-1)+"],seperated by spaces: ")
    cakelist=list(map(int, input().split()))
    break    
 else:
    decision = input("Please only pick 'yes' or 'no': ")
    
print("initial state: ", end="")
print(cakelist)    

#reversing the arrray by index func.
def reversePancakeByIndex(input, k): 
    return (input[k-1::-1] + input[k:]) 


class PancakeProblem(SearchProblem):
    def __init__(self):
        super(PancakeProblem, self).__init__(initial_state=tuple(cakelist))
    def actions(self, state):
        cakes = list(range(pancake_number))
        for a in range(pancake_number):
            cakes[a] = a+1
        return cakes

    def result(self, state, action):
        state = reversePancakeByIndex(state, int(action))
        return state

    def is_goal(self, state):
        self.goal = tuple(sorted(cakelist))
        return state == self.goal

    def heuristic(self, state):
        h = 0
        sortedcake = sorted((cakelist))
        for i in range(pancake_number):
            if(state[i] == sortedcake[i]):
                h = h+1
        return pancake_number-h


    def cost(self, state, action, state2):
       return int(action)


problem = PancakeProblem()
result = breadth_first(problem, graph_search=True, viewer=WebViewer())
#result = depth_first(problem,graph_search=True,viewer=WebViewer())
#result = uniform_cost(problem,graph_search=True,viewer=WebViewer())
#result = iterative_limited_depth_first(problem,graph_search=True,viewer=WebViewer())
#result = limited_depth_first(problem,graph_search=True,viewer=WebViewer())
#result = astar(problem,graph_search=True,viewer=WebViewer())
#result = greedy(problem,graph_search=True,viewer=WebViewer())
