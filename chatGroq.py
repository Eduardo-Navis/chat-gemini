# install the groq package with command: pip install groq
# Install dotenv package with command: pip install python-dotenv

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
        "content": "Conte até 10 curiosidades sobre o Brasil, em português, de forma resumida e objetiva."
      }
    ],
    temperature=1, #0 é o menos criativo, 2 é o mais
    max_completion_tokens=2048, ##Limita o tamanho da resposta
    top_p=1, #Controla a diversidade da resposta, 0.1 é mais conservador, 1 é mais criativo
    frequency_penalty=0, #Controla a repetição de palavras, 0 é o mais permissivo, 2 é o mais restritivo
    reasoning_effort="medium", #Controla o esforço de raciocínio, "low", "medium", "high"
    stream=True, #Permite que a resposta seja transmitida em tempo real, em vez de esperar até que toda a resposta seja gerada
    stop=None #Controla quando a resposta deve parar, None significa que não há limite de parada
) # Envia uma requisição para gerar uma resposta baseada nas configurações fornecidas dentro dos parênteses.

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
    #O uso de or "" garante que não ocorra um erro se o pacote vier vazio, e o argumento end="" impede a quebra de linha padrão do comando print. 
    #O resultado disso na tela é um efeito fluido e contínuo, como se as palavras estivessem sendo digitadas em tempo real.