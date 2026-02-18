import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_itinerary(destination, days, nights):
    model = genai.GenerativeModel("models/gemini-flash-latest")

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"Write a travel itinerary to {destination} for {days} days and {nights} nights"
                ],
            }
        ]
    )

    response = chat_session.send_message(
        f"Create a detailed day-wise travel itinerary for {destination} "
        f"for {days} days and {nights} nights. Include places, food, and tips.",
        request_options={"timeout": 30}
    )

    return response.text

def main():
    st.title("Travel Itinerary Generator")
    destination = st.text_input("Enter your desired destination:")
    days = st.number_input("Enter the number of days:", min_value=1)
    nights = st.number_input("Enter the number of nights:", min_value=0)
    if st.button("Generate Itinerary"):
        if destination.strip() and days > 0 and nights >= 0:

            with st.spinner("Generating itinerary..."):
                itinerary = generate_itinerary(destination, days, nights)

            st.text_area(
                "Generated Itinerary:",
                value=itinerary,
                height=300
            )

        else:
            st.error("Please make sure all inputs are provided and valid.")

if __name__ == "__main__":
    main()
