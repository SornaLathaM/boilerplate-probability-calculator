import random
import copy

class Hat:
  def __init__(self,**kwargs):
    self.contents=[str(key)  for key,value in kwargs.items() for i in range(value)]

    
  def draw(self,n):
     drawn=[]
     if len(self.contents)<n:
       return self.contents
     else:
          for i in range(n):
              i= random.randint(0,len(self.contents))
              drawn+=[self.contents.pop(i)]
          
          return drawn
  
  
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob=0
    exp=[str(key) for key,value in expected_balls.items() for i in range(value)]
    for i in range(num_experiments):
        copy_hat=copy.deepcopy(hat)
        drawn_balls=copy_hat.draw(num_balls_drawn)
        check=[]
        for ball in exp:
            if ball in drawn_balls:
                drawn_balls.remove(ball)
                check.append(ball)
        if len(check)==len(exp):
                prob+=1
                
    return prob/num_experiments
