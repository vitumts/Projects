# 🚀 Autostyle.ps1 - Ultimate Setup Script
# Author: Victor Hugo
# Purpose: Install PowerShell 7, oh-my-posh, theme, Nerd Font,
#          configure Windows Terminal & VS Code automatically

# =========================
# 1️⃣ Install PowerShell 7
# =========================
Write-Host "Checking for PowerShell 7..."
if (-not (Get-Command pwsh -ErrorAction SilentlyContinue)) {
    Write-Host "PowerShell 7 not found. Installing via winget..."
    winget install Microsoft.PowerShell -e --source winget
} else {
    Write-Host "PowerShell 7 is already installed."
}

# =========================
# 2️⃣ Install oh-my-posh
# =========================
Write-Host "`nChecking for oh-my-posh..."
if (-not (Get-Command oh-my-posh -ErrorAction SilentlyContinue)) {
    Write-Host "oh-my-posh not found. Installing via winget..."
    winget install JanDeDobbeleer.OhMyPosh -e --source winget
} else {
    Write-Host "oh-my-posh is already installed."
}

# =========================
# 3️⃣ Download jandedobbeleer theme
# =========================
$ThemeFolder = "$HOME\ohmyposh"
$ThemeFile = "$ThemeFolder\jandedobbeleer.omp.json"

if (-not (Test-Path $ThemeFolder)) {
    New-Item -ItemType Directory -Path $ThemeFolder -Force | Out-Null
}

Invoke-WebRequest -Uri "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/jandedobbeleer.omp.json" `
    -OutFile $ThemeFile -UseBasicParsing

# =========================
# 4️⃣ Create/Edit PowerShell 7 PROFILE
# =========================
$ProfilePath = "$HOME\Documents\PowerShell\Microsoft.PowerShell_profile.ps1"
if (-not (Test-Path (Split-Path $ProfilePath))) {
    New-Item -ItemType Directory -Path (Split-Path $ProfilePath) -Force | Out-Null
}
if (-not (Test-Path $ProfilePath)) {
    New-Item -ItemType File -Path $ProfilePath -Force | Out-Null
}

$ProfileContent = @"
# Load oh-my-posh with jandedobbeleer theme
oh-my-posh init pwsh --config `"$ThemeFile`" | Invoke-Expression
"@

$CurrentContent = Get-Content $ProfilePath -Raw
if ($CurrentContent -notmatch "oh-my-posh init pwsh") {
    Add-Content -Path $ProfilePath -Value $ProfileContent
}

# =========================
# 5️⃣ Check / Install Nerd Font
# =========================
$fontName = "CaskaydiaCove Nerd Font"
$installed = (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" |
              Where-Object { $_.PSChildName -match $fontName }) -or
             (Get-ItemProperty "HKCU:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" |
              Where-Object { $_.PSChildName -match $fontName })

if (-not $installed) {
    Write-Host "`nInstalling Nerd Font ($fontName)..."
    $FontUrl = "https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/CaskaydiaCove.zip"
    $FontZip = "$env:TEMP\CaskaydiaCove.zip"
    $FontFolder = "$env:TEMP\CaskaydiaCove"

    Invoke-WebRequest -Uri $FontUrl -OutFile $FontZip -UseBasicParsing
    Expand-Archive -Path $FontZip -DestinationPath $FontFolder -Force

    $FontsToInstall = Get-ChildItem -Path $FontFolder -Filter "*Complete.ttf" -Recurse
    foreach ($f in $FontsToInstall) {
        Copy-Item $f.FullName "$env:WINDIR\Fonts\" -Force
        $wshell = New-Object -ComObject WScript.Shell
        $wshell.RegWrite("HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts\$($f.BaseName) (TrueType)", $f.Name, "REG_SZ")
    }
}

# =========================
# 6️⃣ Install/Configure VS Code
# =========================
$VSCodePath = "$env:LOCALAPPDATA\Programs\Microsoft VS Code\Code.exe"
if (-not (Test-Path $VSCodePath)) {
    Write-Host "`nVS Code not found. Installing via winget..."
    winget install Microsoft.VisualStudioCode -e --source winget
} else {
    Write-Host "VS Code is already installed."
}

$VSCodeSettings = "$env:APPDATA\Code\User\settings.json"
if (Test-Path $VSCodeSettings) {
    Write-Host "Configuring VS Code terminal..."
    $vscodeJson = Get-Content $VSCodeSettings -Raw | ConvertFrom-Json
    $vscodeJson["terminal.integrated.defaultProfile.windows"] = "PowerShell"
    $vscodeJson["terminal.integrated.profiles.windows"]["PowerShell"] = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
    $vscodeJson["terminal.integrated.fontFamily"] = "CaskaydiaCove Nerd Font"
    $vscodeJson | ConvertTo-Json -Depth 10 | Set-Content $VSCodeSettings
}

# =========================
# 7️⃣ Configure Windows Terminal
# =========================
$WTSettings = "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
if (Test-Path $WTSettings) {
    Write-Host "`nConfiguring Windows Terminal..."
    $json = Get-Content $WTSettings -Raw | ConvertFrom-Json
    $pwshProfile = $json.profiles.list | Where-Object { $_.commandline -match "pwsh" }
    if ($pwshProfile) {
        $json.profiles.defaults.fontFace = "CaskaydiaCove Nerd Font"
        $json.defaultProfile = $pwshProfile.guid
        $json | ConvertTo-Json -Depth 10 | Set-Content $WTSettings
    }
}

# =========================
# ✅ Finished
# =========================
Write-Host "`n🎯 Setup complete! Open PowerShell 7 to see the theme."
Write-Host "Windows Terminal and VS Code have been configured automatically."