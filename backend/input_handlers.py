# backend/input_handlers.py
from backend.validation import get_valid_input
from backend.planner_state import PlannerState
from langchain_core.messages import HumanMessage

def input_city(state: PlannerState) -> PlannerState:
    city = get_valid_input("Please enter the city you want to visit for your day trip: ")
    return {**state, "city": city, "messages": state['messages'] + [HumanMessage(content=city)]}

def input_interest(state: PlannerState) -> PlannerState:
    interests = get_valid_input(f"Please enter your interests for the trip to {state['city']} (comma-separated): ")
    return {**state, "interest": [interest.strip() for interest in interests.split(",")], "messages": state['messages'] + [HumanMessage(content=interests)]}

def input_days(state: PlannerState) -> PlannerState:
    num_days = get_valid_input("📅 How many days is your trip? ", input_type="int")
    return {**state, "num_days": num_days, "messages": state['messages'] + [HumanMessage(content=f"Trip duration: {num_days} days")]}

def input_budget(state: PlannerState) -> PlannerState:
    budget_level = get_valid_input("💰 Choose your budget (Budget, Mid-range, Luxury): ", valid_choices=["budget", "mid-range", "luxury"])
    return {**state, "budget_level": budget_level, "messages": state['messages'] + [HumanMessage(content=f"Budget preference: {budget_level}")]}

def input_trip_type(state: PlannerState) -> PlannerState:
    trip_type = get_valid_input("👫 Please describe your group type (e.g., 'We are 3 friends', 'A couple', 'A family of 4'): ")
    return {**state, "trip_type": trip_type, "messages": state['messages'] + [HumanMessage(content=f"Trip type: {trip_type}")]}
