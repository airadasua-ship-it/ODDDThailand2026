import json
import os
import shutil

with open('public/participants_fallback.json', 'r', encoding='utf-8') as f:
    participants_raw = f.read().strip()

default_prizes = [
    {
        "id": "prize_1",
        "name": "MacBook Pro 16\" M3 Max",
        "tier": "Grand Prize",
        "quantity": 1,
        "remaining": 1,
        "notes": "Space Black • 36GB Unified Memory",
        "image": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200' width='200' height='200'><defs><linearGradient id='mb' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%23ffd700'/><stop offset='100%' stop-color='%23b8860b'/></linearGradient><linearGradient id='screen' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%231e293b'/><stop offset='100%' stop-color='%230f172a'/></linearGradient></defs><rect width='200' height='200' rx='28' fill='%23131722'/><rect x='35' y='45' width='130' height='85' rx='8' fill='url(%23mb)' stroke='%23ffd700' stroke-width='2'/><rect x='42' y='52' width='116' height='71' rx='4' fill='url(%23screen)'/><circle cx='100' cy='88' r='12' fill='%23ffd700' opacity='0.9'/><path d='M20 135 L180 135 L170 148 L30 148 Z' fill='url(%23mb)' stroke='%23ffe082' stroke-width='1.5'/><rect x='85' y='136' width='30' height='4' rx='2' fill='%23334155'/><text x='100' y='180' text-anchor='middle' fill='%23ffd700' font-family='sans-serif' font-weight='bold' font-size='13'>GRAND PRIZE</text></svg>"
    },
    {
        "id": "prize_2",
        "name": "iPhone 16 Pro 256GB",
        "tier": "1st Prize",
        "quantity": 2,
        "remaining": 2,
        "notes": "Natural Titanium • Super Retina XDR",
        "image": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200' width='200' height='200'><defs><linearGradient id='ip' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%23f59e0b'/><stop offset='100%' stop-color='%23d97706'/></linearGradient></defs><rect width='200' height='200' rx='28' fill='%23131722'/><rect x='65' y='30' width='70' height='125' rx='18' fill='%231e293b' stroke='url(%23ip)' stroke-width='3'/><rect x='70' y='36' width='60' height='113' rx='14' fill='%230b0f19'/><rect x='85' y='40' width='30' height='8' rx='4' fill='%231e293b'/><circle cx='80' cy='55' r='5' fill='%23f59e0b'/><circle cx='95' cy='55' r='5' fill='%23f59e0b'/><circle cx='88' cy='67' r='5' fill='%23f59e0b'/><text x='100' y='180' text-anchor='middle' fill='%23f59e0b' font-family='sans-serif' font-weight='bold' font-size='13'>1ST PRIZE</text></svg>"
    },
    {
        "id": "prize_3",
        "name": "iPad Air 13\" M2",
        "tier": "2nd Prize",
        "quantity": 3,
        "remaining": 3,
        "notes": "Starlight • Liquid Retina Display",
        "image": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200' width='200' height='200'><defs><linearGradient id='ipad' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%2338bdf8'/><stop offset='100%' stop-color='%230284c7'/></linearGradient></defs><rect width='200' height='200' rx='28' fill='%23131722'/><rect x='45' y='35' width='110' height='115' rx='14' fill='%231e293b' stroke='url(%23ipad)' stroke-width='3'/><rect x='51' y='41' width='98' height='103' rx='10' fill='%23082f49'/><circle cx='100' cy='92' r='18' fill='url(%23ipad)' opacity='0.8'/><text x='100' y='180' text-anchor='middle' fill='%2338bdf8' font-family='sans-serif' font-weight='bold' font-size='13'>2ND PRIZE</text></svg>"
    },
    {
        "id": "prize_4",
        "name": "Apple Watch Series 10",
        "tier": "3rd Prize",
        "quantity": 5,
        "remaining": 5,
        "notes": "Jet Black Aluminum Case",
        "image": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200' width='200' height='200'><defs><linearGradient id='aw' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%23ec4899'/><stop offset='100%' stop-color='%23be185d'/></linearGradient></defs><rect width='200' height='200' rx='28' fill='%23131722'/><rect x='80' y='20' width='40' height='145' rx='8' fill='%23334155'/><rect x='68' y='52' width='64' height='76' rx='18' fill='%230f172a' stroke='url(%23aw)' stroke-width='3'/><circle cx='100' cy='90' r='18' stroke='url(%23aw)' stroke-width='3' fill='none'/><line x1='100' y1='90' x2='100' y2='79' stroke='%23f472b6' stroke-width='2' stroke-linecap='round'/><line x1='100' y1='90' x2='110' y2='90' stroke='%23f472b6' stroke-width='2' stroke-linecap='round'/><text x='100' y='185' text-anchor='middle' fill='%23ec4899' font-family='sans-serif' font-weight='bold' font-size='13'>3RD PRIZE</text></svg>"
    },
    {
        "id": "prize_5",
        "name": "Lucky Ang Pao 10,000 THB",
        "tier": "Special Prize",
        "quantity": 10,
        "remaining": 10,
        "notes": "Red Packet Cash Reward",
        "image": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200' width='200' height='200'><defs><linearGradient id='ap' x1='0%' y1='0%' x2='100%' y2='100%'><stop offset='0%' stop-color='%23ef4444'/><stop offset='100%' stop-color='%23b91c1c'/></linearGradient></defs><rect width='200' height='200' rx='28' fill='%23131722'/><rect x='60' y='32' width='80' height='120' rx='10' fill='url(%23ap)' stroke='%23ffd700' stroke-width='2.5'/><path d='M60 40 Q100 80 140 40 Z' fill='%23dc2626' stroke='%23ffd700' stroke-width='1.5'/><circle cx='100' cy='85' r='18' fill='%23ffd700'/><text x='100' y='92' text-anchor='middle' fill='%23b91c1c' font-family='sans-serif' font-weight='bold' font-size='20'>福</text><text x='100' y='180' text-anchor='middle' fill='%23ef4444' font-family='sans-serif' font-weight='bold' font-size='13'>SPECIAL CASH</text></svg>"
    }
]

prizes_raw = json.dumps(default_prizes)

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>D&D Annual Lucky Draw | Grand Celebration Spin</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Inter:wght@400;500;600;700;800&family=Kanit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --gold-primary: #f59e0b;
      --gold-light: #fde68a;
      --gold-dark: #b45309;
      --gold-glow: rgba(245, 158, 11, 0.45);
      --gold-gradient: linear-gradient(135deg, #fef08a 0%, #f59e0b 50%, #b45309 100%);
      --gold-border: 1px solid rgba(245, 158, 11, 0.4);
      --glass-bg: rgba(11, 15, 25, 0.78);
      --glass-bg-hover: rgba(17, 24, 39, 0.88);
      --glass-border: 1px solid rgba(255, 255, 255, 0.12);
      --cyan-accent: #38bdf8;
      --cyan-glow: rgba(56, 189, 248, 0.4);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 22px;
      --radius-xl: 32px;
      --panel-width: clamp(340px, 26vw, 440px);
      --spin-width: clamp(380px, 32vw, 540px);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
    }

    body {
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      font-family: 'Inter', 'Kanit', system-ui, -apple-system, sans-serif;
      background-color: #06080f;
      color: var(--text-main);
      position: relative;
    }

    /* FULLSCREEN BACKGROUND VIDEO */
    #bgVideo {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      object-fit: cover;
      z-index: 1;
      pointer-events: none;
    }

    /* BACKGROUND OVERLAY WITH ADJUSTABLE OPACITY & RADIAL HIGHLIGHT */
    #bgOverlay {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: radial-gradient(circle at 75% 45%, rgba(6, 8, 15, 0.15) 0%, rgba(6, 8, 15, 0.65) 100%);
      z-index: 2;
      pointer-events: none;
      transition: background 0.3s ease;
    }

    /* CELEBRATION CANVAS FOR FIREWORKS & CONFETTI */
    #celebrationCanvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 90;
      pointer-events: none;
    }

    /* TOP STAGE FLOATING DOCK */
    .stage-dock {
      position: fixed;
      top: clamp(12px, 2vh, 24px);
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: clamp(8px, 1.2vw, 18px);
      background: rgba(10, 15, 29, 0.65);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: var(--glass-border);
      border-radius: 9999px;
      padding: 8px 18px;
      z-index: 40;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
      transition: opacity 0.4s ease, transform 0.4s ease;
    }

    .stage-dock.hidden-stage {
      opacity: 0.15;
      transform: translateX(-50%) translateY(-60%);
    }
    .stage-dock.hidden-stage:hover {
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }

    .dock-btn {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #e2e8f0;
      padding: 7px 14px;
      border-radius: 9999px;
      font-size: clamp(0.78rem, 0.9vw, 0.88rem);
      font-weight: 600;
      cursor: pointer;
      transition: all 0.25s ease;
      white-space: nowrap;
    }
    .dock-btn:hover {
      background: rgba(255, 255, 255, 0.18);
      border-color: var(--gold-primary);
      color: #fff;
      transform: translateY(-1px);
    }
    .dock-btn.active {
      background: var(--gold-gradient);
      color: #000;
      border-color: #fff;
      box-shadow: 0 0 16px var(--gold-glow);
    }

    .dock-pill-prize {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(245, 158, 11, 0.15);
      border: 1px solid rgba(245, 158, 11, 0.45);
      padding: 5px 14px;
      border-radius: 9999px;
      cursor: pointer;
      transition: all 0.25s ease;
    }
    .dock-pill-prize:hover {
      background: rgba(245, 158, 11, 0.28);
      box-shadow: 0 0 14px var(--gold-glow);
    }
    .dock-pill-prize .prize-tag {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #ffd700;
      background: rgba(0, 0, 0, 0.4);
      padding: 2px 7px;
      border-radius: 6px;
    }
    .dock-pill-prize .prize-name {
      font-size: clamp(0.82rem, 0.95vw, 0.92rem);
      font-weight: 700;
      color: #fff;
      max-width: 220px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    /* LEFT SIDE SPIN CONTAINER - DELIBERATELY OVERLAPPING THE D&D TEXT AREA */
    .spin-stage-container {
      position: absolute;
      left: clamp(20px, 4.5vw, 85px);
      top: 50%;
      transform: translateY(-50%);
      width: var(--spin-width);
      z-index: 20;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: clamp(14px, 2vh, 22px);
      pointer-events: auto;
    }

    /* LUXURY TITLE & ACTIVE PRIZE BANNER */
    .spin-header {
      width: 100%;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
    }

    .spin-title {
      font-family: 'Cinzel', serif;
      font-size: clamp(1.4rem, 2.2vw, 2.2rem);
      font-weight: 900;
      letter-spacing: 0.12em;
      background: var(--gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      text-shadow: 0 0 25px rgba(245, 158, 11, 0.4);
      text-transform: uppercase;
    }

    .active-prize-card {
      width: 100%;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid rgba(245, 158, 11, 0.35);
      border-radius: var(--radius-md);
      padding: 10px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    .prize-info-left {
      display: flex;
      align-items: center;
      gap: 12px;
      overflow: hidden;
    }
    .prize-thumb-mini {
      width: 44px;
      height: 44px;
      border-radius: 8px;
      object-fit: cover;
      background: #1e293b;
      border: 1px solid rgba(245, 158, 11, 0.4);
      flex-shrink: 0;
    }
    .prize-text-wrap {
      display: flex;
      flex-direction: column;
      text-align: left;
      overflow: hidden;
    }
    .prize-tier-badge {
      font-size: 0.68rem;
      font-weight: 800;
      color: var(--gold-primary);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .prize-title-display {
      font-size: clamp(0.95rem, 1.1vw, 1.15rem);
      font-weight: 700;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .prize-remain-badge {
      font-size: 0.76rem;
      font-weight: 600;
      color: var(--text-muted);
    }
    .btn-reveal-prize {
      background: rgba(245, 158, 11, 0.2);
      border: 1px solid var(--gold-primary);
      color: #fef08a;
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      transition: all 0.25s ease;
      flex-shrink: 0;
    }
    .btn-reveal-prize:hover {
      background: var(--gold-gradient);
      color: #000;
      box-shadow: 0 0 14px var(--gold-glow);
    }

    /* MAIN SLOT MACHINE CONSOLE */
    .slot-machine-frame {
      width: 100%;
      background: linear-gradient(180deg, rgba(17, 24, 39, 0.92) 0%, rgba(10, 15, 29, 0.95) 100%);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 2px solid rgba(245, 158, 11, 0.55);
      border-radius: var(--radius-xl);
      padding: clamp(14px, 2vh, 22px);
      box-shadow: 0 0 45px rgba(245, 158, 11, 0.25), 0 25px 60px rgba(0, 0, 0, 0.7);
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }

    /* GOLD CORNER ACCENTS */
    .slot-corner {
      position: absolute;
      width: 18px;
      height: 18px;
      border-color: #ffd700;
      pointer-events: none;
    }
    .slot-corner.tl { top: 10px; left: 10px; border-top: 3px solid #ffd700; border-left: 3px solid #ffd700; border-top-left-radius: 8px; }
    .slot-corner.tr { top: 10px; right: 10px; border-top: 3px solid #ffd700; border-right: 3px solid #ffd700; border-top-right-radius: 8px; }
    .slot-corner.bl { bottom: 10px; left: 10px; border-bottom: 3px solid #ffd700; border-left: 3px solid #ffd700; border-bottom-left-radius: 8px; }
    .slot-corner.br { bottom: 10px; right: 10px; border-bottom: 3px solid #ffd700; border-right: 3px solid #ffd700; border-bottom-right-radius: 8px; }

    /* SLOT VIEWPORT (3 ITEMS VISIBLE, 1 CENTER WINNER HIGHLIGHT) */
    .slot-viewport {
      width: 100%;
      height: 288px; /* 3 x 96px items */
      background: rgba(6, 9, 18, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-lg);
      position: relative;
      overflow: hidden;
      box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.8);
    }

    /* TOP & BOTTOM SHADOW GRADIENTS FOR 3D DRUM DEPTH */
    .slot-gradient-top {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 85px;
      background: linear-gradient(180deg, rgba(6, 9, 18, 0.95) 0%, rgba(6, 9, 18, 0) 100%);
      z-index: 8;
      pointer-events: none;
    }
    .slot-gradient-bottom {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 85px;
      background: linear-gradient(0deg, rgba(6, 9, 18, 0.95) 0%, rgba(6, 9, 18, 0) 100%);
      z-index: 8;
      pointer-events: none;
    }

    /* CENTER TARGET FRAME WITH GLOW & POINTERS */
    .slot-target-frame {
      position: absolute;
      top: 96px;
      left: 0;
      width: 100%;
      height: 96px;
      border-top: 2px solid rgba(245, 158, 11, 0.85);
      border-bottom: 2px solid rgba(245, 158, 11, 0.85);
      background: linear-gradient(90deg, rgba(245, 158, 11, 0.12) 0%, rgba(245, 158, 11, 0.22) 50%, rgba(245, 158, 11, 0.12) 100%);
      box-shadow: 0 0 30px rgba(245, 158, 11, 0.35);
      z-index: 5;
      pointer-events: none;
      transition: all 0.25s ease;
    }
    .slot-target-frame.winner-locked {
      border-color: #ffd700;
      background: linear-gradient(90deg, rgba(255, 215, 0, 0.25) 0%, rgba(255, 215, 0, 0.45) 50%, rgba(255, 215, 0, 0.25) 100%);
      box-shadow: 0 0 50px rgba(255, 215, 0, 0.7);
    }

    .slot-pointer {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      font-size: 1.5rem;
      color: #ffd700;
      filter: drop-shadow(0 0 8px rgba(255, 215, 0, 0.8));
      z-index: 9;
      pointer-events: none;
      animation: pulsePointer 1.4s infinite ease-in-out;
    }
    .slot-pointer.left { left: 10px; }
    .slot-pointer.right { right: 10px; }

    @keyframes pulsePointer {
      0%, 100% { transform: translateY(-50%) scale(1); }
      50% { transform: translateY(-50%) scale(1.22); }
    }

    /* THE ROLLING DRUM TRACK */
    .slot-drum-track {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      will-change: transform;
    }

    /* INDIVIDUAL PARTICIPANT CARD (HEIGHT 96px) */
    .participant-card {
      width: 100%;
      height: 96px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0 35px;
      gap: 16px;
      box-sizing: border-box;
      transition: opacity 0.2s, transform 0.2s;
    }
    .participant-card .card-content {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      gap: 4px;
      width: 100%;
    }
    .participant-dept-pill {
      display: inline-flex;
      align-items: center;
      padding: 2px 10px;
      border-radius: 9999px;
      font-size: clamp(0.72rem, 0.85vw, 0.82rem);
      font-weight: 800;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      background: rgba(245, 158, 11, 0.2);
      border: 1px solid rgba(245, 158, 11, 0.5);
      color: #fde68a;
    }
    .participant-dept-pill.hq {
      background: linear-gradient(135deg, rgba(239, 68, 68, 0.3) 0%, rgba(245, 158, 11, 0.4) 100%);
      border-color: #f87171;
      color: #fff;
      box-shadow: 0 0 10px rgba(239, 68, 68, 0.35);
    }
    .participant-name {
      font-size: clamp(1.4rem, 2vw, 1.85rem);
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 0.03em;
      text-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 90%;
    }
    .participant-id {
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--text-muted);
      letter-spacing: 0.05em;
    }

    /* CONTROLS AREA BELOW SLOT */
    .slot-actions {
      width: 100%;
      margin-top: 18px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }

    .btn-spin-main {
      width: 100%;
      height: clamp(58px, 7.5vh, 72px);
      background: var(--gold-gradient);
      border: 2px solid #fff;
      border-radius: 9999px;
      color: #0b0f19;
      font-family: 'Cinzel', 'Inter', sans-serif;
      font-size: clamp(1.15rem, 1.4vw, 1.45rem);
      font-weight: 900;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      box-shadow: 0 0 35px var(--gold-glow), 0 8px 25px rgba(0, 0, 0, 0.5);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
      overflow: hidden;
    }
    .btn-spin-main:hover {
      transform: translateY(-2px) scale(1.02);
      box-shadow: 0 0 50px rgba(245, 158, 11, 0.7), 0 12px 35px rgba(0, 0, 0, 0.6);
    }
    .btn-spin-main:active {
      transform: translateY(1px) scale(0.98);
    }
    .btn-spin-main.is-spinning {
      background: linear-gradient(135deg, #ef4444 0%, #dc2626 50%, #991b1b 100%);
      color: #ffffff;
      border-color: #fca5a5;
      box-shadow: 0 0 40px rgba(239, 68, 68, 0.6);
      animation: pulseSpinBtn 1s infinite alternate;
    }
    @keyframes pulseSpinBtn {
      0% { transform: scale(1); }
      100% { transform: scale(1.03); }
    }

    .spin-kbd-hint {
      display: inline-flex;
      align-items: center;
      padding: 3px 10px;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.3);
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 800;
      letter-spacing: 0.05em;
    }

    .slot-status-bar {
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 8px;
      font-size: 0.82rem;
      color: var(--text-muted);
      font-weight: 600;
    }
    .pool-counter-badge {
      color: var(--gold-light);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .pool-counter-badge .dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
    }

    /* COLLAPSIBLE SIDE PANELS (LEFT = SETTINGS, RIGHT = HISTORY) */
    .panel-drawer {
      position: fixed;
      top: 0;
      height: 100vh;
      width: var(--panel-width);
      background: rgba(10, 15, 28, 0.88);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border-top: none;
      border-bottom: none;
      z-index: 60;
      display: flex;
      flex-direction: column;
      box-shadow: 0 0 50px rgba(0, 0, 0, 0.75);
      transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .panel-drawer.left {
      left: 0;
      border-right: 1px solid rgba(245, 158, 11, 0.3);
      transform: translateX(-100%);
    }
    .panel-drawer.left.open {
      transform: translateX(0);
    }
    .panel-drawer.right {
      right: 0;
      border-left: 1px solid rgba(245, 158, 11, 0.3);
      transform: translateX(100%);
    }
    .panel-drawer.right.open {
      transform: translateX(0);
    }

    /* EDGE TOGGLE HANDLES TO EXPAND DRAWERS */
    .edge-handle {
      position: fixed;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(14px);
      border: 1px solid rgba(245, 158, 11, 0.4);
      color: var(--gold-light);
      padding: 14px 10px;
      cursor: pointer;
      z-index: 55;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
      transition: all 0.3s ease;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .edge-handle:hover {
      background: rgba(245, 158, 11, 0.25);
      border-color: #ffd700;
      color: #fff;
    }
    .edge-handle.left {
      left: 0;
      border-top-right-radius: 14px;
      border-bottom-right-radius: 14px;
      border-left: none;
    }
    .edge-handle.right {
      right: 0;
      border-top-left-radius: 14px;
      border-bottom-left-radius: 14px;
      border-right: none;
    }

    /* PANEL HEADER & TABS */
    .panel-header {
      padding: 18px 22px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(0, 0, 0, 0.2);
    }
    .panel-title {
      font-family: 'Cinzel', serif;
      font-size: 1.15rem;
      font-weight: 800;
      color: #ffd700;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .panel-close-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #cbd5e1;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      transition: all 0.2s ease;
    }
    .panel-close-btn:hover {
      background: #ef4444;
      color: #fff;
      border-color: #ef4444;
    }

    .panel-tabs {
      display: flex;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(0, 0, 0, 0.25);
    }
    .panel-tab {
      flex: 1;
      padding: 12px 6px;
      text-align: center;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.2s ease;
      white-space: nowrap;
    }
    .panel-tab:hover {
      color: #fff;
      background: rgba(255, 255, 255, 0.04);
    }
    .panel-tab.active {
      color: #ffd700;
      border-bottom-color: #ffd700;
      background: rgba(245, 158, 11, 0.08);
    }

    .panel-body {
      flex: 1;
      overflow-y: auto;
      padding: 18px 22px;
      display: flex;
      flex-direction: column;
      gap: 18px;
    }
    .panel-body::-webkit-scrollbar {
      width: 6px;
    }
    .panel-body::-webkit-scrollbar-thumb {
      background: rgba(245, 158, 11, 0.35);
      border-radius: 9999px;
    }

    /* FORM STYLES */
    .form-group {
      display: flex;
      flex-direction: column;
      gap: 7px;
    }
    .form-label {
      font-size: 0.82rem;
      font-weight: 700;
      color: #e2e8f0;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .form-input, .form-textarea, .form-select {
      width: 100%;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-sm);
      padding: 10px 14px;
      color: #fff;
      font-size: 0.88rem;
      outline: none;
      transition: border-color 0.2s;
    }
    .form-input:focus, .form-textarea:focus, .form-select:focus {
      border-color: var(--gold-primary);
      box-shadow: 0 0 10px rgba(245, 158, 11, 0.3);
    }

    .btn-secondary {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      padding: 9px 16px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      transition: all 0.2s;
    }
    .btn-secondary:hover {
      background: rgba(255, 255, 255, 0.16);
      border-color: #fff;
    }
    .btn-primary {
      background: var(--gold-gradient);
      border: none;
      color: #0b0f19;
      padding: 9px 16px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      transition: all 0.2s;
    }
    .btn-primary:hover {
      box-shadow: 0 0 16px var(--gold-glow);
      transform: translateY(-1px);
    }
    .btn-danger {
      background: rgba(239, 68, 68, 0.18);
      border: 1px solid #ef4444;
      color: #fca5a5;
      padding: 9px 16px;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
      transition: all 0.2s;
    }
    .btn-danger:hover {
      background: #ef4444;
      color: #fff;
    }

    /* PRIZE MANAGER CARDS */
    .prize-item-row {
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(15, 23, 42, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: var(--radius-md);
      padding: 10px 14px;
      transition: all 0.2s;
    }
    .prize-item-row.is-active {
      border-color: #ffd700;
      background: rgba(245, 158, 11, 0.12);
      box-shadow: 0 0 14px rgba(245, 158, 11, 0.2);
    }
    .prize-item-thumb {
      width: 48px;
      height: 48px;
      border-radius: 8px;
      object-fit: cover;
      background: #1e293b;
      border: 1px solid rgba(245, 158, 11, 0.3);
      flex-shrink: 0;
    }
    .prize-item-info {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 2px;
      overflow: hidden;
    }
    .prize-item-title {
      font-size: 0.9rem;
      font-weight: 700;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .prize-item-sub {
      font-size: 0.75rem;
      color: var(--text-muted);
    }
    .prize-item-actions {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .btn-icon {
      width: 30px;
      height: 30px;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #cbd5e1;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 0.85rem;
      transition: all 0.2s;
    }
    .btn-icon:hover {
      background: rgba(255, 255, 255, 0.2);
      color: #fff;
    }

    /* WINNER HISTORY CARDS */
    .winner-card {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid rgba(245, 158, 11, 0.25);
      border-radius: var(--radius-md);
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      position: relative;
      transition: all 0.2s;
    }
    .winner-card:hover {
      border-color: #ffd700;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(0, 0, 0, 0.4);
    }
    .winner-card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .winner-rank {
      font-family: 'Cinzel', serif;
      font-size: 0.78rem;
      font-weight: 800;
      color: #ffd700;
      background: rgba(245, 158, 11, 0.15);
      padding: 2px 8px;
      border-radius: 4px;
    }
    .winner-time {
      font-size: 0.72rem;
      color: var(--text-muted);
    }
    .winner-details {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .winner-name-display {
      font-size: 1.15rem;
      font-weight: 800;
      color: #fff;
    }
    .winner-prize-banner {
      font-size: 0.78rem;
      color: var(--gold-light);
      background: rgba(0, 0, 0, 0.35);
      padding: 4px 8px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .btn-redraw-winner {
      align-self: flex-end;
      background: transparent;
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #f87171;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }
    .btn-redraw-winner:hover {
      background: #ef4444;
      color: #fff;
    }

    /* MODAL OVERLAY & DIALOGS */
    .modal-backdrop {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(4, 6, 14, 0.85);
      backdrop-filter: blur(18px);
      -webkit-backdrop-filter: blur(18px);
      z-index: 120;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
      padding: 20px;
    }
    .modal-backdrop.open {
      opacity: 1;
      pointer-events: auto;
    }

    .modal-dialog {
      background: linear-gradient(180deg, #131b2e 0%, #0a0f1d 100%);
      border: 2px solid rgba(245, 158, 11, 0.6);
      border-radius: var(--radius-xl);
      box-shadow: 0 0 60px rgba(245, 158, 11, 0.35), 0 30px 80px rgba(0, 0, 0, 0.85);
      width: clamp(340px, 90vw, 560px);
      max-height: 90vh;
      overflow-y: auto;
      padding: clamp(24px, 3vh, 36px);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      transform: scale(0.92);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .modal-backdrop.open .modal-dialog {
      transform: scale(1);
    }

    /* PRE-SPIN PRIZE REVEAL MODAL */
    .prize-reveal-modal {
      width: clamp(360px, 92vw, 640px);
    }
    .prize-reveal-badge {
      font-family: 'Cinzel', serif;
      font-size: 0.85rem;
      font-weight: 800;
      letter-spacing: 0.15em;
      color: #ffd700;
      background: rgba(245, 158, 11, 0.2);
      border: 1px solid var(--gold-primary);
      padding: 6px 18px;
      border-radius: 9999px;
      margin-bottom: 16px;
    }
    .prize-reveal-img {
      width: clamp(160px, 24vw, 240px);
      height: clamp(160px, 24vw, 240px);
      object-fit: contain;
      border-radius: var(--radius-lg);
      background: #0b0f19;
      border: 2px solid rgba(245, 158, 11, 0.5);
      box-shadow: 0 0 40px rgba(245, 158, 11, 0.3);
      margin-bottom: 18px;
    }
    .prize-reveal-name {
      font-family: 'Cinzel', 'Inter', sans-serif;
      font-size: clamp(1.6rem, 2.4vw, 2.2rem);
      font-weight: 900;
      background: var(--gold-gradient);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 8px;
    }
    .prize-reveal-notes {
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-bottom: 22px;
      max-width: 80%;
    }

    /* GRAND WINNER SPOTLIGHT MODAL */
    .winner-spotlight-modal {
      width: clamp(380px, 92vw, 680px);
      border-color: #ffd700;
      box-shadow: 0 0 80px rgba(255, 215, 0, 0.5), 0 30px 90px rgba(0, 0, 0, 0.9);
    }
    .winner-spotlight-header {
      font-family: 'Cinzel', serif;
      font-size: clamp(1.2rem, 1.8vw, 1.6rem);
      font-weight: 900;
      letter-spacing: 0.15em;
      color: #ffd700;
      text-transform: uppercase;
      margin-bottom: 6px;
    }
    .winner-spotlight-name {
      font-size: clamp(2.4rem, 4vw, 3.8rem);
      font-weight: 900;
      color: #ffffff;
      letter-spacing: 0.02em;
      text-shadow: 0 0 35px rgba(255, 215, 0, 0.7);
      margin: 10px 0;
      line-height: 1.1;
    }
    .winner-dept-badge-large {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 18px;
      border-radius: 9999px;
      font-size: clamp(0.95rem, 1.2vw, 1.2rem);
      font-weight: 800;
      text-transform: uppercase;
      background: linear-gradient(135deg, rgba(245, 158, 11, 0.3) 0%, rgba(239, 68, 68, 0.4) 100%);
      border: 1.5px solid #ffd700;
      color: #fff;
      box-shadow: 0 0 20px rgba(245, 158, 11, 0.4);
      margin-bottom: 20px;
    }
    .winner-prize-card-large {
      width: 100%;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(245, 158, 11, 0.4);
      border-radius: var(--radius-md);
      padding: 14px 20px;
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 24px;
      text-align: left;
    }
    .winner-prize-img-large {
      width: 64px;
      height: 64px;
      object-fit: contain;
      border-radius: 8px;
      background: #0b0f19;
      border: 1px solid rgba(245, 158, 11, 0.4);
    }

    /* TOAST ALERTS */
    .toast-container {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      flex-direction: column;
      gap: 8px;
      z-index: 150;
      pointer-events: none;
    }
    .toast-message {
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(245, 158, 11, 0.5);
      border-radius: 9999px;
      padding: 10px 22px;
      color: #fff;
      font-size: 0.88rem;
      font-weight: 600;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
      animation: fadeInOut 3s forwards;
    }
    @keyframes fadeInOut {
      0% { opacity: 0; transform: translateY(12px); }
      15% { opacity: 1; transform: translateY(0); }
      85% { opacity: 1; transform: translateY(0); }
      100% { opacity: 0; transform: translateY(-12px); }
    }

    /* ULTRA-WIDE STAGE RESPONSIVENESS */
    @media (min-aspect-ratio: 21/9) {
      :root {
        --panel-width: clamp(380px, 20vw, 500px);
        --spin-width: clamp(440px, 26vw, 620px);
      }
      .spin-stage-container {
        left: clamp(40px, 6vw, 140px);
      }
    }

    @media (max-width: 900px) {
      .spin-stage-container {
        left: 50%;
        transform: translate(-50%, -50%);
        width: 92vw;
      }
    }
  </style>
</head>
<body>

  <!-- FULLSCREEN BACKGROUND VIDEO -->
  <video id="bgVideo" autoplay loop muted playsinline poster="D&D2026_1920x1080.jpg">
    <source src="bg.mp4" type="video/mp4">
    <source src="./bg.mp4" type="video/mp4">
    <source src="public/bg.mp4" type="video/mp4">
    <source src="<b>public<b>/<b>bg.mp4<:b>./Fireworks_exploding_behind_castle_20261018181317.mp4" type="video/mp4">
  </video>

  <!-- BACKGROUND OVERLAY -->
  <div id="bgOverlay"></div>

  <!-- CELEBRATION CANVAS -->
  <canvas id="celebrationCanvas"></canvas>

  <!-- TOP STAGE FLOATING DOCK -->
  <div class="stage-dock" id="stageDock">
    <button class="dock-btn" id="btnToggleSettingsDock" title="Toggle Settings (Hotkey: S)">
      ⚙️ <span>Settings</span>
    </button>

    <div class="dock-pill-prize" id="dockPrizePill" title="Click to Reveal Current Prize (Hotkey: P)">
      <span class="prize-tag" id="dockPrizeTier">GRAND</span>
      <span class="prize-name" id="dockPrizeName">MacBook Pro 16" M3 Max</span>
      <span style="font-size: 0.85rem;">🎁</span>
    </div>

    <button class="dock-btn" id="btnToggleBgm" title="Toggle Background Music">
      🎵 <span id="bgmLabel">BGM: OFF</span>
    </button>

    <button class="dock-btn" id="btnToggleSfx" title="Toggle Sound Effects (Hotkey: M)">
      🔊 <span id="sfxLabel">SFX: ON</span>
    </button>

    <button class="dock-btn" id="btnToggleStageMode" title="Clean Stage Presentation (Hotkey: H)">
      🎭 <span>Stage Mode</span>
    </button>

    <button class="dock-btn" id="btnToggleFullscreen" title="Fullscreen (Hotkey: F)">
      ⛶ <span>Fullscreen</span>
    </button>

    <button class="dock-btn" id="btnToggleHistoryDock" title="Toggle Winners List (Hotkey: W)">
      🏆 <span id="dockWinnerCount">Winners (0)</span>
    </button>
  </div>

  <!-- EDGE TOGGLE HANDLES -->
  <div class="edge-handle left" id="leftEdgeHandle" title="Open Settings (S)">
    <span>⚙️</span>
    <span style="writing-mode: vertical-rl; transform: rotate(180deg);">SETTINGS</span>
  </div>
  <div class="edge-handle right" id="rightEdgeHandle" title="Open Winners (W)">
    <span>🏆</span>
    <span style="writing-mode: vertical-rl; transform: rotate(180deg);" id="rightEdgeCount">WINNERS (0)</span>
  </div>

  <!-- LEFT SIDE SPIN CONTAINER (OVERLAPS D&D LOGO AREA) -->
  <div class="spin-stage-container" id="spinContainer">
    <div class="spin-header">
      <h1 class="spin-title">D&D LUCKY DRAW</h1>

      <!-- ACTIVE PRIZE CARD -->
      <div class="active-prize-card" id="activePrizeCard">
        <div class="prize-info-left">
          <img src="" alt="Prize" class="prize-thumb-mini" id="activePrizeThumb">
          <div class="prize-text-wrap">
            <span class="prize-tier-badge" id="activePrizeTier">GRAND PRIZE</span>
            <span class="prize-title-display" id="activePrizeTitle">MacBook Pro 16"</span>
            <span class="prize-remain-badge" id="activePrizeRemaining">1 of 1 remaining</span>
          </div>
        </div>
        <button class="btn-reveal-prize" id="btnRevealPrizeQuick">
          🎁 Reveal
        </button>
      </div>
    </div>

    <!-- MAIN SLOT MACHINE CONSOLE -->
    <div class="slot-machine-frame">
      <div class="slot-corner tl"></div>
      <div class="slot-corner tr"></div>
      <div class="slot-corner bl"></div>
      <div class="slot-corner br"></div>

      <div class="slot-viewport" id="slotViewport">
        <div class="slot-gradient-top"></div>
        <div class="slot-gradient-bottom"></div>
        <div class="slot-target-frame" id="slotTargetFrame"></div>
        <div class="slot-pointer left">▶</div>
        <div class="slot-pointer right">◀</div>

        <!-- ROLLING DRUM TRACK -->
        <div class="slot-drum-track" id="slotDrumTrack"></div>
      </div>

      <!-- ACTIONS -->
      <div class="slot-actions">
        <button class="btn-spin-main" id="btnSpinMain">
          <span id="spinBtnIcon">🎰</span>
          <span id="spinBtnText">START SPIN</span>
          <span class="spin-kbd-hint">SPACE</span>
        </button>

        <div class="slot-status-bar">
          <span class="pool-counter-badge">
            <span class="dot"></span>
            <span id="poolStatusText">510 In Pool</span>
          </span>
          <span style="font-size: 0.76rem;" id="spinTipText">Press SPACE to spin</span>
        </div>
      </div>
    </div>
  </div>

  <!-- LEFT PANEL: SETTINGS & CONTROLS -->
  <div class="panel-drawer left" id="settingsDrawer">
    <div class="panel-header">
      <div class="panel-title">
        <span>⚙️</span> Controls & Settings
      </div>
      <button class="panel-close-btn" id="btnCloseSettings">✕</button>
    </div>

    <div class="panel-tabs">
      <div class="panel-tab active" data-tab="tab-sheet">Sheet Sync</div>
      <div class="panel-tab" data-tab="tab-prizes">Prizes</div>
      <div class="panel-tab" data-tab="tab-sound">Audio / BGM</div>
      <div class="panel-tab" data-tab="tab-system">Stage / Reset</div>
    </div>

    <div class="panel-body">
      <!-- TAB 1: GOOGLE SHEET SYNC -->
      <div class="tab-content" id="tab-sheet">
        <div class="form-group">
          <label class="form-label">Published Google Sheet CSV URL</label>
          <input type="text" class="form-input" id="sheetUrlInput" placeholder="https://docs.google.com/spreadsheets/d/.../pub?output=csv">
          <span style="font-size: 0.74rem; color: var(--text-muted); line-height: 1.4;">
            Mapping: Col A = ID, Col B = Name, Col C = Dept, Col D = Division.<br>
            HQ Rule: Dept "HQ" + Division displays as <b>HQ - [Division]</b>.
          </span>
        </div>

        <div style="display: flex; gap: 8px;">
          <button class="btn-primary" id="btnSyncSheet" style="flex: 1;">
            🔄 Sync Google Sheet
          </button>
          <button class="btn-secondary" id="btnResetDefaultSheet" title="Reset to default URL">
            Default
          </button>
        </div>

        <div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; border: 1px solid rgba(255,255,255,0.08); font-size: 0.8rem; display: flex; flex-direction: column; gap: 6px;">
          <div style="display: flex; justify-content: space-between;">
            <span style="color: var(--text-muted);">Total Participants:</span>
            <strong id="statTotalParticipants" style="color: #fff;">510</strong>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span style="color: var(--text-muted);">Remaining in Pool:</span>
            <strong id="statRemainingPool" style="color: #10b981;">510</strong>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span style="color: var(--text-muted);">Total Winners Drawn:</span>
            <strong id="statWinnersDrawn" style="color: #ffd700;">0</strong>
          </div>
          <div style="display: flex; justify-content: space-between;">
            <span style="color: var(--text-muted);">Sync Status:</span>
            <span id="statSyncStatus" style="color: #38bdf8;">Loaded & Cached</span>
          </div>
        </div>
      </div>

      <!-- TAB 2: PRIZE MANAGER -->
      <div class="tab-content" id="tab-prizes" style="display: none;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.82rem; font-weight: 700; color: #ffd700;">Prizes List</span>
          <button class="btn-primary" id="btnAddPrize" style="padding: 5px 12px; font-size: 0.78rem;">
            ➕ Add Prize
          </button>
        </div>

        <div id="prizeListContainer" style="display: flex; flex-direction: column; gap: 10px;">
          <!-- Dynamically populated -->
        </div>
      </div>

      <!-- TAB 3: AUDIO & BGM -->
      <div class="tab-content" id="tab-sound" style="display: none;">
        <div class="form-group">
          <label class="form-label">
            <span>Spin & Celebration Sound FX</span>
            <span id="sfxStatusText" style="color: #10b981;">ENABLED</span>
          </label>
          <div style="display: flex; gap: 8px;">
            <button class="btn-secondary" id="btnTestTick" style="flex: 1;">Test Tick</button>
            <button class="btn-secondary" id="btnTestFanfare" style="flex: 1;">Test Fanfare</button>
          </div>
        </div>

        <div class="form-group" style="margin-top: 14px;">
          <label class="form-label">Background Music (BGM)</label>
          <div style="display: flex; gap: 8px; margin-bottom: 8px;">
            <button class="btn-primary" id="btnBgmPlayPause" style="flex: 1;">
              ▶ Play BGM
            </button>
          </div>
          <label class="form-label" style="font-size: 0.75rem; color: var(--text-muted);">BGM Volume</label>
          <input type="range" min="0" max="1" step="0.05" value="0.5" class="form-input" id="bgmVolumeSlider">
        </div>

        <div class="form-group" style="margin-top: 14px;">
          <label class="form-label">Custom BGM Audio File / URL</label>
          <input type="text" class="form-input" id="bgmUrlInput" placeholder="URL to MP3 or leave blank for synth ambient">
          <div style="margin-top: 6px;">
            <label class="btn-secondary" style="width: 100%; cursor: pointer;">
              📁 Upload Local Audio File
              <input type="file" id="bgmFileInput" accept="audio/*" style="display: none;">
            </label>
          </div>
        </div>
      </div>

      <!-- TAB 4: STAGE & SYSTEM -->
      <div class="tab-content" id="tab-system" style="display: none;">
        <div class="form-group">
          <label class="form-label">Background Video Overlay Darkness</label>
          <input type="range" min="0.1" max="0.8" step="0.05" value="0.4" class="form-input" id="overlayDarknessSlider">
          <span style="font-size: 0.72rem; color: var(--text-muted);">Increase darkness if LED stage requires higher contrast for names.</span>
        </div>

        <div class="form-group" style="margin-top: 16px;">
          <label class="form-label">Stage Clean Mode</label>
          <button class="btn-secondary" id="btnTriggerStageMode">
            🎭 Toggle Stage Mode (H)
          </button>
          <span style="font-size: 0.72rem; color: var(--text-muted);">Hides all controls and side panels for clean camera/stage shot.</span>
        </div>

        <div style="margin-top: 24px; padding-top: 18px; border-top: 1px solid rgba(255,255,255,0.1); display: flex; flex-direction: column; gap: 10px;">
          <span style="font-size: 0.8rem; font-weight: 700; color: #f87171;">Pool & Data Reset</span>
          <button class="btn-danger" id="btnResetPoolOnly">
            🔄 Reset All Winners (Restore Pool)
          </button>
          <button class="btn-secondary" id="btnFactoryReset" style="border-color: rgba(239, 68, 68, 0.4); color: #fca5a5;">
            ⚠️ Factory Reset All Settings
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- RIGHT PANEL: WINNER HISTORY -->
  <div class="panel-drawer right" id="historyDrawer">
    <div class="panel-header">
      <div class="panel-title">
        <span>🏆</span> Winners List (<span id="historyHeaderCount">0</span>)
      </div>
      <button class="panel-close-btn" id="btnCloseHistory">✕</button>
    </div>

    <div style="padding: 12px 22px; border-bottom: 1px solid rgba(255,255,255,0.1); display: flex; gap: 8px; align-items: center; background: rgba(0,0,0,0.2);">
      <button class="btn-primary" id="btnExportCsv" style="flex: 1; padding: 7px 12px; font-size: 0.8rem;">
        📥 Export Winners CSV
      </button>
      <button class="btn-secondary" id="btnClearHistoryBtn" style="padding: 7px 12px; font-size: 0.8rem;">
        Clear
      </button>
    </div>

    <div class="panel-body" id="historyListContainer">
      <!-- Winner cards dynamically populated -->
      <div id="historyEmptyState" style="text-align: center; color: var(--text-muted); padding: 40px 10px; font-size: 0.9rem;">
        No winners drawn yet.<br>Press <b>SPACE</b> to spin!
      </div>
    </div>
  </div>

  <!-- PRE-SPIN REVEAL MODAL -->
  <div class="modal-backdrop" id="prizeRevealModal">
    <div class="modal-dialog prize-reveal-modal">
      <span class="prize-reveal-badge" id="modalRevealTier">UP NEXT: GRAND PRIZE</span>
      <img src="" alt="Prize" class="prize-reveal-img" id="modalRevealImg">
      <h2 class="prize-reveal-name" id="modalRevealTitle">MacBook Pro 16"</h2>
      <p class="prize-reveal-notes" id="modalRevealNotes">Space Black • 36GB Unified Memory</p>
      <div style="margin-bottom: 24px; font-size: 0.88rem; color: #ffd700; font-weight: 700;">
        🎁 <span id="modalRevealRemaining">1 remaining in this tier</span>
      </div>
      <button class="btn-spin-main" id="btnStartDrawFromReveal" style="width: 80%;">
        READY TO DRAW!
      </button>
    </div>
  </div>

  <!-- GRAND WINNER SPOTLIGHT MODAL -->
  <div class="modal-backdrop" id="winnerModal">
    <div class="modal-dialog winner-spotlight-modal">
      <div class="winner-spotlight-header">✨ WINNER ANNOUNCEMENT ✨</div>
      <div class="winner-spotlight-name" id="modalWinnerName">Mamaew</div>
      <div class="winner-dept-badge-large" id="modalWinnerDept">
        HQ - DS &bull; ID: 0057
      </div>

      <div class="winner-prize-card-large">
        <img src="" alt="Prize" class="winner-prize-img-large" id="modalWinnerPrizeImg">
        <div style="display: flex; flex-direction: column; gap: 3px;">
          <span style="font-size: 0.74rem; font-weight: 800; color: #ffd700; text-transform: uppercase;" id="modalWinnerPrizeTier">GRAND PRIZE</span>
          <span style="font-size: 1.15rem; font-weight: 800; color: #fff;" id="modalWinnerPrizeName">MacBook Pro 16"</span>
          <span style="font-size: 0.78rem; color: var(--text-muted);" id="modalWinnerPrizeNotes">Space Black</span>
        </div>
      </div>

      <div style="display: flex; gap: 12px; width: 100%;">
        <button class="btn-primary" id="btnConfirmWinner" style="flex: 2; height: 50px; font-size: 1.05rem;">
          🏆 Claim & Continue
        </button>
        <button class="btn-danger" id="btnRedrawImmediate" style="flex: 1; height: 50px; font-size: 0.95rem;">
          🔄 Redraw
        </button>
      </div>
    </div>
  </div>

  <!-- CUSTOM CONFIRM / ALERT MODAL -->
  <div class="modal-backdrop" id="customModal">
    <div class="modal-dialog" style="width: clamp(320px, 85vw, 460px);">
      <h3 id="customModalTitle" style="font-family: 'Cinzel', serif; font-size: 1.3rem; color: #ffd700; margin-bottom: 12px;">Notice</h3>
      <p id="customModalMessage" style="font-size: 0.95rem; color: #e2e8f0; margin-bottom: 24px; line-height: 1.5;"></p>
      <div style="display: flex; gap: 10px; width: 100%; justify-content: center;" id="customModalActions">
        <button class="btn-secondary" id="customModalCancelBtn" style="flex: 1;">Cancel</button>
        <button class="btn-primary" id="customModalConfirmBtn" style="flex: 1;">Confirm</button>
      </div>
    </div>
  </div>

  <!-- PRIZE EDIT / ADD MODAL -->
  <div class="modal-backdrop" id="prizeEditModal">
    <div class="modal-dialog" style="text-align: left; align-items: stretch; width: clamp(340px, 90vw, 500px);">
      <h3 style="font-family: 'Cinzel', serif; font-size: 1.25rem; color: #ffd700; margin-bottom: 16px; text-align: center;" id="prizeEditModalTitle">
        Add Prize
      </h3>
      
      <div class="form-group" style="margin-bottom: 12px;">
        <label class="form-label">Prize Name</label>
        <input type="text" class="form-input" id="editPrizeName" placeholder="e.g. iPhone 16 Pro">
      </div>

      <div class="form-group" style="margin-bottom: 12px;">
        <label class="form-label">Tier / Category</label>
        <input type="text" class="form-input" id="editPrizeTier" placeholder="e.g. Grand Prize, 1st Prize, Gold">
      </div>

      <div class="form-group" style="margin-bottom: 12px;">
        <label class="form-label">Total Quantity</label>
        <input type="number" min="1" max="999" class="form-input" id="editPrizeQty" value="1">
      </div>

      <div class="form-group" style="margin-bottom: 12px;">
        <label class="form-label">Notes / Specs</label>
        <input type="text" class="form-input" id="editPrizeNotes" placeholder="e.g. 256GB Titanium">
      </div>

      <div class="form-group" style="margin-bottom: 18px;">
        <label class="form-label">Prize Image (JPG / PNG)</label>
        <div style="display: flex; gap: 12px; align-items: center;">
          <img src="" id="editPrizeImgPreview" style="width: 54px; height: 54px; border-radius: 8px; object-fit: contain; background: #0f172a; border: 1px solid rgba(255,255,255,0.2);">
          <label class="btn-secondary" style="flex: 1; cursor: pointer; text-align: center;">
            📷 Choose Photo
            <input type="file" id="editPrizeFileInput" accept="image/*" style="display: none;">
          </label>
        </div>
      </div>

      <div style="display: flex; gap: 10px; margin-top: 10px;">
        <button class="btn-secondary" id="btnCancelPrizeEdit" style="flex: 1;">Cancel</button>
        <button class="btn-primary" id="btnSavePrize" style="flex: 1;">Save Prize</button>
      </div>
    </div>
  </div>

  <!-- TOAST ALERTS CONTAINER -->
  <div class="toast-container" id="toastContainer"></div>

  <!-- BACKGROUND MUSIC AUDIO ELEMENT -->
  <audio id="bgmAudio" loop playsinline></audio>

  <!-- EMBEDDED FALLBACK DATA & MAIN JAVASCRIPT ENGINE -->
  <script>
    /* =====================================================================
       EMBEDDED FALLBACK PARTICIPANTS (510 PARTICIPANTS)
       ===================================================================== */
    const EMBEDDED_DEFAULT_PARTICIPANTS = ''' + participants_raw + ''';
    const EMBEDDED_DEFAULT_PRIZES = ''' + prizes_raw + ''';
    const DEFAULT_SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR_0ds0n-epkyCaX2mHzXv9VP0txJn-pD-Bj_QL63H6xvRRfdn1RMVP00L3gtX-XwCOCnbrmJlKVguU/pub?gid=0&single=true&output=csv";

    /* =====================================================================
       APP STATE
       ===================================================================== */
    const state = {
      sheetUrl: localStorage.getItem('dnd_sheet_url') || DEFAULT_SHEET_URL,
      participants: [],
      remainingPool: [],
      winners: [],
      prizes: [],
      activePrizeId: null,
      isSpinning: false,
      spinPhase: 'IDLE', // 'IDLE', 'ACCEL', 'FAST', 'STOPPING', 'SETTLING'
      sfxEnabled: true,
      bgmPlaying: false,
      stageMode: false,
      lastSpacePress: 0,
      winnerPending: null
    };

    /* =====================================================================
       WEB AUDIO SYNTHESIZER FOR SOUND EFFECTS & BGM FALLBACK
       ===================================================================== */
    class SoundEngine {
      constructor() {
        this.ctx = null;
        this.bgmOsc = null;
        this.bgmGain = null;
      }

      init() {
        if (!this.ctx) {
          const AudioCtx = window.AudioContext || window.webkitAudioContext;
          if (AudioCtx) {
            this.ctx = new AudioCtx();
          }
        }
        if (this.ctx && this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      }

      playTick(speedRatio = 1) {
        if (!state.sfxEnabled) return;
        try {
          this.init();
          if (!this.ctx) return;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          const baseFreq = 750 + Math.min(speedRatio * 500, 700);
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(baseFreq, this.ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(150, this.ctx.currentTime + 0.025);

          gain.gain.setValueAtTime(0.22, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.025);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start();
          osc.stop(this.ctx.currentTime + 0.026);
        } catch (e) {
          // Silent fallback
        }
      }

      playLatch() {
        if (!state.sfxEnabled) return;
        try {
          this.init();
          if (!this.ctx) return;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          osc.type = 'sine';
          osc.frequency.setValueAtTime(320, this.ctx.currentTime);
          osc.frequency.exponentialRampToValueAtTime(60, this.ctx.currentTime + 0.12);

          gain.gain.setValueAtTime(0.4, this.ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.12);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start();
          osc.stop(this.ctx.currentTime + 0.13);
        } catch (e) {}
      }

      playFanfare() {
        if (!state.sfxEnabled) return;
        try {
          this.init();
          if (!this.ctx) return;
          const notes = [
            { f: 523.25, t: 0.0, d: 0.15 }, // C5
            { f: 659.25, t: 0.12, d: 0.15 }, // E5
            { f: 783.99, t: 0.24, d: 0.18 }, // G5
            { f: 1046.50, t: 0.40, d: 0.55 }, // C6
            { f: 1318.51, t: 0.55, d: 0.8 }, // E6
          ];

          notes.forEach(n => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(n.f, this.ctx.currentTime + n.t);

            gain.gain.setValueAtTime(0.0, this.ctx.currentTime + n.t);
            gain.gain.linearRampToValueAtTime(0.28, this.ctx.currentTime + n.t + 0.03);
            gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + n.t + n.d);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(this.ctx.currentTime + n.t);
            osc.stop(this.ctx.currentTime + n.t + n.d);
          });
        } catch (e) {}
      }
    }

    const audio = new SoundEngine();

    /* =====================================================================
       CANVAS FIREWORKS & CONFETTI CELEBRATION ENGINE
       ===================================================================== */
    class CelebrationEngine {
      constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.confetti = [];
        this.animId = null;
        this.resize();
        window.addEventListener('resize', () => this.resize());
      }

      resize() {
        this.width = this.canvas.width = window.innerWidth;
        this.height = this.canvas.height = window.innerHeight;
      }

      burst(count = 120) {
        const colors = ['#ffd700', '#f59e0b', '#38bdf8', '#ec4899', '#10b981', '#f43f5e', '#ffffff'];
        
        // Fireworks bursts from multiple origins
        const origins = [
          { x: this.width * 0.25, y: this.height * 0.35 },
          { x: this.width * 0.5, y: this.height * 0.25 },
          { x: this.width * 0.75, y: this.height * 0.35 },
          { x: this.width * 0.65, y: this.height * 0.45 },
          { x: this.width * 0.35, y: this.height * 0.45 }
        ];

        origins.forEach((orig, idx) => {
          setTimeout(() => {
            for (let i = 0; i < 45; i++) {
              const angle = Math.random() * Math.PI * 2;
              const speed = 2 + Math.random() * 8;
              this.particles.push({
                x: orig.x,
                y: orig.y,
                vx: Math.cos(angle) * speed,
                vy: Math.sin(angle) * speed,
                color: colors[Math.floor(Math.random() * colors.length)],
                size: 2.5 + Math.random() * 3.5,
                alpha: 1,
                decay: 0.012 + Math.random() * 0.015,
                gravity: 0.12
              });
            }
          }, idx * 160);
        });

        // Confetti Cannons from bottom corners
        for (let i = 0; i < 140; i++) {
          // Left cannon
          this.confetti.push({
            x: 0,
            y: this.height,
            vx: 8 + Math.random() * 12,
            vy: -(12 + Math.random() * 14),
            w: 8 + Math.random() * 8,
            h: 12 + Math.random() * 10,
            color: colors[Math.floor(Math.random() * colors.length)],
            tilt: Math.random() * 10,
            tiltSpeed: 0.1 + Math.random() * 0.15,
            rotation: Math.random() * Math.PI * 2,
            rotSpeed: 0.05 + Math.random() * 0.1,
            gravity: 0.28,
            drag: 0.985
          });

          // Right cannon
          this.confetti.push({
            x: this.width,
            y: this.height,
            vx: -(8 + Math.random() * 12),
            vy: -(12 + Math.random() * 14),
            w: 8 + Math.random() * 8,
            h: 12 + Math.random() * 10,
            color: colors[Math.floor(Math.random() * colors.length)],
            tilt: Math.random() * 10,
            tiltSpeed: 0.1 + Math.random() * 0.15,
            rotation: Math.random() * Math.PI * 2,
            rotSpeed: 0.05 + Math.random() * 0.1,
            gravity: 0.28,
            drag: 0.985
          });
        }

        if (!this.animId) {
          this.loop();
        }
      }

      loop() {
        this.ctx.clearRect(0, 0, this.width, this.height);

        // Update & draw fireworks
        for (let i = this.particles.length - 1; i >= 0; i--) {
          const p = this.particles[i];
          p.x += p.vx;
          p.y += p.vy;
          p.vy += p.gravity;
          p.alpha -= p.decay;

          if (p.alpha <= 0) {
            this.particles.splice(i, 1);
            continue;
          }

          this.ctx.save();
          this.ctx.globalAlpha = p.alpha;
          this.ctx.fillStyle = p.color;
          this.ctx.beginPath();
          this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
          this.ctx.fill();
          this.ctx.restore();
        }

        // Update & draw confetti
        for (let i = this.confetti.length - 1; i >= 0; i--) {
          const c = this.confetti[i];
          c.x += c.vx;
          c.y += c.vy;
          c.vx *= c.drag;
          c.vy += c.gravity;
          c.tilt += c.tiltSpeed;
          c.rotation += c.rotSpeed;

          if (c.y > this.height + 40) {
            this.confetti.splice(i, 1);
            continue;
          }

          this.ctx.save();
          this.ctx.translate(c.x, c.y);
          this.ctx.rotate(c.rotation);
          this.ctx.fillStyle = c.color;
          this.ctx.fillRect(-c.w / 2, -c.h / 2, c.w * Math.cos(c.tilt), c.h);
          this.ctx.restore();
        }

        if (this.particles.length > 0 || this.confetti.length > 0) {
          this.animId = requestAnimationFrame(() => this.loop());
        } else {
          this.animId = null;
          this.ctx.clearRect(0, 0, this.width, this.height);
        }
      }
    }

    const celebration = new CelebrationEngine('celebrationCanvas');

    /* =====================================================================
       CUSTOM MODALS HELPER (NO NATIVE ALERT OR CONFIRM)
       ===================================================================== */
    const Modal = {
      confirm(title, message, onConfirm, onCancel = null) {
        const modal = document.getElementById('customModal');
        document.getElementById('customModalTitle').textContent = title;
        document.getElementById('customModalMessage').textContent = message;
        
        const actions = document.getElementById('customModalActions');
        actions.innerHTML = `
          <button class="btn-secondary" id="customCancel" style="flex:1;">Cancel</button>
          <button class="btn-primary" id="customOk" style="flex:1;">Confirm</button>
        `;

        const close = () => modal.classList.remove('open');

        document.getElementById('customCancel').onclick = () => {
          close();
          if (onCancel) onCancel();
        };
        document.getElementById('customOk').onclick = () => {
          close();
          if (onConfirm) onConfirm();
        };

        modal.classList.add('open');
      },

      alert(title, message, onOk = null) {
        const modal = document.getElementById('customModal');
        document.getElementById('customModalTitle').textContent = title;
        document.getElementById('customModalMessage').textContent = message;
        
        const actions = document.getElementById('customModalActions');
        actions.innerHTML = `<button class="btn-primary" id="customOk" style="width:160px;">OK</button>`;

        const close = () => modal.classList.remove('open');

        document.getElementById('customOk').onclick = () => {
          close();
          if (onOk) onOk();
        };

        modal.classList.add('open');
      }
    };

    function showToast(msg) {
      const container = document.getElementById('toastContainer');
      const toast = document.createElement('div');
      toast.className = 'toast-message';
      toast.textContent = msg;
      container.appendChild(toast);
      setTimeout(() => toast.remove(), 3200);
    }

    /* =====================================================================
       DATA PARSING & INITIALIZATION
       ===================================================================== */
    function formatDepartment(dept, division) {
      const d = (dept || '').trim();
      const div = (division || '').trim();
      if (d.toUpperCase() === 'HQ' && div) {
        return `HQ - ${div}`;
      }
      return d || 'General';
    }

    function parseCSV(text) {
      const rows = [];
      let currentRow = [];
      let currentVal = '';
      let insideQuotes = false;

      for (let i = 0; i < text.length; i++) {
        const char = text[i];
        const nextChar = text[i + 1];

        if (char === '"') {
          if (insideQuotes && nextChar === '"') {
            currentVal += '"';
            i++;
          } else {
            insideQuotes = !insideQuotes;
          }
        } else if (char === ',' && !insideQuotes) {
          currentRow.push(currentVal.trim());
          currentVal = '';
        } else if ((char === '\r' || char === '\n') && !insideQuotes) {
          if (char === '\r' && nextChar === '\n') i++;
          currentRow.push(currentVal.trim());
          currentVal = '';
          if (currentRow.some(c => c.length > 0)) {
            rows.push(currentRow);
          }
          currentRow = [];
        } else {
          currentVal += char;
        }
      }
      if (currentVal || currentRow.length > 0) {
        currentRow.push(currentVal.trim());
        if (currentRow.some(c => c.length > 0)) rows.push(currentRow);
      }
      return rows;
    }

    function initData() {
      // 1. Load Sheet URL
      document.getElementById('sheetUrlInput').value = state.sheetUrl;

      // 2. Load Prizes
      const savedPrizes = localStorage.getItem('dnd_prizes');
      if (savedPrizes) {
        try {
          state.prizes = JSON.parse(savedPrizes);
        } catch (e) {
          state.prizes = [...EMBEDDED_DEFAULT_PRIZES];
        }
      } else {
        state.prizes = [...EMBEDDED_DEFAULT_PRIZES];
      }

      // 3. Load Active Prize
      state.activePrizeId = localStorage.getItem('dnd_active_prize_id') || (state.prizes[0] ? state.prizes[0].id : null);

      // 4. Load Winners
      const savedWinners = localStorage.getItem('dnd_winners');
      if (savedWinners) {
        try {
          state.winners = JSON.parse(savedWinners);
        } catch (e) {
          state.winners = [];
        }
      } else {
        state.winners = [];
      }

      // 5. Load Participants (from localStorage or embedded fallback)
      const savedParticipants = localStorage.getItem('dnd_participants');
      if (savedParticipants) {
        try {
          state.participants = JSON.parse(savedParticipants);
        } catch (e) {
          state.participants = [...EMBEDDED_DEFAULT_PARTICIPANTS];
        }
      } else {
        state.participants = [...EMBEDDED_DEFAULT_PARTICIPANTS];
      }

      // 6. Recalculate remaining pool (filter out winners)
      updateRemainingPool();

      // 7. Update UI
      renderPrizesUI();
      renderWinnersUI();
      updateActivePrizeUI();
      updateStatsUI();
      setupInitialDrum();
    }

    function updateRemainingPool() {
      const winnerIds = new Set(state.winners.map(w => String(w.id)));
      state.remainingPool = state.participants.filter(p => !winnerIds.has(String(p.id)));
    }

    function updateStatsUI() {
      document.getElementById('statTotalParticipants').textContent = state.participants.length;
      document.getElementById('statRemainingPool').textContent = state.remainingPool.length;
      document.getElementById('statWinnersDrawn').textContent = state.winners.length;
      document.getElementById('poolStatusText').textContent = `${state.remainingPool.length} In Pool`;
      document.getElementById('dockWinnerCount').textContent = `Winners (${state.winners.length})`;
      document.getElementById('rightEdgeCount').textContent = `WINNERS (${state.winners.length})`;
      document.getElementById('historyHeaderCount').textContent = state.winners.length;
    }

    async function syncGoogleSheet(showToasts = true) {
      const url = document.getElementById('sheetUrlInput').value.trim();
      if (!url) {
        Modal.alert('Error', 'Please enter a valid Google Sheets published CSV URL.');
        return;
      }

      state.sheetUrl = url;
      localStorage.setItem('dnd_sheet_url', url);
      document.getElementById('statSyncStatus').textContent = 'Fetching Sheet...';

      try {
        const resp = await fetch(url);
        if (!resp.ok) throw new Error(`HTTP Error ${resp.status}`);
        const csvText = await resp.text();
        const rows = parseCSV(csvText);

        if (rows.length <= 1) {
          throw new Error('CSV is empty or missing data rows.');
        }

        const participants = [];
        // Skip header row
        for (let i = 1; i < rows.length; i++) {
          const row = rows[i];
          if (!row || row.length === 0) continue;
          const id = row[0] || '';
          const name = row[1] || '';
          const dept = row[2] || '';
          const division = row[3] || '';

          if (!name && !id) continue;

          participants.push({
            id: id,
            name: name,
            dept: dept,
            division: division,
            displayDept: formatDepartment(dept, division)
          });
        }

        if (participants.length === 0) {
          throw new Error('No valid participant records found in CSV.');
        }

        state.participants = participants;
        localStorage.setItem('dnd_participants', JSON.stringify(participants));
        updateRemainingPool();
        updateStatsUI();
        setupInitialDrum();

        document.getElementById('statSyncStatus').textContent = `Synced (${participants.length} loaded)`;
        if (showToasts) {
          showToast(`✓ Successfully synced ${participants.length} participants!`);
        }
      } catch (err) {
        console.warn('Sync failed, using offline cache:', err);
        document.getElementById('statSyncStatus').textContent = 'Offline (Using Cache)';
        if (showToasts) {
          Modal.alert('Sync Notice', `Could not fetch online Google Sheet (${err.message}). The app is running smoothly using offline cached participants.`);
        }
      }
    }

    /* =====================================================================
       PRIZE MANAGEMENT
       ===================================================================== */
    function getActivePrize() {
      return state.prizes.find(p => p.id === state.activePrizeId) || state.prizes[0] || null;
    }

    function updateActivePrizeUI() {
      const prize = getActivePrize();
      if (!prize) return;

      document.getElementById('activePrizeTier').textContent = prize.tier.toUpperCase();
      document.getElementById('activePrizeTitle').textContent = prize.name;
      document.getElementById('activePrizeRemaining').textContent = `${prize.remaining} of ${prize.quantity} remaining`;
      document.getElementById('activePrizeThumb').src = prize.image;

      document.getElementById('dockPrizeTier').textContent = prize.tier.toUpperCase();
      document.getElementById('dockPrizeName').textContent = prize.name;
    }

    function renderPrizesUI() {
      const container = document.getElementById('prizeListContainer');
      container.innerHTML = '';

      state.prizes.forEach((prize) => {
        const isActive = prize.id === state.activePrizeId;
        const row = document.createElement('div');
        row.className = `prize-item-row ${isActive ? 'is-active' : ''}`;
        row.innerHTML = `
          <img src="${prize.image}" alt="${prize.name}" class="prize-item-thumb">
          <div class="prize-item-info">
            <div class="prize-item-title">${prize.name}</div>
            <div class="prize-item-sub">
              <span style="color:var(--gold-primary);font-weight:700;">${prize.tier}</span> &bull; 
              <span>${prize.remaining}/${prize.quantity} left</span>
            </div>
          </div>
          <div class="prize-item-actions">
            <button class="btn-icon btn-select-prize" title="Select as Active" style="${isActive ? 'color:#ffd700;border-color:#ffd700;' : ''}">🎯</button>
            <button class="btn-icon btn-edit-prize" title="Edit">✏️</button>
            <button class="btn-icon btn-del-prize" title="Delete" style="color:#f87171;">🗑️</button>
          </div>
        `;

        row.querySelector('.btn-select-prize').onclick = () => {
          state.activePrizeId = prize.id;
          localStorage.setItem('dnd_active_prize_id', prize.id);
          renderPrizesUI();
          updateActivePrizeUI();
          showToast(`Active Prize: ${prize.name}`);
        };

        row.querySelector('.btn-edit-prize').onclick = () => openEditPrizeModal(prize);

        row.querySelector('.btn-del-prize').onclick = () => {
          if (state.prizes.length <= 1) {
            Modal.alert('Notice', 'You must have at least one prize configured.');
            return;
          }
          Modal.confirm('Delete Prize', `Are you sure you want to delete "${prize.name}"?`, () => {
            state.prizes = state.prizes.filter(p => p.id !== prize.id);
            if (state.activePrizeId === prize.id) {
              state.activePrizeId = state.prizes[0].id;
              localStorage.setItem('dnd_active_prize_id', state.activePrizeId);
            }
            localStorage.setItem('dnd_prizes', JSON.stringify(state.prizes));
            renderPrizesUI();
            updateActivePrizeUI();
            showToast('Prize removed.');
          });
        };

        container.appendChild(row);
      });
    }

    let editingPrizeId = null;
    let tempPrizeBase64 = null;

    function openEditPrizeModal(prize = null) {
      editingPrizeId = prize ? prize.id : null;
      document.getElementById('prizeEditModalTitle').textContent = prize ? 'Edit Prize' : 'Add New Prize';
      document.getElementById('editPrizeName').value = prize ? prize.name : '';
      document.getElementById('editPrizeTier').value = prize ? prize.tier : 'Special Prize';
      document.getElementById('editPrizeQty').value = prize ? prize.quantity : 1;
      document.getElementById('editPrizeNotes').value = prize ? (prize.notes || '') : '';
      
      const defaultImg = "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100' fill='%23ffd700'><polygon points='50,15 61,38 86,41 68,59 72,84 50,72 28,84 32,59 14,41 39,38'/></svg>";
      tempPrizeBase64 = prize ? prize.image : defaultImg;
      document.getElementById('editPrizeImgPreview').src = tempPrizeBase64;

      document.getElementById('prizeEditModal').classList.add('open');
    }

    document.getElementById('editPrizeFileInput').onchange = (e) => {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (event) => {
        tempPrizeBase64 = event.target.result;
        document.getElementById('editPrizeImgPreview').src = tempPrizeBase64;
      };
      reader.readAsDataURL(file);
    };

    document.getElementById('btnCancelPrizeEdit').onclick = () => {
      document.getElementById('prizeEditModal').classList.remove('open');
    };

    document.getElementById('btnSavePrize').onclick = () => {
      const name = document.getElementById('editPrizeName').value.trim();
      const tier = document.getElementById('editPrizeTier').value.trim() || 'Prize';
      const qty = parseInt(document.getElementById('editPrizeQty').value, 10) || 1;
      const notes = document.getElementById('editPrizeNotes').value.trim();

      if (!name) {
        Modal.alert('Error', 'Please enter a prize name.');
        return;
      }

      if (editingPrizeId) {
        const p = state.prizes.find(item => item.id === editingPrizeId);
        if (p) {
          p.name = name;
          p.tier = tier;
          p.quantity = qty;
          p.remaining = Math.min(p.remaining, qty);
          p.notes = notes;
          p.image = tempPrizeBase64;
        }
      } else {
        const newPrize = {
          id: 'prize_' + Date.now(),
          name: name,
          tier: tier,
          quantity: qty,
          remaining: qty,
          notes: notes,
          image: tempPrizeBase64
        };
        state.prizes.push(newPrize);
        state.activePrizeId = newPrize.id;
        localStorage.setItem('dnd_active_prize_id', newPrize.id);
      }

      localStorage.setItem('dnd_prizes', JSON.stringify(state.prizes));
      document.getElementById('prizeEditModal').classList.remove('open');
      renderPrizesUI();
      updateActivePrizeUI();
      showToast('Prize saved successfully!');
    };

    document.getElementById('btnAddPrize').onclick = () => openEditPrizeModal(null);

    /* =====================================================================
       PRE-SPIN REVEAL MODAL
       ===================================================================== */
    function showPrizeRevealModal() {
      const prize = getActivePrize();
      if (!prize) return;

      document.getElementById('modalRevealTier').textContent = `UP NEXT: ${prize.tier.toUpperCase()}`;
      document.getElementById('modalRevealImg').src = prize.image;
      document.getElementById('modalRevealTitle').textContent = prize.name;
      document.getElementById('modalRevealNotes').textContent = prize.notes || '';
      document.getElementById('modalRevealRemaining').textContent = `${prize.remaining} of ${prize.quantity} remaining in this draw`;

      const modal = document.getElementById('prizeRevealModal');
      modal.classList.add('open');

      audio.playLatch();
    }

    document.getElementById('btnRevealPrizeQuick').onclick = showPrizeRevealModal;
    document.getElementById('dockPrizePill').onclick = showPrizeRevealModal;
    document.getElementById('btnStartDrawFromReveal').onclick = () => {
      document.getElementById('prizeRevealModal').classList.remove('open');
    };
    document.getElementById('prizeRevealModal').onclick = (e) => {
      if (e.target.id === 'prizeRevealModal') {
        document.getElementById('prizeRevealModal').classList.remove('open');
      }
    };

    /* =====================================================================
       WINNER HISTORY & EXPORT
       ===================================================================== */
    function renderWinnersUI() {
      const container = document.getElementById('historyListContainer');
      const emptyState = document.getElementById('historyEmptyState');

      container.querySelectorAll('.winner-card').forEach(el => el.remove());

      if (state.winners.length === 0) {
        if (emptyState) emptyState.style.display = 'block';
        return;
      }

      if (emptyState) emptyState.style.display = 'none';

      state.winners.forEach((w, idx) => {
        const card = document.createElement('div');
        card.className = 'winner-card';
        card.innerHTML = `
          <div class="winner-card-top">
            <span class="winner-rank">#${state.winners.length - idx}</span>
            <span class="winner-time">${w.time || ''}</span>
          </div>
          <div class="winner-details">
            <div>
              <span class="winner-name-display">${w.name}</span>
              <span class="participant-dept-pill ${w.dept === 'HQ' ? 'hq' : ''}" style="margin-left:8px;">${w.displayDept}</span>
              <span class="participant-id" style="margin-left:4px;">#${w.id}</span>
            </div>
          </div>
          <div class="winner-prize-banner">
            🎁 <b>${w.prizeTier || 'Prize'}:</b> ${w.prizeName || ''}
          </div>
          <button class="btn-redraw-winner" title="Return participant back to the pool">
            ↩ Return to Pool
          </button>
        `;

        card.querySelector('.btn-redraw-winner').onclick = () => {
          Modal.confirm('Return to Pool', `Return ${w.name} to the eligible pool?`, () => {
            state.winners = state.winners.filter(item => item.id !== w.id);
            localStorage.setItem('dnd_winners', JSON.stringify(state.winners));
            
            // Restore prize count if available
            const prize = state.prizes.find(p => p.name === w.prizeName);
            if (prize && prize.remaining < prize.quantity) {
              prize.remaining++;
              localStorage.setItem('dnd_prizes', JSON.stringify(state.prizes));
            }

            updateRemainingPool();
            updateStatsUI();
            renderWinnersUI();
            updateActivePrizeUI();
            setupInitialDrum();
            showToast(`${w.name} returned to pool.`);
          });
        };

        container.appendChild(card);
      });
    }

    function exportWinnersCSV() {
      if (state.winners.length === 0) {
        Modal.alert('Notice', 'No winners recorded yet to export.');
        return;
      }

      const headers = ['Order', 'Employee ID', 'Name', 'Department', 'Division', 'Prize Won', 'Prize Tier', 'Timestamp'];
      const rows = state.winners.map((w, idx) => [
        idx + 1,
        `"${w.id}"`,
        `"${w.name}"`,
        `"${w.dept}"`,
        `"${w.division || ''}"`,
        `"${w.prizeName}"`,
        `"${w.prizeTier || ''}"`,
        `"${w.time}"`
      ]);

      const csvContent = '\uFEFF' + [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `D&D_Lucky_Draw_Winners_${new Date().toISOString().slice(0, 10)}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      showToast('CSV Exported!');
    }

    document.getElementById('btnExportCsv').onclick = exportWinnersCSV;
    document.getElementById('btnClearHistoryBtn').onclick = () => {
      if (state.winners.length === 0) return;
      Modal.confirm('Clear Winners', 'Clear the entire winners history and return everyone to the pool?', () => {
        state.winners = [];
        localStorage.removeItem('dnd_winners');
        
        // Restore prize quantities
        state.prizes.forEach(p => p.remaining = p.quantity);
        localStorage.setItem('dnd_prizes', JSON.stringify(state.prizes));

        updateRemainingPool();
        updateStatsUI();
        renderWinnersUI();
        updateActivePrizeUI();
        setupInitialDrum();
        showToast('Winners cleared, pool restored.');
      });
    };

    /* =====================================================================
       SPIN ENGINE & 3D SLOT ROULETTE MECHANICS
       ===================================================================== */
    const ITEM_HEIGHT = 96; // 96px per card
    let drumItems = [];
    let currentY = 0;
    let targetY = 0;
    let velocity = 0;
    let maxVelocity = 3200;
    let targetWinner = null;
    let spinStartTime = 0;
    let lastTickY = 0;
    let animFrame = null;

    function buildReelSequence(winner) {
      const pool = state.remainingPool.length > 0 ? state.remainingPool : state.participants;
      const sequence = [];
      
      // Shuffle pool for filler
      const shuffled = [...pool].sort(() => 0.5 - Math.random());
      
      // We want a sequence of ~70 items for smooth prolonged spin
      const count = 75;
      for (let i = 0; i < count - 1; i++) {
        sequence.push(shuffled[i % shuffled.length]);
      }
      
      // The target winner lands at the designated slot index (e.g. index 70)
      sequence.push(winner);

      // Add a couple trailing cards for natural scroll view
      sequence.push(shuffled[(count) % shuffled.length]);
      sequence.push(shuffled[(count + 1) % shuffled.length]);

      return sequence;
    }

    function createCardElement(participant) {
      const card = document.createElement('div');
      card.className = 'participant-card';
      const isHQ = (participant.dept || '').toUpperCase() === 'HQ';
      card.innerHTML = `
        <div class="card-content">
          <span class="participant-dept-pill ${isHQ ? 'hq' : ''}">${participant.displayDept}</span>
          <div class="participant-name">${participant.name}</div>
          <span class="participant-id">#${participant.id}</span>
        </div>
      `;
      return card;
    }

    function setupInitialDrum() {
      const track = document.getElementById('slotDrumTrack');
      track.innerHTML = '';
      currentY = 0;
      track.style.transform = `translateY(0px)`;

      const pool = state.remainingPool.length > 0 ? state.remainingPool : state.participants;
      if (pool.length === 0) {
        track.innerHTML = `<div class="participant-card"><div class="card-content"><div class="participant-name">All Drawn!</div></div></div>`;
        return;
      }

      // Initial 3 items
      for (let i = 0; i < 3; i++) {
        const p = pool[i % pool.length];
        track.appendChild(createCardElement(p));
      }
    }

    function startSpin() {
      if (state.isSpinning) return;

      if (state.remainingPool.length === 0) {
        Modal.alert('Pool Empty', 'All participants have already won! Go to Settings to reset the pool or add more names.');
        return;
      }

      const activePrize = getActivePrize();
      if (!activePrize || activePrize.remaining <= 0) {
        Modal.alert('Prize Depleted', 'The active prize has 0 remaining! Please choose or add another prize in Settings.');
        return;
      }

      audio.init();

      // Pick random winner from remaining pool
      const winnerIndex = Math.floor(Math.random() * state.remainingPool.length);
      targetWinner = state.remainingPool[winnerIndex];

      // Assemble track
      drumItems = buildReelSequence(targetWinner);
      const track = document.getElementById('slotDrumTrack');
      track.innerHTML = '';
      drumItems.forEach(item => track.appendChild(createCardElement(item)));

      // Target item index is count - 2 (since we added 2 trailing)
      const targetIndex = drumItems.length - 3;
      // Center frame is at 96px from top, so currentY = targetIndex * ITEM_HEIGHT
      targetY = targetIndex * ITEM_HEIGHT;

      state.isSpinning = true;
      state.spinPhase = 'ACCEL';
      currentY = 0;
      velocity = 0;
      spinStartTime = performance.now();
      lastTickY = 0;

      // Update UI button
      const spinBtn = document.getElementById('btnSpinMain');
      spinBtn.classList.add('is-spinning');
      document.getElementById('spinBtnText').textContent = 'STOP SPIN';
      document.getElementById('spinBtnIcon').textContent = '🛑';
      document.getElementById('spinTipText').textContent = 'Press SPACE to stop';
      document.getElementById('slotTargetFrame').classList.remove('winner-locked');

      // Start physics loop
      let lastTime = performance.now();

      function spinPhysics(now) {
        const dt = Math.min((now - lastTime) / 1000, 0.05);
        lastTime = now;

        const elapsed = (now - spinStartTime) / 1000;

        if (state.spinPhase === 'ACCEL') {
          velocity += 4000 * dt;
          if (velocity >= maxVelocity) {
            velocity = maxVelocity;
            state.spinPhase = 'FAST';
          }
          currentY += velocity * dt;
        } else if (state.spinPhase === 'FAST') {
          currentY += velocity * dt;
          // Auto-stop after 5.5 seconds if user hasn't pressed spacebar
          if (elapsed > 5.5) {
            forceStopSpin(false);
          }
        } else if (state.spinPhase === 'STOPPING') {
          // Decelerate towards targetY
          const distRemaining = targetY - currentY;
          if (distRemaining <= 0) {
            currentY = targetY;
            state.spinPhase = 'SETTLING';
            velocity = 0;
          } else {
            // Smooth ease out
            const stopSpeed = Math.max(distRemaining * 4.8, 140);
            velocity = Math.min(velocity, stopSpeed);
            currentY += velocity * dt;
            if (currentY >= targetY) {
              currentY = targetY;
              state.spinPhase = 'SETTLING';
            }
          }
        }

        // Mechanical tick sound as cards roll past
        if (currentY - lastTickY >= ITEM_HEIGHT) {
          const speedRatio = Math.min(velocity / maxVelocity, 1);
          audio.playTick(speedRatio);
          lastTickY = currentY;
        }

        track.style.transform = `translateY(-${currentY}px)`;

        if (state.spinPhase !== 'SETTLING') {
          animFrame = requestAnimationFrame(spinPhysics);
        } else {
          finishSpin(targetWinner);
        }
      }

      animFrame = requestAnimationFrame(spinPhysics);
    }

    function forceStopSpin(isDoubleTap = false) {
      if (!state.isSpinning || state.spinPhase === 'STOPPING' || state.spinPhase === 'SETTLING') return;

      state.spinPhase = 'STOPPING';
      
      // If user double tapped or pressed stop, ensure target is within reasonable distance
      const minDistance = isDoubleTap ? ITEM_HEIGHT * 6 : ITEM_HEIGHT * 14;
      if (targetY - currentY < minDistance) {
        // Already close
      } else {
        // Accelerate landing
      }
    }

    function finishSpin(winner) {
      state.isSpinning = false;
      state.spinPhase = 'IDLE';

      // Snap to exact target
      const track = document.getElementById('slotDrumTrack');
      track.style.transform = `translateY(-${targetY}px)`;

      // Tactile settle & clack sound
      audio.playLatch();
      document.getElementById('slotTargetFrame').classList.add('winner-locked');

      const spinBtn = document.getElementById('btnSpinMain');
      spinBtn.classList.remove('is-spinning');
      document.getElementById('spinBtnText').textContent = 'START SPIN';
      document.getElementById('spinBtnIcon').textContent = '🎰';
      document.getElementById('spinTipText').textContent = 'Press SPACE to spin';

      // Celebration fanfare & fireworks!
      setTimeout(() => {
        audio.playFanfare();
        celebration.burst();
        showWinnerSpotlight(winner);
      }, 250);
    }

    /* =====================================================================
       WINNER SPOTLIGHT & CLAIM FLOW
       ===================================================================== */
    function showWinnerSpotlight(winner) {
      state.winnerPending = winner;
      const prize = getActivePrize();

      document.getElementById('modalWinnerName').textContent = winner.name;
      document.getElementById('modalWinnerDept').innerHTML = `
        <span>${winner.displayDept}</span> &bull; <span>ID: ${winner.id}</span>
      `;

      document.getElementById('modalWinnerPrizeImg').src = prize.image;
      document.getElementById('modalWinnerPrizeTier').textContent = prize.tier.toUpperCase();
      document.getElementById('modalWinnerPrizeName').textContent = prize.name;
      document.getElementById('modalWinnerPrizeNotes').textContent = prize.notes || '';

      document.getElementById('winnerModal').classList.add('open');
    }

    function confirmWinnerRecord() {
      if (!state.winnerPending) return;
      const winner = state.winnerPending;
      const prize = getActivePrize();

      const record = {
        id: winner.id,
        name: winner.name,
        dept: winner.dept,
        division: winner.division,
        displayDept: winner.displayDept,
        prizeName: prize.name,
        prizeTier: prize.tier,
        time: new Date().toLocaleTimeString()
      };

      // Add to winners list
      state.winners.unshift(record);
      localStorage.setItem('dnd_winners', JSON.stringify(state.winners));

      // Decrement prize remaining
      if (prize.remaining > 0) {
        prize.remaining--;
        localStorage.setItem('dnd_prizes', JSON.stringify(state.prizes));
      }

      // Remove from pool
      updateRemainingPool();
      updateStatsUI();
      renderWinnersUI();
      updateActivePrizeUI();

      document.getElementById('winnerModal').classList.remove('open');
      state.winnerPending = null;
      showToast(`🏆 Winner recorded: ${winner.name}!`);

      // If active prize reached 0, auto advance to next available prize
      if (prize.remaining <= 0) {
        const nextPrize = state.prizes.find(p => p.remaining > 0);
        if (nextPrize) {
          state.activePrizeId = nextPrize.id;
          localStorage.setItem('dnd_active_prize_id', nextPrize.id);
          renderPrizesUI();
          updateActivePrizeUI();
          showToast(`Advanced to: ${nextPrize.name}`);
        }
      }
    }

    function redrawWinner() {
      document.getElementById('winnerModal').classList.remove('open');
      state.winnerPending = null;
      showToast('Redrawing...');
      setTimeout(() => startSpin(), 300);
    }

    document.getElementById('btnConfirmWinner').onclick = confirmWinnerRecord;
    document.getElementById('btnRedrawImmediate').onclick = redrawWinner;

    /* =====================================================================
       KEYBOARD CONTROLS (MACBOOK OPTIMIZED SPACEBAR)
       ===================================================================== */
    window.addEventListener('keydown', (e) => {
      // Ignore if user is typing in form inputs
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) {
        return;
      }

      // SPACEBAR CONTROL
      if (e.code === 'Space' || e.key === ' ') {
        e.preventDefault();
        const now = Date.now();
        const isDoubleTap = (now - state.lastSpacePress) < 360;
        state.lastSpacePress = now;

        if (!state.isSpinning) {
          // Close modals if open, then start
          if (document.getElementById('prizeRevealModal').classList.contains('open')) {
            document.getElementById('prizeRevealModal').classList.remove('open');
          }
          if (document.getElementById('winnerModal').classList.contains('open')) {
            confirmWinnerRecord();
            return;
          }
          startSpin();
        } else {
          // Force stop
          forceStopSpin(isDoubleTap);
        }
      }

      // HOTKEYS
      if (e.key === 'h' || e.key === 'H') {
        toggleStageMode();
      } else if (e.key === 's' || e.key === 'S') {
        toggleSettingsDrawer();
      } else if (e.key === 'w' || e.key === 'W') {
        toggleHistoryDrawer();
      } else if (e.key === 'p' || e.key === 'P') {
        showPrizeRevealModal();
      } else if (e.key === 'f' || e.key === 'F') {
        toggleFullscreen();
      } else if (e.key === 'm' || e.key === 'M') {
        toggleSfx();
      }
    });

    document.getElementById('btnSpinMain').onclick = () => {
      if (!state.isSpinning) {
        startSpin();
      } else {
        forceStopSpin(false);
      }
    };

    /* =====================================================================
       STAGE MODE & DRAWER TOGGLES
       ===================================================================== */
    function toggleSettingsDrawer(open = null) {
      const drawer = document.getElementById('settingsDrawer');
      const shouldOpen = open !== null ? open : !drawer.classList.contains('open');
      if (shouldOpen) {
        drawer.classList.add('open');
        document.getElementById('historyDrawer').classList.remove('open');
      } else {
        drawer.classList.remove('open');
      }
    }

    function toggleHistoryDrawer(open = null) {
      const drawer = document.getElementById('historyDrawer');
      const shouldOpen = open !== null ? open : !drawer.classList.contains('open');
      if (shouldOpen) {
        drawer.classList.add('open');
        document.getElementById('settingsDrawer').classList.remove('open');
      } else {
        drawer.classList.remove('open');
      }
    }

    function toggleStageMode() {
      state.stageMode = !state.stageMode;
      const dock = document.getElementById('stageDock');
      const leftDrawer = document.getElementById('settingsDrawer');
      const rightDrawer = document.getElementById('historyDrawer');
      const leftHandle = document.getElementById('leftEdgeHandle');
      const rightHandle = document.getElementById('rightEdgeHandle');

      if (state.stageMode) {
        dock.classList.add('hidden-stage');
        leftDrawer.classList.remove('open');
        rightDrawer.classList.remove('open');
        leftHandle.style.opacity = '0.2';
        rightHandle.style.opacity = '0.2';
        showToast('Stage Mode: ON (Press H to toggle)');
      } else {
        dock.classList.remove('hidden-stage');
        leftHandle.style.opacity = '1';
        rightHandle.style.opacity = '1';
        showToast('Stage Mode: OFF');
      }
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
      }
    }

    document.getElementById('btnToggleSettingsDock').onclick = () => toggleSettingsDrawer();
    document.getElementById('btnCloseSettings').onclick = () => toggleSettingsDrawer(false);
    document.getElementById('leftEdgeHandle').onclick = () => toggleSettingsDrawer();

    document.getElementById('btnToggleHistoryDock').onclick = () => toggleHistoryDrawer();
    document.getElementById('btnCloseHistory').onclick = () => toggleHistoryDrawer(false);
    document.getElementById('rightEdgeHandle').onclick = () => toggleHistoryDrawer();

    document.getElementById('btnToggleStageMode').onclick = toggleStageMode;
    document.getElementById('btnTriggerStageMode').onclick = toggleStageMode;
    document.getElementById('btnToggleFullscreen').onclick = toggleFullscreen;

    /* PANEL TABS SWITCHER */
    document.querySelectorAll('.panel-tab').forEach(tab => {
      tab.onclick = () => {
        document.querySelectorAll('.panel-tab').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const target = tab.dataset.tab;
        document.querySelectorAll('.tab-content').forEach(content => {
          content.style.display = content.id === target ? 'block' : 'none';
        });
      };
    });

    /* =====================================================================
       AUDIO & BACKGROUND MUSIC (BGM)
       ===================================================================== */
    const bgmAudio = document.getElementById('bgmAudio');
    let synthBgmTimer = null;

    function playSynthBgmLoop() {
      if (!state.bgmPlaying) return;
      audio.init();
      if (!audio.ctx) return;

      // Gentle celebratory ambient chord progression
      const chords = [
        [261.63, 329.63, 392.00], // C maj
        [220.00, 261.63, 329.63], // A min
        [174.61, 220.00, 261.63], // F maj
        [196.00, 246.94, 293.66], // G maj
      ];

      let chordIdx = 0;
      function nextChord() {
        if (!state.bgmPlaying) return;
        const currentChord = chords[chordIdx % chords.length];
        chordIdx++;

        currentChord.forEach(freq => {
          const osc = audio.ctx.createOscillator();
          const gain = audio.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, audio.ctx.currentTime);

          gain.gain.setValueAtTime(0.0, audio.ctx.currentTime);
          gain.gain.linearRampToValueAtTime(0.04, audio.ctx.currentTime + 0.5);
          gain.gain.exponentialRampToValueAtTime(0.001, audio.ctx.currentTime + 2.8);

          osc.connect(gain);
          gain.connect(audio.ctx.destination);
          osc.start();
          osc.stop(audio.ctx.currentTime + 3.0);
        });

        synthBgmTimer = setTimeout(nextChord, 2800);
      }

      nextChord();
    }

    function toggleBgm() {
      audio.init();
      state.bgmPlaying = !state.bgmPlaying;
      const label = document.getElementById('bgmLabel');
      const playBtn = document.getElementById('btnBgmPlayPause');

      if (state.bgmPlaying) {
        label.textContent = 'BGM: ON';
        playBtn.textContent = '⏸ Pause BGM';
        
        if (bgmAudio.src) {
          bgmAudio.play().catch(() => playSynthBgmLoop());
        } else {
          playSynthBgmLoop();
        }
        showToast('🎵 Background Music Playing');
      } else {
        label.textContent = 'BGM: OFF';
        playBtn.textContent = '▶ Play BGM';
        bgmAudio.pause();
        if (synthBgmTimer) clearTimeout(synthBgmTimer);
        showToast('BGM Paused');
      }
    }

    function toggleSfx() {
      state.sfxEnabled = !state.sfxEnabled;
      document.getElementById('sfxLabel').textContent = state.sfxEnabled ? 'SFX: ON' : 'SFX: OFF';
      document.getElementById('sfxStatusText').textContent = state.sfxEnabled ? 'ENABLED' : 'MUTED';
      document.getElementById('sfxStatusText').style.color = state.sfxEnabled ? '#10b981' : '#f87171';
      showToast(state.sfxEnabled ? '🔊 SFX Enabled' : '🔇 SFX Muted');
    }

    document.getElementById('btnToggleBgm').onclick = toggleBgm;
    document.getElementById('btnBgmPlayPause').onclick = toggleBgm;
    document.getElementById('btnToggleSfx').onclick = toggleSfx;

    document.getElementById('btnTestTick').onclick = () => audio.playTick(1);
    document.getElementById('btnTestFanfare').onclick = () => {
      audio.playFanfare();
      celebration.burst(80);
    };

    document.getElementById('bgmVolumeSlider').oninput = (e) => {
      bgmAudio.volume = parseFloat(e.target.value);
    };

    document.getElementById('bgmFileInput').onchange = (e) => {
      const file = e.target.files[0];
      if (!file) return;
      const url = URL.createObjectURL(file);
      bgmAudio.src = url;
      showToast(`Loaded audio: ${file.name}`);
      if (state.bgmPlaying) bgmAudio.play();
    };

    document.getElementById('bgmUrlInput').onchange = (e) => {
      const url = e.target.value.trim();
      if (url) {
        bgmAudio.src = url;
        showToast('Updated BGM URL');
        if (state.bgmPlaying) bgmAudio.play();
      }
    };

    /* OVERLAY DARKNESS SLIDER */
    document.getElementById('overlayDarknessSlider').oninput = (e) => {
      const val = e.target.value;
      document.getElementById('bgOverlay').style.background = `radial-gradient(circle at 75% 45%, rgba(6, 8, 15, ${val * 0.4}) 0%, rgba(6, 8, 15, ${val}) 100%)`;
    };

    /* SHEET BUTTONS */
    document.getElementById('btnSyncSheet').onclick = () => syncGoogleSheet(true);
    document.getElementById('btnResetDefaultSheet').onclick = () => {
      document.getElementById('sheetUrlInput').value = DEFAULT_SHEET_URL;
      syncGoogleSheet(true);
    };

    /* RESET BUTTONS */
    document.getElementById('btnResetPoolOnly').onclick = () => {
      Modal.confirm('Reset All Winners', 'Restore all 510 participants back into the pool for testing?', () => {
        state.winners = [];
        localStorage.removeItem('dnd_winners');
        state.prizes.forEach(p => p.remaining = p.quantity);
        localStorage.setItem('dnd_prizes', JSON.stringify(state.prizes));
        updateRemainingPool();
        updateStatsUI();
        renderWinnersUI();
        updateActivePrizeUI();
        setupInitialDrum();
        showToast('Pool fully restored!');
      });
    };

    document.getElementById('btnFactoryReset').onclick = () => {
      Modal.confirm('Factory Reset', 'Clear ALL custom prizes, winner history, and settings back to factory defaults?', () => {
        localStorage.clear();
        state.sheetUrl = DEFAULT_SHEET_URL;
        state.prizes = [...EMBEDDED_DEFAULT_PRIZES];
        state.activePrizeId = state.prizes[0].id;
        state.winners = [];
        state.participants = [...EMBEDDED_DEFAULT_PARTICIPANTS];
        updateRemainingPool();
        initData();
        showToast('Factory reset complete.');
      });
    };

    /* =====================================================================
       AUTO-PLAY VIDEO FALLBACK HANDLER
       ===================================================================== */
    const bgVideo = document.getElementById('bgVideo');
    bgVideo.play().catch(() => {
      console.log('Video autoplay prevented, clicking anywhere will trigger play');
      window.addEventListener('click', () => bgVideo.play(), { once: true });
    });

    /* =====================================================================
       BOOTSTRAP APPLICATION
       ===================================================================== */
    window.addEventListener('DOMContentLoaded', () => {
      initData();
      // Try background sync if online
      if (navigator.onLine) {
        syncGoogleSheet(false);
      }
    });
  </script>
</body>
</html>
'''

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

shutil.copy2('public/index.html', 'index.html')

print("Created public/index.html and index.html successfully!")
print("Size of public/index.html:", os.path.getsize('public/index.html'), "bytes")
