import os
import gradio as gr
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.globals import set_debug, set_verbose

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

set_debug(True)
set_verbose(True)

# Initialize the ChatOpenAI model with your OpenAI API key
model = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4")

# Custom prompt templates for generating personalized travel itinerary
personalized_itinerary_template = ChatPromptTemplate.from_template("""
    Create a detailed, personalized travel itinerary for {name}, who is {age} years old and prefers {travel_style} travel. 
    They will be in Italy for {travel_duration} days, interested in {experiences} experiences and planning to explore {regions}, specifically {destinations}. 
    Their tour preference is {tour_type}, with a budget of {budget_range}. 

    The itinerary should include:
    - A warm introduction, acknowledging {name}'s travel preferences and any specific needs for traveling with children.
    - A detailed plan for each day, including specific activities aligned with their interest in {experiences}, suitable for both adults and children if applicable.
    - Suggestions for accommodations in each destination, with brief descriptions and URLs. Include Hotel Ponte Sisto in Rome, Ortigia Algilà Charme Hotel in Siracusa, and Hotel Maresca in Praiano.
    - Details on transfers between destinations, including private drivers and estimated times.

    Each day's activities should be laid out in a narrative style, starting from the morning until the evening, ensuring variety and engaging experiences. Avoid using bullet points or lists, instead, weave the details into a continuous text that guides {name} through their journey in Italy, day by day.
    
    Remember to include leisure days, suggesting how {name} might enjoy their time at leisure in places like the Amalfi coast, and detail any self-managed trips, such as a day trip to Capri. For travel between cities and regions, specify the mode of transport and provide an estimated duration for these transfers.
""")


output_parser = StrOutputParser()

def generate_personalized_itinerary(name, age, travel_duration, destinations, tour_type, budget_range, travel_style, experiences, regions):
    user_input = {
        "name": name,
        "age": age,
        "travel_duration": travel_duration,
        "destinations": destinations,
        "tour_type": tour_type,
        "budget_range": budget_range,
        "travel_style": travel_style,
        "experiences": experiences,
        "regions": regions
    }
    
    # Generate personalized travel itinerary
    personalized_itinerary = (personalized_itinerary_template | model | output_parser).invoke(user_input)
    
    return personalized_itinerary

# Setup Gradio Interface
inputs = [
    gr.Textbox(label="Name"),
    gr.Number(label="Age", step=1),
    gr.Slider(label="Travel Duration", minimum=1, maximum=30),
    gr.CheckboxGroup(label="Destinations in Italy", choices=["Rome", "Florence", "Venice", "Milan", "Naples"]),
    gr.Radio(label="Tour Type", choices=["Guided", "Self-guided"]),
    gr.Textbox(label="Budget Range"),
    gr.Radio(label="Travel Style", choices=["Luxury", "Economy", "Backpacking"]),
    gr.CheckboxGroup(label="Experiences", choices=["Cultural Visits", "Relaxing Moments", "Nature & Landscape"]),
    gr.CheckboxGroup(label="Regions of Italy you want to visit", choices=["Tuscany", "Lombardy", "Sicily", "Veneto"]),
]



demo = gr.Interface(
    fn=generate_personalized_itinerary,
    inputs=inputs,
    outputs="text",
    title="Personalized Travel Itinerary Generator",
    description="This tool generates a personalized travel itinerary based on your preferences."
)

if __name__ == "__main__":
    # If share=True, gradio will create a public link for your interface
    demo.launch(share=True)
