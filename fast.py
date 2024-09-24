from fastapi import FastAPI, HTTPException
from random import randint
import time

app = FastAPI()

number_to_guess = randint(1, 10)


guesses = []

@app.get("/guess/{number}")
def guess_number(number: int):

    guesses.append(number)

    if number < 1 or number > 10:
        raise HTTPException(status_code=400, detail="Número deve estar entre 1 e 10")
    if number < number_to_guess:
        return {"message": "Tente um número maior!"}
    elif number > number_to_guess:
        return {"message": "Tente um número menor!"}
    else:
        return {"message": "Parabéns! Você adivinhou o número!"}

@app.get("/guesses")
def get_guesses():
    return {"guesses": guesses}
