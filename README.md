# PopupWhacker

![PopupWhacker](https://img.shields.io/badge/Windows-10%2B-brightgreen?logo=windows) ![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)

A lightweight script designed for Windows systems to automatically close non-minimizable application pop-up windows during startup.

[查看中文文档](README_CN.md)

## 🔧 Key Features

- Automatically closes pop-ups using **fuzzy title matching**
- Runs silently in the background
- Configured via plain text files
- **Supports regular expressions**

## 🛠️ Installation Guide

1. **Install dependencies**:
   ```bash
   pip install pywinauto
   ```

2. **Configure rule file**:
   - First run automatically creates `titles.txt` in the same directory
     ```
     Microsoft Teams
     WhatsApp
     Adobe Reader
     ```
   - Save and close Notepad, then restart the script to take effect

## ⚙️ Usage

### 1. Manual test run
```powershell
PopupWhacker.pyw
```

### 2. Set up auto-start (recommended)
1. Open **Task Scheduler** (`taskschd.msc`)
2. Create basic task:
   - **Trigger**: At user logon
   - **Action**: Start program
   - **Program/script**: Select `PopupWhacker.pyw`
   - **Start in**: Script directory (e.g., `C:\Tools\PopupWhacker`)
3. Check "Run with highest privileges"
4. Save task

## 🔍 Fuzzy Matching Mechanism

The script uses regular expressions for intelligent matching:
- **Case-insensitive** (`teams` matches `Microsoft Teams`)
- **Supports regex** (`^Teams` matches `Teams Meeting`)
- Automatically escapes special characters (avoids regex errors)
- Partial matching (`Teams` matches `Microsoft Teams`)

## 📝 Example Rule File
```
Teams
Edge
^Teams
```

Closes:
- Windows containing "Teams" (e.g., `Microsoft Teams`)
- Windows containing "Edge" (e.g., `Microsoft Edge`)
- Windows starting with "Teams" (e.g., `Teams Meeting`)

## 📁 Directory Structure Example
```
PopupWhacker/
├── PopupWhacker.pyw
├── titles.txt        # Add window titles to close (supports regex)
└── README.md
```

## ⚠️ Important Notes

- **Must be run with administrator privileges** (required for window automation)
- Works with **Windows 10/11**
- Does not handle minimized windows

## 📜 License

MIT License

---

> For Windows users who hate startup pop-ups ❤️