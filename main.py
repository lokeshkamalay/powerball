import random
import streamlit as st

def generate_powerball_numbers():
    white_balls = random.sample(range(1, 70), 5)
    red_ball = random.randint(1, 26)
    return white_balls, red_ball

st.title("🎯 Powerball Number Generator")

if st.button("Generate Numbers"):
    white_balls, red_ball = generate_powerball_numbers()
    st.write("### Your Powerball Numbers:")
    st.write(f"White Balls: {white_balls}")
    st.write(f"Red Powerball: {red_ball}")
