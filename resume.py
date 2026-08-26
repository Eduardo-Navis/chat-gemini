from emails import corpos_emails
from chat import chat


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