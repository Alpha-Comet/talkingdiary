import pyperclip as pc
import os

API = pc.paste()
os.environ['GEMINI_API_KEY'] = API
