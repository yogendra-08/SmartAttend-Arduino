# 📡 AttendSync

> Smart Attendance System using Arduino UNO, RFID, Python, LCD Display, Buzzer, and CSV Logging.

![Arduino](https://img.shields.io/badge/Arduino-UNO-blue?style=for-the-badge&logo=arduino)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![RFID](https://img.shields.io/badge/RFID-RC522-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge)

---

## 🚀 Project Overview

AttendSync is a smart attendance system designed to automate attendance tracking using RFID technology and Arduino. The system provides real-time attendance updates through an LCD display, LED indicators, buzzer alerts, and automatic attendance logging using Python.

This project demonstrates how embedded systems and software applications can work together to simplify attendance management.

---

## ✨ Features

✅ RFID-Based Attendance Marking

✅ LCD Status Display

✅ Green LED Attendance Confirmation

✅ Buzzer Alert System

✅ Serial Communication with Python

✅ Automatic CSV Attendance Logging

✅ Timestamp Recording

✅ Attendance Dashboard Integration

✅ Easy Hardware Setup

---

## 🛠️ Hardware Components

| Component | Quantity |
|------------|----------|
| Arduino UNO | 1 |
| RC522 RFID Reader | 1 |
| RFID Card/Tag | 1 |
| 16x2 LCD Display | 1 |
| Green LED | 1 |
| Red LED | 1 |
| Buzzer | 1 |
| Breadboard | 1 |
| Resistors | 2 |
| Jumper Wires | Multiple |

---

## ⚙️ System Workflow

```text
RFID Card Scan
      ↓
Arduino UNO Reads UID
      ↓
Green LED ON
      ↓
Buzzer Beep
      ↓
LCD Displays Attendance Status
      ↓
Serial Data Sent to Python
      ↓
Attendance Saved in CSV
      ↓
Dashboard Updated
```

---

## 📂 Project Structure

```bash
AttendSync/
│
├── arduino/
│   └── attendance_system.ino
│
├── python/
│   └── attendance_logger.py
│
├── data/
│   └── oct02.csv
│
├── images/
│   ├── circuit_diagram.png
│   └── demo.png
│
└── README.md
```

---

## 🖥️ Sample Attendance Record

```csv
Name,Status,Date,Time
YOGI,Present,02-10-2026,10:15:23
```

---

## 📺 LCD Output

```text
YOGI
PRESENT
```

---

## 🔊 Device Response

```text
✓ Green LED ON
✓ Buzzer Beep
✓ Attendance Recorded
```

---

## 📜 Serial Monitor Output

```text
YOGI_PRESENT
Attendance Marked Successfully
```

---

## 💻 Technologies Used

- Arduino IDE
- C++
- Python
- CSV File Handling
- Serial Communication
- RFID RC522
- Embedded Systems

---

## 🎯 Future Enhancements

- Cloud Database Integration
- Google Sheets Logging
- Web Dashboard
- ESP32 WiFi Support
- QR Code Attendance
- Mobile Application
- Face Recognition Integration

---

## 📸 Demo

Add your project screenshots and hardware setup images here.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and create a pull request.

---

## 📄 License

This project is developed for educational and learning purposes.

---

### ⭐ If you found this project useful, don't forget to star the repository!