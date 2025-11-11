# 🤖 FRIDAY — Your Personal Voice Assistant (Python)

## 📄 Overview
**FRIDAY** is a voice-controlled personal AI assistant inspired by *Iron Man’s FRIDAY*.  
It performs a wide range of tasks such as playing songs, answering questions, telling jokes, fetching facts, reading Wikipedia summaries, and even remembering notes — all through **speech commands**.

---

## ⚙️ Features
- 🎵 **Play songs** on YouTube via voice command.  
- 🌤️ **Weather updates** for Karaikudi using live Google data.  
- 📅 **Date, time, and reminder** functionalities.  
- 🧠 **Wikipedia integration** for general knowledge queries.  
- 📚 **How-To Mode** powered by PyWikiHow.  
- 😂 **Jokes & Facts** using `pyjokes` and `randfacts`.  
- 🗒️ **Memory module** — remembers user notes in `data.txt`.  
- 🗣️ **Conversational responses** with `pyttsx3` and `speech_recognition`.  

---

## 🧩 Commands You Can Try
| Command | Function |
|----------|-----------|
| “Play [song name]” | Plays song on YouTube |
| “What’s the time/date?” | Tells current time or date |
| “Tell me a joke/fact” | Says a random joke or fact |
| “What do you know about [topic]” | Reads Wikipedia summary |
| “Activate how to mode” | Explains how to do tasks using WikiHow |
| “Weather” | Tells current weather of Karaikudi |
| “Remember that…” | Saves a note |
| “What do you remember” | Recalls saved notes |

---

## 🧠 Libraries Used
- `speech_recognition` — captures and processes voice input  
- `pyttsx3` — converts text to speech  
- `pywhatkit` — plays YouTube videos via command  
- `wikipedia` — retrieves knowledge summaries  
- `pyjokes`, `randfacts` — entertainment modules  
- `pywikihow` — fetches how-to guides  
- `BeautifulSoup`, `requests` — web scraping for weather data  
- `datetime`, `os`, `webbrowser`, `random` — system utilities

---

## 💻 How to Run
1. Install dependencies:
   ```bash
   pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes randfacts requests beautifulsoup4 pywikihow
2. Run the program
    ```bash
    python Friday.py
    
3. Say “Hey Friday” followed by your command.
   ```bash
   Hey Friday, play Believer on YouTube
   Hey Friday, what’s the weather?
   Hey Friday, tell me a joke

---

## 🚀 Future Enhancements

- Add GUI interface with animations.
- Include voice authentication and personalization.
- Extend to IoT control (e.g., lights, fans, appliances).
- Add support for multiple languages.

---

## 👨‍💻 Author

**Aravinthvasan S**  
B.Tech Electronics & Communication Engineering (Cyber Physical Systems)  
SASTRA Deemed University  

🔗 [GitHub Profile](https://github.com/av1429)

---

## 🪪 License

This project is licensed under the MIT License — free to use, modify, and share with proper credit.
