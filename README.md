AI Travel Itinerary Generator
Project Overview

AI Travel Itinerary Generator is a web-based application that automatically generates a structured, day-wise travel plan based on user inputs such as destination, number of days, and number of nights. The system integrates Google Gemini API to generate intelligent travel suggestions including places to visit, food recommendations, and travel tips.

Problem Statement

Planning a travel itinerary manually requires extensive research and time. Travelers often struggle to organize destinations, activities, and food options efficiently. This project aims to simplify and automate itinerary planning using Generative AI to provide structured travel plans instantly.

Solution

The application collects user inputs through a Streamlit interface and sends them to the Gemini API. The AI model processes the request and returns a detailed, day-wise itinerary. The generated output is displayed in a readable format within the application.

Tech Stack

Frontend

Streamlit

Backend

Python

AI Integration

Google Generative AI (Gemini API)

Environment & Deployment

python-dotenv

GitHub

Render / Streamlit Cloud

Architecture Flow

User Input → Streamlit Interface → Python Backend → Gemini API → Generated Itinerary → Display Output

Project Structure

ai-travel-itinerary-generator/
│
├── travel.py
├── check_models.py
├── requirements.txt
├── Documentation/
└── README.md

How to Run Locally

git clone https://github.com/prathyusha011/ai-travel-itinerary-generator

cd ai-travel-itinerary-generator
pip install -r requirements.txt
streamlit run travel.py

Environment Configuration

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here

Documentation

https://drive.google.com/file/d/1aB0q1qDVN_c11Gzyb8tnpnHZiSYKNOdC/view?usp=sharing

Demo Video

https://drive.google.com/file/d/1XRoTI-f47B9X7eD1vj6x2d6gHhjXFD4x/view?usp=sharing
