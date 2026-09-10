"""
MONTY HALL PROBLEM - INTERACTIVE STREAMLIT WEB APPLICATION
==========================================================

This is an interactive web application built with Streamlit that simulates the famous 
Monty Hall problem. Users can:

1. Adjust the number of simulations they want to run
2. Click a button to execute the simulation
3. See results displayed as metrics and a bar chart visualization

THE MONTY HALL PROBLEM:
- You're on a game show with 3 doors
- 1 door has a car (prize), 2 doors have goats
- You pick a door
- The host reveals a goat behind one of the other doors
- You can either STAY with your choice or SWITCH to the remaining door
- Question: Which strategy wins more often?

THE ANSWER: Switching gives you a 2/3 chance, staying gives 1/3 chance!

HOW TO RUN THIS APP:
- Terminal: streamlit run app.py
- Browser opens automatically to http://localhost:8501

DEPENDENCIES:
- streamlit (pip install streamlit)
- pandas (pip install pandas)
- random (built-in Python module)
"""

import streamlit as st
import pandas as pd
import random


# --- SECTION 1: CORE SIMULATION LOGIC ---

def monty_hall(switch_doors):
    """
    Simulates a single game of the Monty Hall problem.
    
    This function models one round of the game:
    - Randomly arranges 2 goats and 1 car behind 3 doors
    - Player makes an initial choice
    - Host (Monty) reveals a goat door
    - Player either switches or stays based on the parameter
    - Returns whether the player won the car
    
    PARAMETERS:
    -----------
    switch_doors (bool): 
        - True: Player switches to the unrevealed door after the host reveals a goat
        - False: Player sticks with their initial choice
    
    RETURNS:
    --------
    bool: True if player wins the car, False if player wins a goat
    
    STEP-BY-STEP PROCESS:
    ---------------------
    1. doors = ['goat', 'goat', 'car']
       → Create the setup with 2 goats and 1 car
    
    2. random.shuffle(doors)
       → Randomly shuffle the door contents
       → Example after shuffle: ['car', 'goat', 'goat']
    
    3. initial_choice = random.choice(range(3))
       → Player randomly picks a door (0, 1, or 2)
       → Example: initial_choice = 0 (picks the door with 'car')
    
    4. IF switch_doors == True:
       a. doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
          → Find all doors that are:
            - NOT the player's initial choice
            - Do NOT contain the car
          → These are the possible goat doors Monty can reveal
          → Example: if initial_choice=0 and doors=['car', 'goat', 'goat']
                     doors_revealed = [1, 2] (both are goats)
       
       b. door_revealed = random.choice(doors_revealed)
          → Monty randomly picks one of the goat doors to reveal
          → Example: door_revealed = 1
       
       c. final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
          → Player switches to the remaining door
          → This door is not their initial choice and not the revealed door
          → Example: final_choice = 2 (the only other door)
    
    5. ELSE (switch_doors == False):
       → Player sticks with their initial choice
       → final_choice = initial_choice
    
    6. return doors[final_choice] == 'car'
       → Return True if final choice has car, False if it has goat
    
    EXAMPLE 1 - STAYING (NOT switching):
    -------------------------------------
    Scenario: Player picks door 0, which has a car
    >>> random.seed(42)
    >>> monty_hall(False)  # Player doesn't switch
    True  # Player wins because they initially picked the car
    
    EXAMPLE 2 - SWITCHING:
    ----------------------
    Scenario: Player picks door 0 (has goat), Monty reveals door 1 (has goat)
    >>> random.seed(42)
    >>> monty_hall(True)  # Player switches
    True  # Player wins because switching gets them the car!
    
    EXAMPLE 3 - MULTIPLE GAMES:
    ----------------------------
    >>> results_switch = [monty_hall(True) for _ in range(100)]
    >>> win_rate_switch = sum(results_switch) / 100
    >>> print(f"Switch win rate: {win_rate_switch:.1%}")
    Switch win rate: 66.0%  # Approximately 2/3 as expected
    
    >>> results_stay = [monty_hall(False) for _ in range(100)]
    >>> win_rate_stay = sum(results_stay) / 100
    >>> print(f"Stay win rate: {win_rate_stay:.1%}")
    Stay win rate: 33.0%  # Approximately 1/3 as expected
    """
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
    """
    Runs multiple simulations of the Monty Hall problem to calculate win rates.
    
    This function performs a batch of games and returns statistical results
    showing how often each strategy (stay vs switch) wins.
    
    PARAMETERS:
    -----------
    num_games (int): Number of games to simulate
                     - Higher numbers give more accurate results
                     - Recommended: 1000-100000 for good accuracy
    
    RETURNS:
    --------
    tuple: (win_rate_without_switching, win_rate_with_switching)
           - Each value is a float between 0 and 1
           - Represents the probability of winning with that strategy
           - Example return: (0.3345, 0.6689)
    
    HOW IT WORKS:
    --------------
    1. num_win_without_switching = sum(monty_hall(False) for _ in range(num_games))
       → Runs num_games simulations where player STAYS
       → Counts how many games were won (True values)
       → Sums all the True values (True = 1, False = 0)
       → Example: If 3334 out of 10000 games won: sum = 3334
    
    2. num_win_with_switching = sum(monty_hall(True) for _ in range(num_games))
       → Runs num_games simulations where player SWITCHES
       → Counts how many games were won
       → Example: If 6666 out of 10000 games won: sum = 6666
    
    3. Return both values divided by num_games to get rates
       → win_without_switching = 3334 / 10000 = 0.3334 (33.34%)
       → win_with_switching = 6666 / 10000 = 0.6666 (66.66%)
    
    EXAMPLES:
    ---------
    EXAMPLE 1 - Small sample (100 games):
    >>> without_switch, with_switch = simulate_monty_hall(100)
    >>> print(f"Stay: {without_switch:.1%}, Switch: {with_switch:.1%}")
    # Output might be: Stay: 32.0%, Switch: 68.0%
    # (May vary more with smaller sample size)
    
    EXAMPLE 2 - Medium sample (10,000 games - production default):
    >>> without_switch, with_switch = simulate_monty_hall(10000)
    >>> print(f"Stay: {without_switch:.2%}, Switch: {with_switch:.2%}")
    # Output will be close to: Stay: 33.45%, Switch: 66.55%
    # (Very close to theoretical 1/3 and 2/3)
    
    EXAMPLE 3 - Large sample (100,000 games - maximum):
    >>> without_switch, with_switch = simulate_monty_hall(100000)
    >>> print(f"Stay: {without_switch:.3%}, Switch: {with_switch:.3%}")
    # Output will be very close to: Stay: 333.333%, Switch: 666.667%
    # (Nearly perfect match to theory due to large sample)
    
    WHY DOES SWITCHING WIN 2/3 OF THE TIME?
    ----------------------------------------
    Scenario 1 (1/3 probability): You initially picked the CAR
    - You have the prize already
    - Monty must reveal a goat door
    - If you switch: You give up the car and get a goat (LOSE)
    - If you stay: You keep the car (WIN)
    
    Scenario 2 (2/3 probability): You initially picked a GOAT
    - You don't have the prize
    - Monty reveals the OTHER goat door
    - If you switch: You get the car (WIN)
    - If you stay: You keep the goat (LOSE)
    
    Summary:
    - Switching wins in 2 out of 3 possible scenarios
    - Staying wins in 1 out of 3 possible scenarios
    - Therefore: Switching probability = 2/3, Staying probability = 1/3
    """
    num_win_without_switching = sum(monty_hall(False) for _ in range(num_games))
    num_win_with_switching = sum(monty_hall(True) for _ in range(num_games))
    return num_win_without_switching / num_games, num_win_with_switching / num_games


# --- SECTION 2: STREAMLIT USER INTERFACE ---

"""
STREAMLIT UI FLOW:
==================

The Streamlit framework creates an interactive web interface. Here's how it works:

1. st.title() - Creates the main title at the top of the page
2. st.write() - Displays explanatory text
3. st.number_input() - Creates an input box for the user to set number of games
4. st.button() - Creates a clickable button that triggers the simulation
5. st.spinner() - Shows a loading message while simulation runs
6. st.metric() - Displays key results in large, highlighted cards
7. st.columns() - Divides the page into columns for side-by-side display
8. st.bar_chart() - Creates a bar chart visualization of results
9. st.subheader() - Creates section headers

KEY CONCEPT: Streamlit runs the entire script from top to bottom every time
the user interacts with it. This allows for reactive, interactive applications.
"""

st.title("🚪 Monty Hall Simulator")
"""
TITLE DISPLAY:
==============
This creates a large, prominent title at the top of the web page.
The door emoji (🚪) makes it visually appealing and thematic.

What the user sees:
┌─────────────────────────────────────────────┐
│  🚪 Monty Hall Simulator                    │
└─────────────────────────────────────────────┘
"""

st.write("Test the famous probability puzzle! Should you switch your door after the host reveals a goat?")
"""
INTRODUCTORY TEXT:
==================
st.write() displays explanatory text to help users understand what the app does.

What the user sees:
"Test the famous probability puzzle! Should you switch your door after 
the host reveals a goat?"
"""

# User input for number of games
"""
USER INPUT SECTION:
===================
This section creates an interactive input box where users can specify
how many games they want to simulate.
"""
num_games = st.number_input(
    "How many games should we simulate?", 
    min_value=100,           # Minimum allowed value
    max_value=100000,        # Maximum allowed value
    value=10000,             # Default value
    step=500                 # Increment/decrement step size
)
"""
WHAT HAPPENS HERE:
- Creates a number input box labeled "How many games should we simulate?"
- Users can type a number or use +/- buttons
- Minimum: 100 games (to keep results meaningful)
- Maximum: 100000 games (to prevent extremely long runtimes)
- Default: 10000 games (good balance of accuracy and speed)
- Step: 500 (each +/- button click changes by 500)

EXAMPLE USER INTERACTIONS:
1. User sees: How many games should we simulate? [10000]
2. User clicks the + button 5 times
3. Value changes to: 12500 (10000 + 500*5)
4. App stores this in the variable: num_games = 12500
"""

# Button to trigger the simulation
"""
SIMULATION BUTTON:
==================
This creates a clickable button that triggers the entire simulation.
The if statement means: "only run this code block when the button is clicked"
"""
if st.button("Run Simulation"):
    """
    BUTTON BEHAVIOR:
    ================
    - When button is NOT clicked: Everything inside this block is skipped
    - When button IS clicked: This code block runs
    
    This prevents the app from running expensive simulations on every page load.
    It only simulates when the user explicitly clicks "Run Simulation".
    """
    
    with st.spinner(f"Simulating {num_games} games..."):
        """
        LOADING SPINNER:
        ================
        Shows a spinning animation with a message while the simulation runs.
        
        What the user sees:
        ⠙ Simulating 10000 games...
        
        This provides feedback that the app is working and hasn't frozen.
        """
        
        # Run the simulation
        win_without, win_with = simulate_monty_hall(num_games)
        """
        CALLING THE SIMULATION:
        =======================
        This calls the simulate_monty_hall() function with the user's chosen num_games.
        
        Returns:
        - win_without: Probability of winning if player STAYS (approximately 0.33)
        - win_with: Probability of winning if player SWITCHES (approximately 0.67)
        
        EXAMPLE EXECUTION:
        >>> win_without, win_with = simulate_monty_hall(10000)
        >>> win_without
        0.3312  # 33.12% win rate for staying
        >>> win_with
        0.6688  # 66.88% win rate for switching
        """
        
        # Display the results in large metric cards
        col1, col2 = st.columns(2)
        """
        CREATING SIDE-BY-SIDE COLUMNS:
        ==============================
        st.columns(2) divides the page width into 2 equal columns.
        - col1: Left column
        - col2: Right column
        
        This allows displaying results side-by-side for easy comparison.
        
        Visual layout:
        ┌─────────────────────┬─────────────────────┐
        │                     │                     │
        │      col1           │      col2           │
        │   (Stay Results)    │  (Switch Results)   │
        │                     │                     │
        └─────────────────────┴─────────────────────┘
        """
        
        col1.metric("Win Rate (Stay)", f"{win_without:.2%}")
        """
        LEFT COLUMN - STAY RESULTS:
        ==========================
        col1.metric() displays a large, highlighted metric card.
        
        Parameters:
        - Label: "Win Rate (Stay)" - describes what the number represents
        - Value: f"{win_without:.2%}" - formats the number as a percentage
                 .2% means: 2 decimal places and add % sign
                 Example: 0.3312 → "33.12%"
        
        What the user sees in LEFT COLUMN:
        ┌──────────────────────────┐
        │  Win Rate (Stay)         │
        │  33.12%                  │
        └──────────────────────────┘
        """
        
        col2.metric("Win Rate (Switch)", f"{win_with:.2%}")
        """
        RIGHT COLUMN - SWITCH RESULTS:
        =============================
        Same as col1 but for switching strategy.
        
        What the user sees in RIGHT COLUMN:
        ┌──────────────────────────┐
        │  Win Rate (Switch)       │
        │  66.88%                  │
        └──────────────────────────┘
        """
        
        # Create a visualization
        st.subheader("Results Visualization")
        """
        VISUALIZATION HEADER:
        ====================
        st.subheader() creates a smaller section heading.
        This separates the metrics from the chart below.
        
        What the user sees:
        ─────────────────────────────
        📊 Results Visualization
        ─────────────────────────────
        """
        
        chart_data = pd.DataFrame(
            {
                "Strategy": ["Stay (No Switch)", "Switch Doors"],
                "Win Rate": [win_without, win_with]
            }
        ).set_index("Strategy")
        """
        CREATING THE DATA FOR THE CHART:
        ================================
        
        Step 1: Create a dictionary with two columns
        {
            "Strategy": ["Stay (No Switch)", "Switch Doors"],
            "Win Rate": [0.3312, 0.6688]
        }
        
        Step 2: Convert to pandas DataFrame
        This creates a table structure:
        ┌──────────────────────┬────────────┐
        │ Strategy             │ Win Rate   │
        ├──────────────────────┼────────────┤
        │ Stay (No Switch)     │ 0.3312     │
        │ Switch Doors         │ 0.6688     │
        └──────────────────────┴────────────┘
        
        Step 3: .set_index("Strategy")
        Makes "Strategy" the row labels instead of a column:
        ┌──────────────────────┬────────────┐
        │                      │ Win Rate   │
        ├───────────��──────────┼────────────┤
        │ Stay (No Switch)     │ 0.3312     │
        │ Switch Doors         │ 0.6688     │
        └──────────────────────┴────────────┘
        """
        
        st.bar_chart(chart_data)
        """
        DISPLAYING THE BAR CHART:
        =========================
        st.bar_chart() takes the DataFrame and creates an interactive bar chart.
        
        What the user sees:
        
        Win Rate
        ▲
        1 │
          │
        0.75 │
          │
        0.5 │          ┌─────────┐
          │          │         │
        0.25 │  ┌──────┤         │
          │  │      │         │
        0 │  └──────┴─────────┘
          └───────────────────────────────
            Stay (No Switch)  Switch Doors
        
        KEY INSIGHTS FROM THE CHART:
        - The chart visually shows that switching wins more often
        - Makes the 2:1 probability ratio immediately obvious
        - Users can see: "Switching is twice as good as staying"
        
        EXAMPLE OUTPUT:
        ===============
        For num_games = 10000:
        - Stay bar height: ~0.33 (33%)
        - Switch bar height: ~0.67 (67%)
        
        For num_games = 100000:
        - Stay bar height: ~0.3333... (33.33%)
        - Switch bar height: ~0.6667... (66.67%)
        
        The larger the sample, the more accurate these will be.
        """
