# 🎰 D&D Annual Lucky Draw Spin (Ultra-Wide Stage Ready)

A production-ready, ultra-wide responsive **Lucky Draw Spin** web application built from scratch with Vanilla HTML5, CSS3, and modern JavaScript (ES6+). Engineered specifically for high-stakes LED stage screens, live presentations, and MacBook trackpad/keyboard operators.

---

## 🌟 Key Features

### 🖥️ Stage & Ultra-Wide Design
- **Full-Screen Background Video**: Loops `public/bg.mp4` with a high-definition poster fallback (`D&D2026_1920x1080.jpg`).
- **Targeted Overlap Layout**: The 3D-feel vertical roulette slot machine is positioned on the **LEFT** side of the screen (`left: clamp(20px, 4.5vw, 85px)`), purposefully overlapping the 2D "D&D" text area while leaving the majestic castle and fireworks on the center-right crystal clear.
- **Ultra-Wide & Stage Responsiveness**: Scales fluidly on 16:9, 21:9, 32:9, 4K, and 8K LED stage walls using CSS `clamp()`, `vw`, and `vh` relative units.
- **Distraction-Free Stage Mode**: Press **`H`** or click **Stage Mode** to instantly collapse both side drawers and minimize the top dock for a broadcast-ready presentation.

### 🎲 Spacebar Controls & Spin Physics (MacBook Optimized)
- **1-Tap Spacebar**: Starts the vertical roulette spin. Cards accelerate smoothly up to 3,200 px/sec.
- **2-Tap / Force Stop**: Press Spacebar a second time (or double-tap) while spinning to forcefully brake and instantly reveal the winner with a satisfying recoil lock.
- **Fair Pool Elimination**: Winners are permanently removed from the active drawing pool and saved in `localStorage`.
- **ABSENCE / REDRAW SUPPORT**: If a drawn winner is absent from the hall, click "Redraw" on the announcement card or "Return to Pool" in the history list to restore their eligibility.

### 📊 Live Google Sheets Sync & Offline Protection
- **Direct CSV Integration**: Fetches real-time participant records from the Google Sheet published CSV link.
- **Default URL**: Pre-configured with the official published CSV URL.
- **HQ Division Logic**: 
  - Col A = Employee ID, Col B = Full Name, Col C = Department, Col D = Division.
  - Automatically formats Department as `HQ - [Division]` whenever Dept is "HQ" and Division is provided (e.g. `HQ - DS`).
- **Zero-Downtime Offline Fallback**: All 510 participants are embedded directly into the standalone file, guaranteeing the lucky draw functions flawlessly even if WiFi drops on stage.

### 🎁 Prize Management & Pre-Spin Reveal
- **Custom Prize Manager**: Add, edit, or delete prizes with customizable tiers, quantities, and descriptions.
- **Local Photo Upload**: Upload custom JPG/PNG prize images—automatically converted to Base64 and stored in `localStorage` to avoid Google Drive CORS and hotlinking restrictions.
- **Pre-Spin Reveal**: Press **`P`** or click **"Reveal Prize"** to showcase the grand prize on screen with golden glowing rays before the spin starts.

### 🎆 Audio & Celebration FX
- **Canvas Fireworks & Confetti**: Dynamic multi-color particle fireworks and dual-cannon confetti explosion across the screen on every win.
- **Tactile Sound Effects**: Web Audio API synthesized mechanical ratchet clicks (pitch modulates with rolling velocity) and brass victory fanfare.
- **Background Music (BGM)**: HTML5 `<audio>` player with play/pause toggle, volume slider, custom MP3 URL input, and local audio file selector.

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|---|---|
| **`SPACEBAR`** | **Spin** (when idle) / **Force Stop** (when spinning) |
| **`H`** | Toggle **Stage Mode** (hides/shows all side panels) |
| **`P`** | **Pre-Spin Reveal** for the current prize |
| **`W`** | Toggle **Winners History** drawer |
| **`S`** | Toggle **Settings & Controls** drawer |
| **`M`** | Toggle **Sound Effects (SFX)** mute/unmute |
| **`F`** | Toggle **Fullscreen** |

---

## 🚀 Running the App Locally

### Option 1: Direct Double-Click (Zero Server Required)
Simply open `public/index.html` in Safari, Chrome, or Edge on your MacBook. All assets, scripts, styles, and 510 participants are fully bundled.

### Option 2: Local HTTP Server
Run any static server from the terminal:
```bash
# Using Python
python3 -m http.server 8000

# Open in browser:
# http://localhost:8000/public/index.html
```

---

## ☁️ Deploying to Vercel or GitHub Pages

The application is 100% static:
- **Vercel**: Deploy the folder directly (`vercel --prod`). Root `index.html` and `public/index.html` are both pre-configured.
- **GitHub Pages**: Push this repository to GitHub and enable GitHub Pages on the `main` branch.
