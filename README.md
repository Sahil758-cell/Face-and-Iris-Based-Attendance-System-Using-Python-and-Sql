# Face-and-Iris-Based-Attendance-System-Using-Python-and-Sql
In This repository simple pyhton code project are there and it made by using ML and DL algorithm
# 🎓 Face and Retina-Based Attendance System

## 📖 Introduction

The **Face and Retina-Based Attendance System** is an intelligent, Python-based desktop application that automates the process of attendance using two biometric features — **Facial Recognition** and **Iris (Retina) Detection**. The system is developed as a final-year engineering project and leverages computer vision techniques via OpenCV and an interactive GUI using Tkinter.

This hybrid system improves upon traditional and biometric-only attendance methods by incorporating both face and iris recognition to increase security and reliability. The project can work with a **mobile phone camera** (via IP Webcam or Camo app), enabling greater flexibility and cost-effectiveness.

---

## ✨ Key Features

- 🧑‍🏫 **Dual Biometric Authentication**: Uses both face and iris to ensure accurate identity verification.
- 📷 **Live Camera Support**: Connects with phone camera streams for real-time recognition.
- 📊 **Attendance Logging**: Marks and stores attendance entries in a structured CSV file.
- 🖥️ **Fullscreen Tkinter GUI**: Interactive and visually appealing interface for ease of use.
- 📁 **Dataset Collection**: Allows new users to capture and store their face and iris data.
- ⏰ **Live Clock Dashboard**: Embedded clock on the main screen for real-time display.
- 🔐 **Offline Access**: Entirely offline system — no internet required.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core Programming |
| OpenCV     | Face and Iris Detection & Recognition |
| Tkinter    | GUI Design |
| NumPy      | Image Array Manipulation |
| Pandas     | CSV File Handling |
| Camo/IP Webcam | Mobile Camera Integration |

---

## 📁 Project Structure

```plaintext
Face-Retina-Attendance-System/
│
├── main.py                  # Main GUI launcher
├── face_recognition.py      # Face detection & matching
├── iris_attendance.py      # Iris detection & matching
├── data       # Module to capture & save datasets
├── attendance.csv           # Attendance record file
|_____ Project image Folder   # For getting GUI Image upload in project 
├── dataset/
│   ├── Person1/
│   ├── Person2/
│   └── ...
├── images/                  # GUI assets (icons, backgrounds)
├── utils/
│   ├── preprocessor.py
│   └── helpers.py
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
