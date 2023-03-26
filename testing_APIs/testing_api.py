import openai
import random
import re

# Set up OpenAI API key
openai.api_key = "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"  # Replace with your OpenAI API key


# Function to generate names using OpenAI's GPT-3
def generate_name(prompt, model, temperature=0.5, max_tokens=50):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        timeout=15,
        )
    name = response.choices[0].text.strip()
    # Clean up the name and remove any unwanted characters
    name = re.sub('[^a-zA-Z0-9 \n]', '', name)
    name = ''.join(random.choice([i.upper(), i]) for i in name)
    name= name.upper()
    return name


# Define the genre and motive for the name

genre=input("Enter the genre of the name: ")
motive=input("Enter the motive of the name: ")
extras=input("Extra information: ")

prompt = f"Generate a {genre} name that is {motive} which is also a {extras}. Generate {10} names."
model = "text-davinci-002"

name = generate_name(prompt, model)

print(name)
