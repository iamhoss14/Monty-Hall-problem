
import random


def monty_hall(switch_doors):
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    initial_choice = random.choice(range(3))

    if switch_doors:
        doors_reveald = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        door_revealed = random.choice(doors_reveald)
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice
    return doors[final_choice] == 'car'

def simulate_monty_hall(num_games):
    num_win_without_switching = sum(monty_hall(False) for _ in range(num_games))
    num_win_with_switching = sum(monty_hall(True) for _ in range(num_games))
    return num_win_without_switching / num_games, num_win_with_switching / num_games

if __name__ == "__main__":
    num_games = 10000
    win_without_switching, win_with_switching = simulate_monty_hall(num_games)
    print(f"Win rate without switching: {win_without_switching:.2%}")
    print(f"Win rate with switching: {win_with_switching:.2%}")