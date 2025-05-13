# CyberOpsDaily

CyberOpsDaily is an automated platform that transforms cybersecurity headlines into structured, summarized, and translated articles in Spanish, aimed at technical audiences.  
It is designed to integrate with platforms like GetInSI for visibility, configuration auditing, and threat awareness.

---

## 🔧 Main Components

- 🛠 `setup.sh`: Installs dependencies and prepares your VPS for automated execution.
- 🧠 `generate_articles.py`: Fetches and processes news from `news.db`, generates `.md` files with security advice and contextual CTAs.
- 📁 `docs/`: Documentation for modules and roadmap.

---

## 🚀 Project Roadmap (Summary)

CyberOpsDaily is structured in clear development phases to support long-term scalability and integration with cybersecurity platforms like GetInSI.

| Phase | Description | Status |
|-------|-------------|--------|
| **1** | Initial VPS installer (`setup.sh`) for Python + repo automation | ✅ Done |
| **2** | Article Engine: translate, summarize, classify news into Markdown | ✅ Done |
| **3** | Auto-export to blog/newsletter (Markdown/Netlify CMS) | ⏳ In Progress |
| **4** | CMS / Notion sync for automated publishing | 🔜 Planned |
| **5** | AI/ML enhancements for relevance scoring and smart tagging | 🔜 Planned |

📄 See full roadmap in [`docs/roadmap.md`](docs/roadmap.md)

---

## 📦 Installation

```bash
git clone https://github.com/getinsi/cyberopsdaily-installer.git
cd cyberopsdaily-installer
chmod +x setup.sh
./setup.sh

