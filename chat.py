from dotenv import load_dotenv
from google import genai



load_dotenv()

client = genai.Client()

chat = client.chats.create(model="gemini-3.5-flash-lite")

if __name__ == "__main__":
  prompt = input("Digite sua pergunta: ")

  while prompt != "fim":
    respostaP = chat.send_message(prompt)
    print(respostaP.text)
    print("\n")
    prompt = input("Digite sua próxima pergunta: ")
    
