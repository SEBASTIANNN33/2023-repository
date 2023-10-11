import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 15  
    
    print(f"Myslím si čislo mezi 1 a 100.")
    
    while attempts < max_attempts:
        try:
            guess = int(input("Hádej: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        attempts += 1
        
        if guess < secret_number:
            print("Málo.")
        elif guess > secret_number:
            print("Moc.")
        else:
            print(f"Skvěle, uhádl jsi správné číslo {secret_number} v {attempts} pokusech! 	(ﾉ◕ヮ◕)ﾉ*:・ﾟ✧")
            break
    
    if attempts >= max_attempts:
        print(f"Přesáhl jsi počet pokusů, hledané číslo bylo {secret_number} ┌П┐(ಠ_ಠ)")
if __name__ == "__main__":
    guess_the_number()
