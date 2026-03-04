# Chat-Roboter Backend 🤖

## Übersicht 📖
Dies ist das Backend für den Chat-Roboter, das mit Flask (Version 2.4) entwickelt wurde. Es dient als Schnittstelle zwischen der Benutzeranfrage und der Verarbeitung der Daten. Das Backend ist so konfiguriert, dass es mit PythonAnywhere kommuniziert, um eine zuverlässige Bereitstellung und Verwaltung zu gewährleisten.

## Voraussetzungen ✅
Stellen Sie sicher, dass die folgenden Anforderungen erfüllt sind, bevor Sie das Projekt ausführen:

- Python 3.9 oder höher 🐍
- Flask 2.4 🌟
- Ein PythonAnywhere-Konto für die Bereitstellung ☁️

## Installation 🛠️
1. Klonen Sie das Repository:
   ```bash
   git clone <repository-url>
   ```

2. Wechseln Sie in das Projektverzeichnis:
   ```bash
   cd chat-roboter-backend
   ```

3. Installieren Sie die Abhängigkeiten:
   ```bash
   pip install -r requirements.txt
   ```

## Nutzung 🚀
1. Starten Sie den Flask-Server lokal:
   ```bash
   python app.py
   ```

2. Der Server wird standardmäßig unter `http://127.0.0.1:5000` ausgeführt. Sie können die Endpunkte mit einem Tool wie Postman oder cURL testen.

## Bereitstellung auf PythonAnywhere 🌐
1. Laden Sie die Projektdateien auf PythonAnywhere hoch.
2. Konfigurieren Sie die Web-App-Einstellungen auf PythonAnywhere:
   - Wählen Sie Python 3.9 oder höher als Laufzeit.
   - Geben Sie den Pfad zur Flask-App an (z. B. `/home/<Ihr-Benutzername>/chat-roboter-backend/app.py`).
3. Installieren Sie die Abhängigkeiten auf PythonAnywhere:
   ```bash
   pip install -r requirements.txt
   ```
4. Starten Sie die Web-App auf PythonAnywhere neu.

## Endpunkte 🔗
Hier sind einige der Hauptendpunkte des Backends:

- `GET /`: Gibt eine Willkommensnachricht zurück.
- `POST /chat`: Verarbeitet Benutzereingaben und gibt eine Antwort zurück.

## Lizenz 📜
Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE`.

## Autor ✍️
Yannick Vaterlaus

## Technologien 🛠️
Dieses Projekt wurde mit den folgenden Technologien entwickelt:

- Flask 2.4 🌟
- Python 3.9+ 🐍
- PythonAnywhere ☁️

## Features 🚀
Das Backend bietet die folgenden Funktionen:

- 🌐 Kommunikation mit PythonAnywhere für einfache Bereitstellung
- 🤖 Verarbeitung von Benutzereingaben und Generierung von Antworten
- 🔗 Bereitstellung von RESTful-APIs für einfache Integration
- 🛡️ Sicheres und zuverlässiges Backend-Design# Backend-AI-Chat-Roboter
