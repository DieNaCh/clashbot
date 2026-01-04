# Clash Royale Computer Vision Assistant

A computer vision–powered assistant for **Clash Royale** that helps track your opponent’s **elixir**, **card cycle**, and **player statistics** in real time.

This project combines **computer vision**, **OCR**, and **data analysis** to extract meaningful gameplay insights directly from match footage or live gameplay.

> ⚠️ This project is for **educational and research purposes only**. It is not affiliated with or endorsed by Supercell.

---

## Features

### 🎮 In-Game Tracking (Computer Vision)
- **Opponent elixir estimation**
- **Card cycle tracking**
- Detection of cards played in real time

### 📊 Player & Profile Insights
- Clan name
- Most played deck
- Win rate
- Match history summary *(if available via public data)*

---

## 🧠 How It Works

1. **Video Input**
   - Live gameplay capture or recorded footage

2. **Computer Vision**
   - Card recognition using YOLO
   - Elixir bar detection & estimation
   - OCR for text-based data (player name, clan, etc.)

3. **Game Logic Engine**
   - Tracks card rotation (8-card cycle)
   - Updates elixir count based on time and card cost

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **NumPy**
- **Tesseract OCR**
- **YOLO** 
- **Requests / APIs** for player data

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/clash-royale-cv-bot.git
cd clash-royale-cv-bot
pip install -r requirements.txt
