# backend/itinerary_generator.py
from backend.planner_state import PlannerState
from langchain_groq import ChatGroq
from backend.accommodation import suggest_accommodation
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    temperature=0,
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile"
)

itinerary_prompt = ChatPromptTemplate.from_messages([
   ("system", """
    You are a highly knowledgeable and friendly travel assistant. Your job is to create a personalized, detailed, and engaging itinerary for a trip to {city}, considering the user's preferences. 
    The trip will last {num_days} days, and the user has a {budget_level} budget. The user is traveling as a {trip_type}.
    
    For each day of the trip, provide:
    - A list of recommended activities that match the user's interests: {interests}.
    - Suggestions for restaurants, local eateries, or street food that fit within the budget level.
    - Optional hidden gems or off-the-beaten-path places for each day to make the trip more unique.
    - A balance of cultural, historical, natural, and recreational activities.
    - Tips on transportation (e.g., how to get to key spots efficiently), safety, and local customs to make the trip more enjoyable and stress-free.
    
    Tailor the recommendations to ensure they are relevant to the user's trip type and interests. 
    Include any practical tips, local recommendations, and fun facts that will enhance the experience. 
    Be sure to keep the tone friendly, fun, and conversational, yet informative. 
    Additionally, ensure that each day has a good balance between activities and rest to prevent the itinerary from feeling overwhelming.
"""),

    ("human", "Create an itinerary for my trip to {city}."),
])


def generate_multi_day_itinerary(state: PlannerState) -> PlannerState:
    response = llm.invoke(itinerary_prompt.format_messages(
        city=state['city'],
        interests=", ".join(state['interest']),
        num_days=state['num_days'],
        budget_level=state['budget_level'],
        trip_type=state['trip_type']
    ))

    accommodation = suggest_accommodation(state)  # Get accommodation suggestions
    print("\n📍 **Generated Itinerary with Accommodation Suggestions:**\n")
    print(response.content)
    print("\n🏨 **Accommodation Suggestions:**")
    print(accommodation)

    return {
        **state,
        "messages": state['messages'] + [AIMessage(content=response.content + "\n" + accommodation)],
        "itinerary": response.content + "\n" + accommodation,
    }
