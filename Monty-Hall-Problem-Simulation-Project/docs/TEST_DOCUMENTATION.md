# Monty Hall Problem Simulation - Test Documentation

## Project Goal

This project implements a **Monte Carlo simulation** of the famous [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem) to demonstrate and verify the counterintuitive probability results through computational experimentation.

### The Monty Hall Problem Explained

The Monty Hall Problem is a classic probability puzzle:
- **Setup**: There are 3 doors. Behind one door is a car (prize), behind the other two are goats.
- **The Game**: 
  1. You choose a door at random
  2. The host (Monty Hall) opens one of the remaining doors that contains a goat
  3. You're given the option to **switch** to the other unopened door or **stay** with your original choice
- **The Question**: Should you switch or stay to maximize your chances of winning the car?

### The Counterintuitive Answer

Most people intuitively think it doesn't matter (50/50 chance), but the mathematics shows:
- **If you STAY**: ~33% chance of winning (1 in 3)
- **If you SWITCH**: ~67% chance of winning (2 in 3)

This project verifies this result empirically through simulation.

---

## How the Code Works

### Function 1: `monty_hall(switch_doors)`

This function simulates a **single round** of the Monty Hall game.

**Parameters:**
- `switch_doors` (bool): Whether the player switches doors (`True`) or stays (`False`)

**Logic:**
1. **Setup the doors**: Creates a list with 2 goats and 1 car, then shuffles randomly
2. **Initial choice**: Player randomly selects one of the 3 doors (0, 1, or 2)
3. **Monty's action**:
   - Host reveals a door with a goat (not the player's choice, and must have a goat)
   - If `switch_doors=True`: Player switches to the only remaining unopened door
   - If `switch_doors=False`: Player sticks with their initial choice
4. **Check result**: Returns `True` if final choice is the car, `False` otherwise

**Return Value:** `True` if the player wins (chose the car), `False` if they lose (chose a goat)

### Function 2: `simulate_monty_hall(num_games)`

This function runs **multiple rounds** of the game to calculate win rates.

**Parameters:**
- `num_games` (int): Number of simulation rounds to run

**Logic:**
1. Runs `num_games` rounds WITHOUT switching and counts wins
2. Runs `num_games` rounds WITH switching and counts wins
3. Calculates win rate for each strategy as a percentage

**Return Value:** Tuple of two floats
- First value: Win rate without switching (should be ~0.33 or 33%)
- Second value: Win rate with switching (should be ~0.67 or 67%)

### Main Execution Block

```python
if __name__ == "__main__":
    num_games = 10000
    win_without_switching, win_with_switching = simulate_monty_hall(num_games)
    print(f"Win rate without switching: {win_without_switching:.2%}")
    print(f"Win rate with switching: {win_with_switching:.2%}")
```

This runs the simulation with **10,000 games** and prints the results formatted as percentages.

---

## Example Output

```
Win rate without switching: 33.45%
Win rate with switching: 66.55%
```

The exact percentages will vary slightly each run due to randomness, but they should hover around 33% and 67%.

---

## Key Insights

1. **Empirical Verification**: This code proves the mathematical theory through simulation—a powerful way to understand probability
2. **Law of Large Numbers**: With 10,000 games, the results converge to the theoretical probabilities
3. **Why Switching Works**: When you switch, you win unless your initial choice was the car (1/3 chance). Without switching, you only win if your initial choice was correct (1/3 chance)

---

## How to Run

```bash
python test.py
```

## Customization

To run a different number of simulations, edit this line:
```python
num_games = 10000  # Change this number
```

Larger numbers = more accurate results but slower execution
Smaller numbers = faster but more variation

---

## Files in This Project

- **test.py**: Main simulation code (this file)
- **docs/TEST_DOCUMENTATION.md**: This documentation file

---

## Learning Outcomes

After reviewing this project, you should understand:
- ✅ What the Monty Hall Problem is
- ✅ Why switching is statistically advantageous
- ✅ How to use Monte Carlo simulations for probability verification
- ✅ How randomization and statistics can counter human intuition
