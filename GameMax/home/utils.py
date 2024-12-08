from mailjet_rest import Client

from GameMax import settings


def contact_form_message(name, last_name, email, subject, message):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "zdravkobg1321@students.softuni.bg",
                    "Name": "GAMEMAX"
                },
                "To": [
                    {
                        "Email": "zyq4ka@gmail.com",
                        "Name": "GameMax Boss"
                    }
                ],
                "Subject": f"Subject: {subject}",
                "TextPart": f"""
                    Name: {name} {last_name}
                    Email: {email}
                    Message:
                    {message}
                """,
                "HTMLPart": f"""
                    <h1>GAMEMAX SUPPORT TEAM</h1>
                    <p><strong>Name:</strong> {name} {last_name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Message:</strong></p>
                    <p>{message}</p>
                """,
                "ReplyTo": {
                    "Email": email,
                    "Name": f"{name} {last_name}"
                }
            }
        ]
    }

    result = mailjet.send.create(data=data)

    return result
