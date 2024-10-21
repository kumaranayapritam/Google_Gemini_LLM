**Gemini LLM Streamlit Applications**

This repository contains two Streamlit applications that interact with Google's Gemini LLM API. One app handles text-based questions, while the other processes both text inputs and images to generate content using Gemini.

**Prerequisites**

Before running the applications, ensure you have the following installed:

Python 3.8 or above
Streamlit
python-dotenv for loading environment variables
Google's Generative AI Python library (google-generativeai)
PIL (Pillow) for handling images in app_image.py

**Setup**
1. Clone this repository.
2. Install the required dependencies:

**pip install streamlit python-dotenv google-generativeai Pillow**

3. Create a .env file in the root directory and set your Google API key:

**GOOGLE_API_KEY=your_google_api_key**

**Running the Applications**

**1. app.py - Text Q&A with Gemini LLM**

This app allows users to ask text-based questions, and it generates responses using the Gemini LLM model.

streamlit run app.py

**Features:**

1.  Input text field to ask a question.
2. On submission, it fetches a response from the Gemini model.
3. Displays the response in the UI.

**2. app_image.py - Image and prompt with Gemini LLM**

This app lets users upload an image and optionally provide text prompts. The Gemini LLM will generate content based on the input.

streamlit run app_image.py

**Features:**

1.  Input text field to provide a prompt (optional).
2. Image uploader to process images.
3. On submission, the app generates a response based on the image and optional text prompt.
4. Displays the image and response in the UI.
