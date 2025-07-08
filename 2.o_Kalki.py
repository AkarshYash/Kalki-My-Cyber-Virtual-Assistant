import speech_recognition as sr
import pyttsx3
import openai
from gtts import gTTS
import os
import random
import datetime
import requests

# === Init Section ===
engine = pyttsx3.init()
openai.api_key = 'klzi_0kJmkHT79'

LOG_FILE = "alerts.log"

# === Knowledge Base ===
cyber_security_tools = {
    "nmap": "Nmap is a network scanning tool used to discover hosts and services on a computer network.",
    "metasploit": "Metasploit is a penetration testing framework for developing and executing exploit code against a remote target machine.",
    "wireshark": "Wireshark is a network protocol analyzer used to capture and interactively browse traffic running on a computer network.",
    "burp suite": "Burp Suite is an integrated platform for performing web application security testing."
}

vulnerabilities = {
    "sql injection": "SQL injection is a code injection technique that might destroy your database.",
    "xss": "Cross-site scripting (XSS) is a vulnerability that allows an attacker to inject malicious scripts into content delivered to users."
}

# === Helper Functions ===
def speak(text, language='en'):
    if language == 'hi':
        tts = gTTS(text=text, lang='hi')
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")
    else:
        engine.say(text)
        engine.runAndWait()

def listen(language='en'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening in {language}...")
        audio = recognizer.listen(source)
        try:
            if language == 'hi':
                command = recognizer.recognize_google(audio, language="hi-IN")
            else:
                command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, please repeat.", language)
            return listen(language)
        except sr.RequestError:
            speak("Connection error.", language)
            return None

def ask_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def log_event(event):
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{datetime.datetime.now()}] {event}\n")

# === Code Generator ===
def generate_code_tool(command, lang='en'):
    languages = ['python', 'java', 'c', 'c++', 'html', 'javascript']
    selected_lang = None
    for l in languages:
        if l in command:
            selected_lang = l
            break
    if not selected_lang:
        speak("Please specify a language.", lang)
        return

    speak(f"Okay! What should this {selected_lang} tool do?", lang)
    feature_command = listen(lang)
    if not feature_command:
        return

    prompt = f"Create a full working code file in {selected_lang} to do the following: {feature_command}. Include all necessary boilerplate."
    code = ask_openai(prompt)

    filename = f"tool_{selected_lang}_{random.randint(1000,9999)}.{('py' if selected_lang=='python' else 'html' if selected_lang=='html' else 'java' if selected_lang=='java' else 'cpp' if selected_lang=='c++' else 'c' if selected_lang=='c' else 'js')}"
    with open(filename, 'w') as f:
        f.write(code)

    speak(f"Your code is ready and saved as {filename}.", lang)
    log_event(f"Code tool generated in {selected_lang}: {filename} with features: {feature_command}")

# === Threat Intelligence ===
def get_shodan_data(ip):
    api_key = "YOUR_SHODAN_API_KEY"
    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        return f"{ip} is running {data.get('org', 'Unknown')} and has open ports: {[port['port'] for port in data.get('data', [])]}"
    except:
        return "Could not fetch Shodan data."

def get_virustotal_report(file_hash):
    api_key = "YOUR_VIRUSTOTAL_API_KEY"
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        malicious = data['data']['attributes']['last_analysis_stats']['malicious']
        return f"{malicious} engines flagged this file as malicious."
    return "Hash not found or error."

def get_otx_info(ip):
    api_key = "YOUR_OTX_API_KEY"
    url = f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general"
    headers = {'X-OTX-API-KEY': api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return f"Reputation: {data['reputation']} | Pulse Count: {len(data['pulse_info']['pulses'])}"
    return "OTX data not available."

# === Command Processor ===
def process_command(command, lang='en'):
    if 'code' in command or 'tool' in command:
        generate_code_tool(command, lang)

    elif 'shodan' in command:
        speak("Tell me the IP address.", lang)
        ip = listen(lang)
        result = get_shodan_data(ip)
        speak(result, lang)

    elif 'virustotal' in command or 'hash' in command:
        speak("Tell me the hash.", lang)
        file_hash = listen(lang)
        result = get_virustotal_report(file_hash)
        speak(result, lang)

    elif 'otx' in command:
        speak("Tell me the IP address.", lang)
        ip = listen(lang)
        result = get_otx_info(ip)
        speak(result, lang)

    elif 'vulnerability' in command or 'exploit' in command:
        for vuln in vulnerabilities:
            if vuln in command:
                speak(vulnerabilities[vuln], lang)
                return

    elif 'run nmap' in command:
        speak("Running Nmap scan...", lang)
        os.system("nmap -sV 127.0.0.1")
        speak("Scan complete.", lang)

    else:
        response = ask_openai(command)
        speak(response, lang)
        log_event(f"ChatGPT Response: {response}")

# === Main Entry ===
def main():
    speak("I am Kalki, your cybersecurity assistant.", 'en')
    speak("Do you want to speak in English or Hindi?", 'en')
    choice = listen('en')
    lang = 'hi' if 'hindi' in choice else 'en'

    speak("How can I assist you today?", lang)

    while True:
        command = listen(lang)
        if command:
            if 'exit' in command or 'goodbye' in command:
                speak("Goodbye! Stay safe online!", lang)
                break
            process_command(command, lang)

if __name__ == "__main__":
    main()
