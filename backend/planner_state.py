# backend/planner_state.py
from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage, AIMessage

class PlannerState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]
    city: str
    interest: List[str]
    itinerary: str
    num_days: int
    budget_level: str
    trip_type: str
