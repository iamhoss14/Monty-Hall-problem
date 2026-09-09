import streamlit as st
import pandas as pd
import random

# --- 1. Your Core Logic ---
def monty_hall(switch_doors):
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    initial_choice = random.choice(range(3))

    if switch_doors:
        doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        door_revealed = random.choice(doors_revealed)
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice
    return doors[final_choice] == 'car'

def simulate_monty_hall(num_games):
    num_win_without_switching = sum(monty_hall(False) for _ in range(num_games))
    num_win_with_switching = sum(monty_hall(True) for _ in range(num_games))
    return num_win_without_switching / num_games, num_win_with_switching / num_games

# --- 2. Streamlit UI Elements ---
st.title("🚪 Monty Hall Simulator")
st.write("Test the famous probability puzzle! Should you switch your door after the host reveals a goat?")

# User input for number of games
num_games = st.number_input(
    "How many games should we simulate?", 
    min_value=100, 
    max_value=100000, 
    value=10000, 
    step=500
)

# Button to trigger the simulation
if st.button("Run Simulation"):
    with st.spinner(f"Simulating {num_games} games..."):
        # Run your math
        win_without, win_with = simulate_monty_hall(num_games)
        
        # Display the results in large metric cards
        col1, col2 = st.columns(2)
        col1.metric("Win Rate (Stay)", f"{win_without:.2%}")
        col2.metric("Win Rate (Switch)", f"{win_with:.2%}")
        
        # Create a simple bar chart to visualize the difference
        st.subheader("Results Visualization")
        chart_data = pd.DataFrame(
            {
                "Strategy": ["Stay (No Switch)", "Switch Doors"],
                "Win Rate": [win_without, win_with]
            }
        ).set_index("Strategy")
        
        st.bar_chart(chart_data)