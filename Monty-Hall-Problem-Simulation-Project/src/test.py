
import random

"""
MONTY HALL PROBLEM SIMULATION
=============================

This module simulates the famous Monty Hall problem from probability theory.

THE PROBLEM:
- You're on a game show with 3 doors
- Behind one door is a car (prize), behind two doors are goats
- You choose a door initially
- The host (Monty) opens one of the remaining doors to reveal a goat
- You're given the option to switch to the last unopened door
- Question: Should you switch?

THE ANSWER: YES! Switching gives you a 2/3 chance of winning, while staying gives 1/3 chance.

THEORY:
- Without switching: You have a 1/3 chance (only if you initially picked the car)
- With switching: You have a 2/3 chance (since you likely initially picked a goat)

This module demonstrates this mathematically through simulation.
"""


def monty_hall(switch_doors):
    """
    Simulates a single game of the Monty Hall problem.
    
    PARAMETERS:
    -----------
    switch_doors (bool): If True, the player switches doors after one is revealed.
                         If False, the player sticks with their initial choice.
    
    RETURNS:
    --------
    bool: True if the player wins the car, False if they get a goat.
    
    LOGIC FLOW:
    -----------
    1. Create 3 doors: 2 goats and 1 car
    2. Randomly shuffle the door contents
    3. Player makes a random initial choice (picks a door 0-2)
    4. IF switching:
       - Find all doors that are NOT the player's initial choice AND don't have the car
       - Monty reveals one of these goat doors randomly
       - Player switches to the remaining unopened door
    5. IF not switching:
       - Player keeps their initial choice
    6. Return whether the final choice has the car
    
    EXAMPLE 1 - WITHOUT SWITCHING (stick with initial choice):
    ---------------------------------------------------------
    >>> random.seed(42)
    >>> monty_hall(False)  # Player doesn't switch
    False
    
    EXAMPLE 2 - WITH SWITCHING (switch after reveal):
    --------------------------------------------------
    >>> random.seed(42)
    >>> monty_hall(True)  # Player switches to the other door
    True
    """
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    initial_choice = random.choice(range(3))

    if switch_doors:
        # Find doors that are NOT the player's choice AND don't have the car
        # These are the goat doors Monty can reveal
        doors_reveald = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        
        # Monty randomly picks one goat door to reveal
        door_revealed = random.choice(doors_reveald)
        
        # Player switches to the remaining door (not initial choice, not revealed)
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        # Player sticks with their initial choice
        final_choice = initial_choice
    
    # Return True if the final choice has a car, False if it's a goat
    return doors[final_choice] == 'car'

def simulate_monty_hall(num_games):
    """
    Runs multiple simulations of the Monty Hall problem to calculate win rates.
    
    PARAMETERS:
    -----------
    num_games (int): Number of games to simulate. Higher numbers give more accurate results.
    
    RETURNS:
    --------
    tuple: (win_rate_without_switching, win_rate_with_switching)
           Both values are floats between 0 and 1 representing win percentages.
    
    HOW IT WORKS:
    --------------
    1. Runs num_games iterations of monty_hall(False) and sums the wins (True values)
    2. Runs num_games iterations of monty_hall(True) and sums the wins
    3. Divides each sum by num_games to get the win rate (probability)
    
    EXAMPLES:
    ---------
    >>> # Simulate 1000 games
    >>> without_switch, with_switch = simulate_monty_hall(1000)
    >>> print(f"Without switching: {without_switch:.1%}")
    >>> print(f"With switching: {with_switch:.1%}")
    # Expected output (approximately):
    # Without switching: 33.3%
    # With switching: 66.7%
    
    >>> # Simulate a larger sample for better accuracy
    >>> without_switch, with_switch = simulate_monty_hall(100000)
    >>> print(f"Without switching: {without_switch:.3%}")
    >>> print(f"With switching: {with_switch:.3%}")
    # Expected output (approximately):
    # Without switching: 333.333%
    # With switching: 666.667%
    """
    num_win_without_switching = sum(monty_hall(False) for _ in range(num_games))
    num_win_with_switching = sum(monty_hall(True) for _ in range(num_games))
    return num_win_without_switching / num_games, num_win_with_switching / num_games

if __name__ == "__main__":
    """
    MAIN EXECUTION EXAMPLE:
    ======================
    
    This runs when you execute: python test.py
    
    It simulates 10,000 games of Monty Hall and prints the results.
    
    EXPECTED OUTPUT:
    ----------------
    Win rate without switching: 33.33% (approximately 1/3)
    Win rate with switching: 66.67% (approximately 2/3)
    
    This demonstrates that switching doubles your chances of winning!
    
    DEEPER UNDERSTANDING:
    ---------------------
    Why does switching win 2/3 of the time?
    
    Scenario 1 (1/3 probability): You initially picked the CAR
    - Monty reveals a goat
    - If you switch: You get a goat (LOSE)
    - If you stay: You get the car (WIN)
    
    Scenario 2 (2/3 probability): You initially picked a GOAT
    - Monty reveals the OTHER goat
    - If you switch: You get the car (WIN)
    - If you stay: You get the goat (LOSE)
    
    So switching wins in 2 out of 3 scenarios!
    """
    num_games = 10000
    win_without_switching, win_with_switching = simulate_monty_hall(num_games)
    print(f"Win rate without switching: {win_without_switching:.2%}")
    print(f"Win rate with switching: {win_with_switching:.2%}")

