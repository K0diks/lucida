## English
<a id="english"></a>
# ✨ Lucida – Experimental Programming Language  

🌟 **Lucida** is my own programming language created to learn the principles of interpreters and compilers. In the future, it is planned to add support for graphics, window interfaces, and advanced features.  

---

## 🌍 Translations  
- 🇬🇧 [English](#english)
- 🇩🇪 [Deutsch](#german)
- 🇷🇺 [Русский](#russian)

---


---



## 🚀 Features  
✅ **Basic Syntax** – variables, conditions, loops  
✅ **Text Handling** – input and output  
✅ **Configuration via `config.json`**  
🖥️ **Graphics** – window creation, text rendering (in development)  
📂 **File System** – reading and writing files (planned)  

---

## 🔧 Installation and Setup  

### 📥 Installation  
1. **Install Python** (if you don’t have it yet) – [python.org](https://www.python.org/downloads/)  
2. **Download Lucida** from GitHub:  
3. **Download the project**  
4. **Go to the project folder**:  
5. **Install dependencies (if any)**:  

---

## ▶ First Run of Lucida  
1. **Run the main file**:  
2. **Lucida will create a folder in `Documents`**:  
3. ## ⚙ Configure Lucida via `config.json`  
The configuration file is located at:  
C:\Users\YOUR_USER_NAME\Documents\LucidaCode\config\config.json  

Example `config.json`:  
```json
{
    "theme": "dark",
    "autoload_last_project": true,
    "library_path": "C:/Users/YOUR_USER_NAME/Documents/Lucida/libs"
}
```
---

## Deutsch
<a id="german"></a>
# ✨ Lucida – Experimentelle Programmiersprache  

🌟 **Lucida** ist meine eigene Programmiersprache, die entwickelt wurde, um die Prinzipien von Interpretern und Compilern zu lernen. In Zukunft ist geplant, die Unterstützung für Grafik, Fensteroberflächen und erweiterte Funktionen hinzuzufügen.  

## 🌍 Übersetzungen
- 🇬🇧 [English](#english)
- 🇩🇪 [Deutsch](#german)

---

## 🚀 Funktionen  
✅ **Grundsyntax** – Variablen, Bedingungen, Schleifen  
✅ **Textverarbeitung** – Eingabe und Ausgabe  
✅ **Konfiguration über `config.json`**  
🖥️ **Grafik** – Fenstererstellung, Textdarstellung (in Entwicklung)  
📂 **Dateisystem** – Lesen und Schreiben von Dateien (geplant)  

---

## 🔧 Installation und Setup  

### 📥 Installation  
1. **Installiere Python** (falls noch nicht installiert) – [python.org](https://www.python.org/downloads/)  
2. **Lade Lucida von GitHub herunter**:  
3. **Lade das Projekt herunter**  
4. **Wechsle in das Projektverzeichnis**:  
5. **Installiere die Abhängigkeiten (falls vorhanden)**:  

---

## ▶ Erster Start von Lucida  
1. **Führe die Hauptdatei aus**:  
2. **Lucida erstellt einen Ordner in `Dokumente`**:  
3. ## ⚙ Konfiguration von Lucida über `config.json`  
Die Konfigurationsdatei befindet sich unter:  
C:\Users\DEIN_BENUTZERNAME\Documents\LucidaCode\config\config.json  

Beispiel `config.json`:  
```json
{
    "theme": "dark",
    "autoload_last_project": true,
    "library_path": "C:/Users/DEIN_BENUTZERNAME/Documents/Lucida/libs"
}
```

---

## Русский
<a id="russian"></a>

---














<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lucida</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .language-buttons { margin-bottom: 20px; }
        .language-buttons button { padding: 10px; margin-right: 10px; }
    </style>
</head>
<body>

    <div class="language-buttons">
        <button onclick="changeLanguage('en')">🇬🇧 English</button>
        <button onclick="changeLanguage('de')">🇩🇪 Deutsch</button>
    </div>

    <div id="content"></div>

    <script>
        const content = {
            en: `
                <h1>✨ Lucida – Experimental Programming Language</h1>
                <p>🌟 <strong>Lucida</strong> is my own programming language created to learn the principles of interpreters and compilers. In the future, it is planned to add support for graphics, window interfaces, and advanced features.</p>
            `,
            de: `
                <h1>✨ Lucida – Experimentelle Programmiersprache</h1>
                <p>🌟 <strong>Lucida</strong> ist meine eigene Programmiersprache, die entwickelt wurde, um die Prinzipien von Interpretern und Compilern zu lernen. In Zukunft ist geplant, die Unterstützung für Grafik, Fensteroberflächen und erweiterte Funktionen hinzuzufügen.</p>
            `
        };

        function changeLanguage(lang) {
            document.getElementById('content').innerHTML = content[lang];
        }

        // Set default language
        changeLanguage('en');
    </script>

</body>
</html>


