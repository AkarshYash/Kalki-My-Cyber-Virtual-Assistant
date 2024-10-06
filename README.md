
Kalki: My Cybersecurity Assistant

Kalki is a voice-activated cybersecurity assistant that can assist users in various cybersecurity-related tasks such as explaining vulnerabilities, suggesting tools, performing basic network tests, and more. The assistant is designed to interact using both English and Hindi languages, with speech recognition and text-to-speech capabilities.

Table of Contents
- Introduction
- Features
- Requirements
- Installation
- Usage
  - Commands
  - Languages Supported
- Customization
- Future Improvements
- License

Introduction

Kalki is a speech-driven assistant that leverages Python libraries such as `speech_recognition`, `pyttsx3`, `gTTS`, and OpenAI's API to provide information on cybersecurity tools, vulnerabilities, and tips. It is capable of recognizing voice commands in English and Hindi, querying the OpenAI API for responses, and performing actions like running a basic `nmap` scan.

Features

- Speech Recognition: Kalki can listen to voice commands in both English and Hindi.
- Text-to-Speech: Responses are spoken aloud in the specified language.
- Cybersecurity Tool Descriptions: Provides descriptions of popular tools like Nmap, Metasploit, Burp Suite, and Wireshark.
- Vulnerability Information: Explains common vulnerabilities such as SQL Injection and Cross-Site Scripting (XSS).
- Basic Network Scanning: Can run basic `nmap` scans as part of the demo.
- Cybersecurity Tips: Recites a random cybersecurity tip to improve the user's security awareness.
- OpenAI Integration: Queries OpenAI for additional answers related to cybersecurity or other topics.

Requirements

The following Python libraries are required for Kalki to function:

- `speech_recognition`: For listening to voice commands.
- `pyttsx3`: For English text-to-speech (TTS) functionality.
- `gTTS`: For Hindi text-to-speech functionality.
- `openai`: To integrate with OpenAI for generating responses.
- `os`: To execute system commands and manage file system interactions.
- `random`: To generate random cybersecurity tips.

Additionally, you'll need:
- OpenAI API Key: Replace the placeholder in the code (`openai.api_key`) with your actual API key.
- mpg321: Required for playing `.mp3` files when using Hindi TTS (can be installed using a package manager like `apt` on Linux).

Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Kalki-Cybersecurity-Assistant.git
   cd Kalki-Cybersecurity-Assistant
   ```

2. Install the required Python packages:
   ```bash
   pip install speechrecognition pyttsx3 gtts openai
   ```

3. Install additional dependencies:
   For playing audio files (Hindi TTS):
   ```bash
   sudo apt install mpg321
   ```

4. Set up OpenAI API Key:
   Open the script file and replace `openai.api_key = 'your-api-key'` with your actual OpenAI API key.

Usage

To run Kalki, execute the Python script:

```bash
python kalki_cybersecurity_assistant.py
```

Commands

Here are some example commands you can give to Kalki:

- Help Command:
  - Help me with cybersecurity tools
  - Help me understand vulnerabilities
  
- Tool Information:
  - Tell me about Nmap
  - What is Metasploit?
  
- Vulnerability Information:
  - Explain SQL Injection
  - What is Cross-Site Scripting?

- Run a Basic Nmap Scan:
  - Run Nmap on my network

- Cybersecurity Tips:
  - The assistant will automatically provide random tips on starting.

Languages Supported

Kalki supports two languages:
- English: Default language.
- Hindi: To switch to Hindi, say "Hindi" or "हिंदी" when prompted.

Commands are processed in the language you choose, and responses are provided accordingly.

Exiting the Program

To exit the program, you can use any of the following commands:
- exit
- goodbye
- stop
- alvida

Customization

You can easily expand the functionality of Kalki by adding more cybersecurity tools or vulnerabilities to the existing lists in the script. Here's how:

1. Adding Tools:
   Open the script and modify the `cyber_security_tools` dictionary:
   ```python
   cyber_security_tools = {
       "nmap": "Nmap is a network scanning tool...",
       "new_tool": "Description of the new tool..."
   }
   ```

2. Adding Vulnerabilities:
   Similarly, you can add more vulnerabilities to the `vulnerabilities` dictionary:
   ```python
   vulnerabilities = {
       "sql injection": "SQL injection is...",
       "new_vulnerability": "Description of the new vulnerability..."
   }
   ```

3. Customizing Commands:
   Add more functionality by modifying the `process_command()` function to include new actions based on user commands.

Future Improvements

Some future improvements that can be added:
- Advanced Scanning: Integrating more advanced security tools (e.g., running Metasploit modules or OWASP ZAP).
- Natural Language Processing: Enhance command recognition to support more natural queries and follow-up questions.
- Machine Learning Models: Integrate local machine learning models for offline use or expand response generation with cybersecurity-specific models.
- Interactive Reports: Generate more detailed vulnerability reports or logs based on network scans.

License

This project is licensed under the MIT License. Feel free to use, modify, and distribute as per the terms of the license.

