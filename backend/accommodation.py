# backend/accommodation.py
from backend.planner_state import PlannerState

def suggest_accommodation(state: PlannerState) -> str:
    trip_type = state.get("trip_type", "").lower()
    budget_level = state.get("budget_level", "budget").lower()

    accommodation_suggestions = {
        "solo": {
            "budget": "Budget hostels with private rooms, affordable boutique hotels.",
            "mid-range": "Mid-range hotels with good amenities and privacy.",
            "luxury": "Luxury boutique hotels with privacy, great reviews, and top-notch amenities."
        },
        "friends": {
            "budget": "Hostels with shared dorm rooms, affordable group accommodations.",
            "mid-range": "Affordable hotels with group-friendly amenities and common areas.",
            "luxury": "Luxury hotels with large common areas, ideal for group hangouts and social activities."
        },
        "family": {
            "budget": "Budget-friendly family rooms in hostels, family guesthouses.",
            "mid-range": "Hotels with family suites and kid-friendly activities.",
            "luxury": "Luxury hotels with family suites, kids' clubs, and recreational facilities."
        }
    }

    accommodation = f"Accommodation suggestions based on your trip type '{trip_type}' and budget '{budget_level}': "

    if "friends" in trip_type:
        accommodation += accommodation_suggestions["friends"].get(budget_level, "No accommodation suggestions available.")
    elif "couple" in trip_type:
        accommodation += "Intimate hotels, boutique stays, or romantic getaways."
    elif "family" in trip_type:
        accommodation += accommodation_suggestions["family"].get(budget_level, "No accommodation suggestions available.")
    elif "solo" in trip_type:
        accommodation += accommodation_suggestions["solo"].get(budget_level, "No accommodation suggestions available.")
    else:
        accommodation += "Custom group type. Please refine your input for better suggestions."

    return accommodation
