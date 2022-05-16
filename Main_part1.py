from fastapi import FastAPI

from typing import Dict, List



# a= [3, 0, 1, 2] a[0]= 3, a[3]= 2, a[2]= 1, a[1]= 0 --> perfect cycle 
def check_cycle (element):
    visited_index = []
    current = 0
    done = False 
    while not done:
        visited_index.append(current)
        current = element[current]
        if 0 == current:
            done = True
        if current> len(element) -1:
            done = True
    visited_index = set(visited_index)
    if (len(visited_index)== len(element) and current ==0):
        return True
    else: 
        return False
    
    
app = FastAPI()

@app.post("/check_cycle")
def endpoint(element: dict [str, list[int]] ):
    result={}
    for i in element.keys():
        result[i] = [element[i], check_cycle(element[i])]
    return result

# to test the code 
"""{
  "list1": [
    0, 1, 2, 3, 4  ],
  "list2": [
    3, 0, 1, 2
  ],
  "list3": [
    4, 5, 6, 7, 9
  ]
}
"""
