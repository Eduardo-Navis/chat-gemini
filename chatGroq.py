# install the groq package with command: pip install groq
import sys
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
sys.stdout.reconfigure(encoding="utf-8")

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
      {
        "role": "user",
        "content": "Qual modelo é você? Consegue reconhecer em qual ambiente está sendo executado? Se sim, descreva o ambiente e o modelo que você é. Responda em português"
      }
    ],
    temperature=1, #0 é o menos criativo, 2 é o mais
    max_completion_tokens=2048,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")