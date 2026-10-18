# 🎰 D&D Anniversary Celebration | Grand Lucky Draw (Ultra-Wide Stage Edition)

A production-ready, ultra-wide responsive **Lucky Draw Spin** web application built from scratch with Vanilla HTML5, CSS3, and modern JavaScript (ES6+). Engineered for high-stakes LED stage screens, live presentations, and MacBook operators.

---

## 🌟 Upgraded Features

### 1. 🔐 Admin Login & Protected Configuration
- **Glassmorphism Login Modal**: Clicking the Settings button or pressing `S` prompts for Admin credentials:
  - **Admin ID**: `odmarketing`
  - **Password**: `ilovemyjob`
- **Protected Access**: Only authorized operators can access sheet sync, prize manager, screen calibration, and reset options.
- **Security & Alerts**: Invalid credentials trigger an elegant shake animation and custom glass toast (strictly zero native `alert()` dialogs).

### 2. 📊 UTF-8 BOM CSV Export (Excel & Thai Compatible)
- The **"Export CSV"** button downloads `state.winners` with a **UTF-8 BOM (`\uFEFF`)** prefix, ensuring Thai names and departments open cleanly in Microsoft Excel without character corruption.
- **Required Columns**:
  1. `ลำดับ` (Order)
  2. `ชื่อ` (Name)
  3. `แผนก` (Department)
  4. `รางวัล` (Prize)
  5. `เวลา` (Timestamp)

### 3. ✨ Premium Vector UI (Strictly Zero Emojis)
- **100% Emoji-Free**: Every childish emoji has been replaced with clean, minimalist inline vector SVGs (gear, trophy, gift box, speaker, music note, fullscreen, lock, download arrow, etc.).
- **Anniversary Luxury Theme**: Polished dark sapphire glassmorphism, royal gold borders (`#ffd700`, `#f59e0b`), metallic bevels, and Cinzel/Inter typography.

### 4. ⏱️ 15-Second Suspense Spin & Manual Override
- **15-Second Suspense Spin**: Starts fast, sustains rolling momentum, and progressively decelerates over the final ~6.5 seconds with a custom power-curve easing to build maximum stage tension.
- **Instant Spacebar Override**: Press **Spacebar** once to start; press Spacebar again at any time while spinning to forcefully override the 15-second timer and brake into the winner in ~1.5s.
- **Infinite Virtual Loop**: Uses a virtual card carousel that recycles cards infinitely through the participant pool. The reel **never runs out of cards**, eliminating blank spaces or visual popping.

### 5. 🎯 Mathematical Pointer Alignment on Stop
- Viewport height: `288px` (3 visible cards of `96px`).
- Center highlighted band spans `top: 96px` to `192px` (centerline `144px`).
- Center laser pointers (`▶` and `◀`) are positioned at `top: 144px`.
- Final `translateY` is mathematically calculated as `(targetIndex - 1) * 96px`, ensuring the winner card lands **dead-center** between the pointers with 0-pixel error.

### 6. 📐 Screen Configuration & Stage Calibration
- Located inside the protected Settings modal under **"Screen Calibration"**:
  - **Stage Scale / Zoom %**: Adjust between 60% and 140% for ultra-wide projector calibration.
  - **Max Width / Height (px)**: Constrain layout bounds to specific stage LED processor resolutions.
  - **Spin Console Left Offset**: Move the spin machine horizontally to calibrate exact stage overlap on LED walls.
  - **History Panel Right Offset**: Adjust right panel margin for curved or bezel displays.
- Persists in `localStorage` across page refreshes.

### 7. 🏆 Minimalist Winner Overlay (Zero Distracting Buttons)
- Clean, focused stage announcement:
  - Giant glowing Winner Name, Department (`HQ - DS` / `SBK`), Employee ID, and Prize Card.
  - **Zero Action Buttons**: Eliminates confusing "Claim" or "Redraw" buttons on screen.
  - **Keyboard Driven**: Press **`Enter`** (or click anywhere on overlay) to confirm the winner, update the history panel, and prepare the UI for the next spin.
  - Subtle pulsing hint: `Press [ ENTER ] to continue`.

### 8. 📜 Permanent Winner History Panel
- The Winner History panel on the right side remains **permanently visible at all times**:
  - Never auto-hides during spin animations.
  - Never collapses when settings or other panels are opened.
  - Audience can always see the live-updating record of past winners.

---

## ⌨️ Keyboard Shortcuts Reference

| Shortcut | Action |
|---|---|
| **`SPACEBAR`** | **Spin** (when idle) / **Force Stop Override** (when spinning) |
| **`ENTER`** | **Confirm Winner & Dismiss** (when winner overlay is open) |
| **`S`** | Open **Admin Login / Settings** |
| **`P`** | **Pre-Spin Reveal** for current prize |
| **`M`** | Toggle **Sound Effects (SFX)** mute/unmute |
| **`F`** | Toggle **Fullscreen** mode |

---

## 🚀 Running Locally

```bash
# Start local server
python3 -m http.server 8000

# Open in browser:
# http://localhost:8000/public/index.html
```
