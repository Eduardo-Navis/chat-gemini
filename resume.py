from emails import corpos_emails
from chat import chat
import emails


def recebeLista(text_emails):
    emails = ""

    for i, email in enumerate(text_emails):
        emails += f"\nE-mail {i + 1}:\n{email}\n"

    send = chat.send_message(
        f"""
        Resuma cada um dos e-mails abaixo em uma sentença sucinta, três palavras.
        Mantenha a numeração dos e-mails.

        {emails}
        """
    )

    print(send.text)

if __name__ == "__main__":
    recebeLista(corpos_emails)

with open("emails.txt", "w", encoding="utf-8") as file:
    for i, email in enumerate(corpos_emails):
        file.write(f"E-mail {i + 1}:\n{email}\n\n") 


nova_lista = []

with open("Lista-de-resumos.txt", "r", encoding="utf-8") as arquivo:
  for line in emails.txt:
    nova_lista.append(line.strip())
