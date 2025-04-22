# frontend/app.py
import streamlit as st
from backend.input_handlers import input_city, input_interest, input_days, input_budget, input_trip_type
from backend.itinerary_generator import generate_multi_day_itinerary
from backend.planner_state import PlannerState

# Initialize state
state = PlannerState(
    messages=[],
    city="",
    interest=[],
    itinerary="",
    num_days=0,
    budget_level="",
    trip_type=""
)

def display_messages(messages):
    for message in messages:
        st.write(message.content)

def get_user_input():
    state["city"] = st.text_input("🏙️ Enter the city you want to visit:")
    state["interest"] = st.text_input("🎯 Enter your interests (comma-separated):").split(",")
    state["num_days"] = st.number_input("🗓️ How many days will your trip be?", min_value=1, max_value=30)
    state["budget_level"] = st.selectbox("💰 What is your budget?", options=["budget", "mid-range", "luxury"])
    state["trip_type"] = st.text_input("👫 Please describe your group type (e.g., 'We are 3 friends', 'A couple', etc.):")
    
    if st.button("Generate Itinerary"):
        # Generate the itinerary based on inputs
        updated_state = generate_multi_day_itinerary(state)
        st.write(updated_state["itinerary"])

# Display the interface
st.title("Travel Planner")
display_messages(state['messages'])
get_user_input()
