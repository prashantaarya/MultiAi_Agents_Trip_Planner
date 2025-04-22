# backend/workflow.py
from backend.planner_state import PlannerState
from backend.input_handlers import input_city, input_interest, input_days, input_budget, input_trip_type
from backend.itinerary_generator import generate_multi_day_itinerary

class StateGraph:
    def __init__(self, initial_state: PlannerState):
        self.state = initial_state

    def add_node(self, node_name, node_function):
        pass

    def set_entry_point(self, node_name):
        pass

    def add_edge(self, from_node, to_node):
        pass

    def compile(self):
        pass
