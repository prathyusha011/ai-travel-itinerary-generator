import google.generativeai as genai

genai.configure(api_key="AIzaSyCAohI4q08PnOt6tVoxc3Y3SDWWomNPs0Q")

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(m.name)
