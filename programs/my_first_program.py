from nada_dsl import *

def nada_main():
    alice = Party(name="Alice")
    bob = Party(name="Bob")
    
    alice_cats = SecretInteger(Input(name="alice_cats", party=alice))
    bob_dogs = SecretInteger(Input(name="bob_dogs", party=bob))
    
    pet_difference = alice_cats - bob_dogs
    cat_dog_sum = alice_cats + bob_dogs
    pet_product = alice_cats * bob_dogs
    
    cats_win = pet_difference > 0
    winner = cats_win.if_else("Cats rule!", "Dogs drool!")
    
    treat_budget = cat_dog_sum * 5
    
    chaos_factor = pet_product / 10
    
    return [
        Output(winner, "contest_result", alice),
        Output(treat_budget, "treat_budget", bob),
        Output(chaos_factor, "chaos_factor", alice)
    ]