from fastapi import FastAPI,Query
from enum import Enum
from item_model import Items

class Greetings(str,Enum):
    morning="Good Morning"
    evening = "Good Evening"
    night = "Good Night"

app = FastAPI()


#query parameters
#this function need to be at first place as fastapi reads it line by line
@app.get("/query")
def get_query(skip:int = 0 , limit:bool = True):
    if(skip>0 and limit):
        reply = "Skipping files and limiting results"
    elif(limit and skip == 0):
        reply = "Limiting results without skipping"
    else:
        reply="Showing results without skipping or limiting"
    
    return {"reply":reply}


#path parameter and simple function
@app.get("/greet/{greet}")
def root(greet:Greetings):
    if(greet == Greetings.morning):
        return {"Greet":Greetings.morning}
    elif(greet == Greetings.evening):
        return {"Greet":Greetings.evening}
    elif(greet == Greetings.night):
        return{"Greet":Greetings.night}
    else:
        return{"Warning":"Invalid greeting!"}
    

#getting a post request
@app.post("/add-items")
def add_items(item:Items):
    if item:
        return item
    else:
        return{"Error":"No item was given"}

#validation using query parameter
#'...' makes parameter required, we can use a defaut value or None to make it optional
@app.post("/email")
def validate_email(email:str = Query(...,max_length=50,min_length=5)):
    if email:
        return {"email":email}
    else:
        return{"Error":"Invalid email!"}

