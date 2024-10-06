import speech_recognition as sr
import pyttsx3
import openai
from gtts import gTTS
import os
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set your OpenAI API key here
openai.api_key = 'Pls create your Personal service api key from open ai like - S9msaKIA'

# Cyber security tools and information (expand this list as needed)
cyber_security_tools = {
    "nmap": "Nmap is a network scanning tool used to discover hosts and services on a computer network.",
    "metasploit": "Metasploit is a penetration testing framework for developing and executing exploit code against a remote target machine.",
    "wireshark": "Wireshark is a network protocol analyzer used to capture and interactively browse traffic running on a computer network.",
    "burp suite": "Burp Suite is an integrated platform for performing web application security testing.",
}

# Vulnerabilities and exploits (expand this list as needed)
vulnerabilities = {
    "sql injection": "SQL injection is a code injection technique that might destroy your database. It allows an attacker to interfere with the queries that an application makes to its database.",
    "xss": "Cross-site scripting (XSS) is a vulnerability that allows an attacker to inject malicious scripts into content delivered to users.",
}

# Function to speak text
def speak(text, language='en'):
    """This function will make Kalki speak out loud in both English and Hindi."""
    if language == 'hi':  # Use gTTS for Hindi
        tts = gTTS(text=text, lang='hi')
        tts.save("response.mp3")
        os.system("mpg321 response.mp3")  # Play the audio
    else:
        engine.say(text)
        engine.runAndWait()

def listen(language='en'):
    """This function listens for a user's speech and converts it to text in the specified language."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Kalki: I am listening in {language}...")
        audio = recognizer.listen(source)

        try:
            if language == 'hi':  # For Hindi
                command = recognizer.recognize_google(audio, language="hi-IN")
            else:  # For English
                command = recognizer.recognize_google(audio)
                
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?", language)
            return listen(language)
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the service.", language)
            return None

def ask_openai(prompt, language='en'):
    """This function queries OpenAI to get a response based on the input."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def process_command(command, language='en'):
    """This function processes user commands related to cybersecurity and ethical hacking."""
    if 'help' in command:
        help_text = "I can assist you with cybersecurity-related tasks such as explaining vulnerabilities, suggesting tools, and testing scripts. What would you like help with?"
        speak(help_text, language)

    elif 'tool' in command:
        for tool in cyber_security_tools:
            if tool in command:
                speak(cyber_security_tools[tool], language)
                return

    elif 'vulnerability' in command or 'exploit' in command:
        for vulnerability in vulnerabilities:
            if vulnerability in command:
                speak(vulnerabilities[vulnerability], language)
                return

    elif 'test script' in command or 'run nmap' in command:
        # Example: You can expand this to interact with actual scripts/tools
        if 'nmap' in command:
            speak("Running Nmap scan on the target network...", language)
            os.system("nmap -sV 127.0.0.1")  # Example command
            speak("Scan complete.", language)

    else:
        response = ask_openai(command, language)
        speak(response, language)

def recite_cybersecurity_tip():
    """This function gives a random cybersecurity tip."""
    tips = [
        "Always keep your software updated to the latest version.",
        "Use strong, unique passwords and enable two-factor authentication.",
        "Regularly perform vulnerability assessments on your network.",
        "Use network segmentation to limit access to sensitive data.",
    ]
    tip = random.choice(tips)
    speak("Here's a cybersecurity tip:", 'en')
    speak(tip, 'en')

def main():
    """Main loop for the assistant."""
    # Introduce Kalki
    speak("I am Kalki, your cybersecurity assistant.", 'en')
    speak("How can I help you today with cybersecurity tasks?", 'en')

    # Provide a cybersecurity tip
    recite_cybersecurity_tip()

    while True:
        # Ask the user whether they want to speak in Hindi or English
        speak("Do you want to speak in English or Hindi?", 'en')
        choice = listen()

        # Default language is English, but switch to Hindi if the user chooses so
        if 'hindi' in choice or 'हिंदी' in choice:
            language = 'hi'
            speak("Namaste, main Kalki hoon. Aapki kaise madad kar sakta hoon?", 'hi')
        else:
            language = 'en'
            speak("Hello, I am Kalki. How can I help you today?", 'en')
        
        command = listen(language)

        if command:
            if 'exit' in command or 'goodbye' in command or 'stop' in command or 'alvida' in command:
                speak("Goodbye! Stay safe online!", language)
                break
            
            process_command(command, language)

if __name__ == "__main__": 
    main()
