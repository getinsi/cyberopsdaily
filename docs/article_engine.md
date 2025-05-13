# Article Engine – CyberOpsDaily

This module (`generate_articles.py`) automates the generation of cybersecurity articles in Spanish, designed for technical audiences. It extracts headlines from a SQLite database, summarizes content using OpenAI, and outputs Markdown files with brand-aware CTAs.

---

## 🧠 Purpose

- Convert raw news from `news.db` into high-quality Spanish summaries
- Add practical security advice
- Promote relevant tools (GetInSI, Shield, Observe) based on content

---

## ⚙️ Workflow

1. Connect to `data/news.db`
2. Retrieve the 5 latest news entries
3. For each entry:
   - Build a custom GPT prompt
   - Get translated + summarized response
   - Classify article content
   - Save `.md` in `/articles/` with CTA

---

## 🧩 Output Example

**Filename:**
```
2025-05-12-critical-cve-in-cisco.md
```

**Content:**
```markdown
# Critical CVE in Cisco ASA
**Date:** 2025-05-12  
**Source:** https://...

Resumen en español del CVE...

---

**Assess your configurations with GetInSI Shield:** [getinsi.com](https://getinsi.com)
```

---

## 🧠 Classification Logic

- `shield`: mentions keywords like firewall, CVE, Cisco, misconfiguration
- `observe`: mentions monitoring, visibility, logs, traffic
- `general`: fallback if no match

---

## 📦 Dependencies

- `openai`
- `python-dotenv`

Add them via:

```bash
pip install -r requirements.txt
```

---

## 🕒 Automation via Cron

Use this command on VPS (Ubuntu):

```bash
crontab -e
```

And add:

```bash
0 7 * * * /root/cyberopsdaily/venv/bin/python /root/cyberopsdaily/generate_articles.py >> /root/cyberopsdaily/logs/cronlog.txt 2>&1
```

---

## 📁 Location

Place this file in:

```
/docs/article_engine.md
```