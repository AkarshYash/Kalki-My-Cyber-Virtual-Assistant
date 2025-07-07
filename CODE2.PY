# Kalki: Advanced AI Cybersecurity Assistant

import speech_recognition as sr
import pyttsx3
import openai
from gtts import gTTS
import os
import random
import socket
import dns.resolver
import requests
import threading
import streamlit as st
from datetime import datetime

# ------------------ Initialization ------------------
engine = pyttsx3.init()
openai.api_key = 'your-openai-api-key-here'

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
        print(f"Listening ({language})...")
        audio = recognizer.listen(source)
        try:
            if language == 'hi':
                return recognizer.recognize_google(audio, language="hi-IN").lower()
            else:
                return recognizer.recognize_google(audio).lower()
        except:
            speak("Sorry, I couldn't understand that.", language)
            return listen(language)

# ------------------ Cyber Dictionary ------------------
cyber_security_tools = {
    "nmap": "Nmap is used to discover hosts and services on a computer network.",
    "metasploit": "Metasploit helps create and execute exploits.",
    "wireshark": "Wireshark captures and analyzes network traffic.",
    "burp suite": "Burp Suite is used for web application security testing."
}

vulnerabilities = {
    "sql injection": "Allows attacker to interfere with application DB queries.",
    "xss": "Cross-site scripting injects malicious scripts."
}

# ------------------ Logging ------------------
def log_event(message):
    with open("alerts.log", "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

# ------------------ Network Tools ------------------
def resolve_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        speak(f"The IP address of {domain} is {ip}.")
        log_event(f"Resolved IP for {domain}: {ip}")
        return ip
    except:
        speak("Could not resolve IP address.")


def get_dns_records(domain):
    try:
        result = dns.resolver.resolve(domain, 'A')
        ips = [ip.to_text() for ip in result]
        speak(f"DNS A Records for {domain} are {', '.join(ips)}")
        log_event(f"DNS A Records for {domain}: {ips}")
    except:
        speak("DNS resolution failed.")


def scan_ports(domain, port_range=(1, 1024)):
    open_ports = []
    closed_ports = []
    ip = resolve_ip(domain)

    if not ip:
        return

    speak(f"Scanning ports 1 to 1024 for {domain}")

    def check_port(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)
        s.close()

    threads = []
    for port in range(port_range[0], port_range[1] + 1):
        t = threading.Thread(target=check_port, args=(port,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    log_event(f"Open ports for {domain}: {open_ports}")
    speak(f"Port scan completed. {len(open_ports)} open ports found.")
    return open_ports, closed_ports


# ------------------ Code Generation ------------------
def generate_code(language, task_description):
    prompt = f"Write a {language} code that does the following: {task_description}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=400,
        temperature=0.5
    )
    code = response.choices[0].text.strip()
    extension = {
        "python": ".py", "java": ".java", "html": ".html",
        "css": ".css", "javascript": ".js", "c": ".c", "c++": ".cpp"
    }.get(language.lower(), ".txt")
    filename = f"generated_code_{datetime.now().strftime('%Y%m%d_%H%M%S')}{extension}"
    with open(filename, "w") as f:
        f.write(code)
    speak(f"Code written to {filename}")
    log_event(f"Code generated: {filename}")
    return filename


# ------------------ Process Command ------------------
def process_command(command, language='en'):
    if 'help' in command:
        speak("I can help with cybersecurity tasks, code generation, scanning and more.", language)

    elif 'tool' in command:
        for tool in cyber_security_tools:
            if tool in command:
                speak(cyber_security_tools[tool], language)

    elif 'vulnerability' in command or 'exploit' in command:
        for vuln in vulnerabilities:
            if vuln in command:
                speak(vulnerabilities[vuln], language)

    elif 'run nmap' in command:
        speak("Running simulated Nmap scan...")
        os.system("nmap -sV 127.0.0.1")

    elif 'ip address' in command:
        domain = command.split("of")[-1].strip()
        resolve_ip(domain)

    elif 'dns' in command:
        domain = command.split("of")[-1].strip()
        get_dns_records(domain)

    elif 'scan port' in command or 'port scanning' in command:
        domain = command.split("of")[-1].strip()
        open_ports, closed_ports = scan_ports(domain)
        speak(f"Open ports: {open_ports}")

    elif 'create code' in command or 'generate tool' in command:
        speak("Which language should I use?", language)
        language = listen(language)
        speak("Describe the features or functionality.", language)
        features = listen(language)
        generate_code(language, features)

    else:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=command,
            max_tokens=200
        )
        speak(response.choices[0].text.strip(), language)


# ------------------ Main ------------------
def main():
    speak("I am Kalki, your cybersecurity assistant.")
    speak("Do you want to speak in English or Hindi?")
    choice = listen()
    language = 'hi' if 'hindi' in choice else 'en'

    speak("Namaste!" if language == 'hi' else "Hello! How can I help you today?", language)

    while True:
        command = listen(language)
        if command:
            if any(word in command for word in ['exit', 'stop', 'quit', 'alvida']):
                speak("Goodbye! Stay safe online!", language)
                break
            process_command(command, language)


if __name__ == "__main__":
    main()
