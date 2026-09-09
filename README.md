# 🚪 Monty Hall Simulator Dashboard

A Python-based interactive dashboard built with Streamlit to simulate the famous **Monty Hall Problem**. This project proves computationally whether it is better to stick with your original door or switch doors after a goat is revealed.

## 🧠 The Monty Hall Problem Explained
Suppose you're on a game show, and you're given the choice of three doors: 
* Behind one door is a **car** 🚗
* Behind the others, **goats** 🐐

You pick a door (say No. 1), and the host, who knows what's behind the doors, opens another door (say No. 3), which has a goat. He then says to you, "Do you want to pick door No. 2?" 

**Is it to your advantage to switch your choice?** 
Math and probability say **YES**. Sticking with your original door gives you a 1/3 (33.3%) chance of winning. Switching doors doubles your odds to 2/3 (66.6%). This simulator runs thousands of games instantly to prove it!

## 🚀 Features
* **Interactive UI:** Choose exactly how many games you want to simulate (from 100 up to 100,000).
* **Live Calculations:** The backend Python script randomizes the doors and simulates the game logic on the fly.
* **Data Visualization:** Instantly see the win rates compared side-by-side using Streamlit's built-in metric cards and bar charts.

## 🛠️ Installation & Setup

1. **Prerequisites:** Ensure you have Python installed on your computer.
2. **Install Dependencies:** Open your terminal and install the required libraries:
   ```bash
   pip install streamlit pandas