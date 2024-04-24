import google.generativeai as genai
import os


while True:
    api_key = os.environ["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    break

model = genai.GenerativeModel('gemini-pro')

def journalize():
    with open(rf"Data/record.dat", "r", encoding="utf-8") as f:
        conversation = f.read()

    prompt  = f"Rewrite the following conversation as a long journal entry of me talking to my diary. Do not mention about the conversation. Keep the language casually balanced. Interpret each line. Ignore whatever the Diary is saying. Do not make up any detail beyond what is written below:\n{conversation}"
    
    journal = model.generate_content(prompt).text

    return journal

