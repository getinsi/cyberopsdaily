# CyberOpsDaily – Project Roadmap

This document outlines the phased development of the CyberOpsDaily platform, from initial deployment to advanced automation and AI-driven content handling.

---

## ✅ Phase 1 – Installer Script

- [x] `setup.sh` created and hosted on GitHub (`cyberopsdaily-installer`)
- [x] Automates VPS setup: Python, pip, virtualenv, repo cloning
- [x] Prompts for OpenAI API key
- [x] Creates necessary folders (`articles/`, `logs/`, etc.)

---

## ✅ Phase 2 – Article Engine

- [x] Script `generate_articles.py` fetches latest headlines from `news.db`
- [x] Uses OpenAI GPT to translate and summarize in Spanish
- [x] Applies classification logic:
  - 🔐 `GetInSI Shield` for CVEs, firewalls, Cisco
  - 📊 `GetInSI Observe` for monitoring/log-related topics
  - 🧩 General `GetInSI` fallback
- [x] Outputs `.md` with structured summaries and CTA
- [x] Documented in `docs/article_engine.md`

---

## ⏳ Phase 3 – Blog & Newsletter Output

- [ ] Auto-export `.md` to blog system (Markdown-based or Netlify CMS)
- [ ] Optional: send `.md` as daily newsletter
- [ ] Option to tag posts for grouping by category

---

## 🔜 Phase 4 – Notion / CMS Sync

- [ ] Integrate with Notion via API (`notion-py`) to publish summaries
- [ ] Sync summaries to CMS (Ghost, Hugo, etc.)
- [ ] Optional UI for manual validation before publish

---

## 🔜 Phase 5 – AI/ML Enhancement

- [ ] Implement scoring or tagging model
- [ ] Use LLM or ML to detect relevance, assign urgency
- [ ] Build dashboard of trending terms or security topics

---

## 📌 Long-Term Goals

- Build public portal to explore archived summaries
- Integrate with GetInSI Shield blog strategy
- Add donation or sponsorship links to support free content generation