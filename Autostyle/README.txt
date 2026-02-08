🚀 Autostyle - Ultimate PowerShell + oh-my-posh Setup

Author: Victor Hugo

Purpose: Install and configure PowerShell 7, oh-my-posh, jandedobbeleer theme, Nerd Font,
and automatically configure Windows Terminal & VS Code for a plug-and-play setup.

---

✨ Features:

- Installs PowerShell 7 if missing
- Installs oh-my-posh (modern version)
- Downloads and sets the jandedobbeleer theme
- Creates/updates PowerShell 7 profile ($PROFILE) to auto-load the theme
- Checks for CaskaydiaCove Nerd Font; installs it if missing
- Installs VS Code if missing and configures terminal/font
- Configures Windows Terminal automatically
- Fully plug-and-play setup

⚠️ Note: The script runs everything automatically. Manual verification optional.

---

How to Use

You can run the script in **two ways**:

1️⃣ **Using PowerShell Terminal**

- Open PowerShell (as Administrator for font installation)
- Navigate to the folder where the script is saved:

  cd C:\Users\Victor\Downloads\

- Run:

  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
  .\Autostyle.ps1

> 💡 Note: The `.\` means “this directory”. You must be in the same folder where `Autostyle.ps1` is saved.

2️⃣ **Using the GUI**

- Right-click the `Autostyle.ps1` file
- Select **Run with PowerShell**
- The script executes automatically without needing to navigate to the folder

---

💻 Automated Setup Includes:

- PowerShell 7 installation (if missing)
- oh-my-posh installation
- Download & configure jandedobbeleer theme
- Update `$PROFILE` to auto-load theme
- Install CaskaydiaCove Nerd Font
- Install & configure VS Code terminal/font
- Configure Windows Terminal default profile & font

---

🛠 Manual Steps (Optional)

Windows Terminal:
- Open **Settings → Startup → Default profile**
- Confirm PowerShell 7 is default
- Confirm font is **CaskaydiaCove Nerd Font**

VS Code:
- Ctrl+Shift+P → Terminal: Select Default Profile → PowerShell
- Confirm font is **CaskaydiaCove Nerd Font**
- Adjust font size/line height as desired

---

✅ Quick Check

- Run `$PSVersionTable` → should show **PowerShell 7.x**
- Open PowerShell 7 → **jandedobbeleer theme** should load automatically
- Open Windows Terminal / VS Code → confirm **PowerShell 7** + **CaskaydiaCove Nerd Font**

---

🎯 Ready! You now have a professional, visually appealing terminal setup
that can be replicated on any Windows machine with **Autostyle**.