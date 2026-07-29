## Final project

# Emotion Detection Web Application

A full-stack Python web application that uses the **IBM Watson NLP EmotionPredict API** to analyze input text and determine emotional tone (anger, disgust, fear, joy, and sadness), identifying the dominant emotion. Built using **Flask**, **Requests**, and **HTML5/JavaScript**.

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Project Architecture](#-project-architecture)
- [Directory Structure](#-directory-structure)


---

## 🎯 Overview

This project provides both a reusable Python package (`EmotionDetection`) and a Flask web service to perform real-time sentiment/emotion analysis on user-submitted text. It communicates with IBM Watson's NLP runtime environment via REST API endpoints, processes the JSON response payload, handles error conditions (such as blank entries or invalid requests), and presents formatted results to the web UI.

---

## 🏗 Project Architecture

+---------------------------+
                            |      Web User Interface   |
                            | (HTML / JS / Index Page)  |
                            +-------------+-------------+
                                          |
                                 GET /emotionDetector
                                          |
                                          v
                            +---------------------------+
                            |      Flask Server         |
                            |        (server.py)        |
                            +-------------+-------------+
                                          |
                                emotion_detector()
                                          |
                                          v
                            +---------------------------+
                            |  EmotionDetection Package |
                            |   (emotion_detection.py)  |
                            +-------------+-------------+
                                          |
                                 POST /EmotionPredict
                                          |
                                          v
                            +---------------------------+
                            |    IBM Watson NLP API     |
                            +---------------------------+

---

## 📁 Directory Structure

```text
final-project-emb-ai/
│
├── EmotionDetection/                  # Python Package Module
│   ├── __init__.py                    # Package initialization
│   └── emotion_detection.py           # Core API wrapper function
│
├── static/                            # Static Frontend Assets
│   └── mywebscript.js             # Asynchronous AJAX requests handler
│
├── templates/                         # Flask HTML Templates
│   └── index.html                     # Main Web Interface
│
├── server.py                          # Flask Server Application Entrypoint
├── test_emotion_detection.py          # Unit Tests suite
└── README.md                          # Project Documentation