<h1 align="center">
  ⚡ KALKI ⚔️ — Your Cybersecurity AI Assistant
</h1>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&center=true&vCenter=true&width=435&lines=KALKI+AI+Cybersecurity+Assistant;Builds+Tools+from+Voice+Commands;Web+Dev+%7C+Code+%7C+AI+%7C+Scanner;OpenAI+%2B+Python+%2B+Nmap+%2B+Shodan" alt="Typing SVG" />
</p>



---

## 📖 What is Kalki?

> **Kalki** is an advanced, AI-powered cybersecurity virtual assistant that talks to you, understands your voice, helps with security testing, builds code, fixes tools, and even talks back using human-like voice. 🧠🎤💻

It’s designed to help developers, cybersecurity analysts, and ethical hackers automate tasks by just **speaking**.

---

## ⚙️ What Can Kalki Do?

| 🎯 Feature | ✅ Description |
|-----------|----------------|
| 🔐 Cybersecurity Tools | Explains and runs tools like Nmap, Metasploit, Burp Suite, etc. |
| 🦠 CVE & Vulnerability Info | Explains top vulnerabilities like SQLi, XSS, and more |
| 🧠 AI Chat | Uses OpenAI to answer technical queries smartly |
| 🧑‍💻 Code Generation | Creates Python, Java, HTML/CSS/JS, C, and C++ code from voice prompts |
| 🔧 Tool Repair | Repairs/rewrites broken code/tools based on your voice description |
| 🌐 Network Scans | DNS Lookup, IP resolver, port scanning using Nmap |
| 📊 GUI Reports | Visualizes scan reports using Streamlit or GUI modules |
| 💬 Hindi + English | Understands and replies in both Hindi and English |
| 🧵 Discord Integration | Sends alerts, scans, or logs to your Discord server |
| 🔍 Shodan, VirusTotal, OTX | Integrates with top threat intelligence APIs |
| 🔄 Realtime Logs | Keeps logs of activity with timestamps |
| 📁 Auto Save | Saves generated code in files with proper naming |

---

## 🛠 Tech Stack

- 🧠 OpenAI GPT-4
- 🎤 SpeechRecognition
- 🔊 pyttsx3 + gTTS
- 🌐 Nmap (via `os.system`)
- 🧰 Python subprocess
- 🧪 Streamlit (for GUI reports)
- 📡 Shodan API, VirusTotal API, OTX AlienVault API
- 📦 Discord Webhooks

---

## 🖥 Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/AkarshYash/Kalki-My-Cyber-Virtual-Assistant.git
cd Kalki-My-Cyber-Virtual-Assistant

# 2. Create virtual env (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Set your API keys
# Replace 'your-openai-key' and others in kalki.py

# 5. Run it!
python Kalki.py



