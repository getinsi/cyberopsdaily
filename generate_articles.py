import os
import sqlite3
import openai
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import re

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create output directory
Path("articles").mkdir(exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect("data/news.db")
cursor = conn.cursor()

# Get recent news
cursor.execute("SELECT fecha, titulo, link FROM news ORDER BY id DESC LIMIT 5")
news_items = cursor.fetchall()

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]', '', text).strip().replace(" ", "-")[:60]

def classify_article(text):
    text = text.lower()
    if any(kw in text for kw in ["firewall", "cisco", "cve", "misconfiguration", "vulnerability", "exploit"]):
        return "shield"
    elif any(kw in text for kw in ["monitoring", "visibility", "logs", "network traffic", "telemetry"]):
        return "observe"
    else:
        return "general"

# Process each news item
for item in news_items:
    date, title, link = item
    prompt = f"""Translate and summarize the following cybersecurity news article into Spanish for a technical audience.
Include a brief practical security recommendation at the end.
Finish with a call to action such as: 'Explore tools like GetInSI Shield to assess configurations.'

Title: {title}
Source: {link}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a cybersecurity and technical writing expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=700
        )
        summary = response["choices"][0]["message"]["content"]

        # Create .md file
        file_name = f"{date}-{clean_text(title)}.md"
        path = Path("articles") / file_name

        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n")
            f.write(f"**Date:** {date}\n")
            f.write(f"**Source:** {link}\n\n")
            f.write(summary.strip())
            f.write("\n\n---\n")

            category = classify_article(title + " " + summary)
            if category == "shield":
                f.write("**Assess your configurations with GetInSI Shield:** [getinsi.com](https://getinsi.com)\n")
            elif category == "observe":
                f.write("**Monitor and analyze your network with GetInSI Observe:** [getinsi.com](https://getinsi.com)\n")
            else:
                f.write("**Assess your configurations with:** [GetInSI](https://getinsi.com)\n")

        print(f"[✔] Article: {path.name}")

    except Exception as e:
        print(f"[✖] Error processing: {title}\n{e}")

conn.close()
