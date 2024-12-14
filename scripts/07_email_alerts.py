import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# JSON data (replace this with reading from a file or other source if necessary)
data = [
    {"video_id":"ZQbWWOzvyfo","title":"Verizon","published_at":"2024-07-03T02:03:05Z","channel_title":"Verizon","category_id":28,"category_label":"Science & Technology","kids_safe_BERT":0,"profanity":False,"themes":False,"readability":False,"tone":False,"cultural_sensitivity":False,"kids_safe_content":False,"profanity_words":"na","themes_identified":"na","tone_score":"na","contains_cultural_sensitivity":False,"cultural_sensitivity_identified":[]},
    {"video_id":"u4gEBRSKi2E","title":"Is Being Fat A Choice? Fit Women vs Fat Women | Middle Ground","published_at":"2024-10-16T16:01:03Z","channel_title":"Jubilee","category_id":24,"category_label":"Entertainment","kids_safe_BERT":0,"profanity":True,"themes":True,"readability":False,"tone":True,"cultural_sensitivity":False,"kids_safe_content":False,"profanity_words":["suck","crap","hell","fat","god"],"themes_identified":["boyfriend","adult","kill","sex","lingerie","war","crap","hell","cult","fear","hot","die"],"tone_score":1.0,"contains_cultural_sensitivity":False,"cultural_sensitivity_identified":[]},
    {"video_id":"T5niXqwAnME","title":"Big Muscle Guy Scars RELEASED #health #muscles #knots","published_at":"2024-06-14T13:30:15Z","channel_title":"Mondragon Chiropractic","category_id":27,"category_label":"Education","kids_safe_BERT":0,"profanity":False,"themes":True,"readability":False,"tone":True,"cultural_sensitivity":False,"kids_safe_content":False,"profanity_words":"na","themes_identified":["war"],"tone_score":0.9136,"contains_cultural_sensitivity":False,"cultural_sensitivity_identified":[]},
    {"video_id":"yeSbUxW2M-4","title":"clips that made Kai Cenat famous","published_at":"2022-12-31T17:00:38Z","channel_title":"Kai Cenat Live","category_id":24,"category_label":"Entertainment","kids_safe_BERT":0,"profanity":True,"themes":True,"readability":False,"tone":True,"cultural_sensitivity":False,"kids_safe_content":False,"profanity_words":["hell","god","damn"],"themes_identified":["hell","fire","damn","hot","gun"],"tone_score":0.999,"contains_cultural_sensitivity":False,"cultural_sensitivity_identified":[]}
]

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "alertsystem583@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "********"  # Replace with your app password
RECIPIENT_EMAIL = "bhavana.devulapally.456@gmail.com"  # Replace with the recipient's email

# Check conditions and prepare alert content
alerts = []
for item in data:
    if item.get("profanity") or item.get("themes") or not item.get("tone") or item.get("cultural_sensitivity"):
        profanity_words = (", ".join(item["profanity_words"]) if isinstance(item["profanity_words"], list) else "None")
        themes_identified = (", ".join(item["themes_identified"]) if isinstance(item["themes_identified"], list) else "None")
        alerts.append(
            f"Youtube Video ID: {item['video_id']}\n"
            f"Title of the Video: {item['title']}\n"
            f"Channel: {item['channel_title']}\n"
            f"Profanity Words Used: {profanity_words}\n"
            f"Themes Identified: {themes_identified}\n\n"
        )

if alerts:
    # Compose the email
    subject = "Alert: Content Issues Detected"
    body = (
        "The following content has been identified as potentially unsuitable and irrelevant for children which has been watched by your child: \n\n"
        + "\n".join(alerts)
    )

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
else:
    print("No alerts triggered.")