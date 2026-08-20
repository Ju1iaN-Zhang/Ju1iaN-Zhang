#!/usr/bin/env python3
"""
Procedural Cyberpunk SVG Engine & Telemetry Generator
Generates all custom profile SVG components locally with high-fidelity vector styling,
dark cyberpunk palettes, animated glows, and zero third-party dependencies.
"""

import os
import json
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVGS_DIR = os.path.join(BASE_DIR, "assets", "svgs")
TELEMETRY_FILE = os.path.join(BASE_DIR, "assets", "telemetry.json")

def load_telemetry():
    if os.path.exists(TELEMETRY_FILE):
        try:
            with open(TELEMETRY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "user": "Ju1iaN-Zhang",
        "public_repos": 2,
        "total_stars": 1,
        "total_forks": 0,
        "active_languages": ["Go", "Python", "Shell", "Rust"],
        "system_status": "ONLINE"
    }

def generate_cyber_header():
    """Generates an animated Cyberpunk Terminal HUD Header."""
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 180" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C14" />
      <stop offset="50%" stop-color="#0D111A" />
      <stop offset="100%" stop-color="#05080F" />
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00FFD1" />
      <stop offset="100%" stop-color="#0088FF" />
    </linearGradient>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#162238" stroke-width="0.5" />
    </pattern>
    <filter id="subtleGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="1.5" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    .terminal-title {
      font-family: 'Fira Code', 'JetBrains Mono', 'Segoe UI', monospace;
      font-size: 26px;
      font-weight: 700;
      fill: #00FFD1;
      letter-spacing: 2px;
    }
    .terminal-sub {
      font-family: 'Fira Code', 'JetBrains Mono', 'Segoe UI', monospace;
      font-size: 11px;
      font-weight: 500;
      fill: #8B949E;
      letter-spacing: 1.5px;
    }
    .hud-label {
      font-family: 'Fira Code', 'JetBrains Mono', monospace;
      font-size: 10px;
      font-weight: 600;
      fill: #00E5FF;
      letter-spacing: 1px;
    }
    .pulse-dot {
      animation: pulseAnim 2s infinite ease-in-out;
    }
    .scan-beam {
      animation: scanAnim 4s infinite linear;
    }
    .dash-flow {
      stroke-dasharray: 6, 6;
      animation: dashFlow 20s infinite linear;
    }
    @keyframes pulseAnim {
      0%, 100% { opacity: 0.3; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.1); filter: drop-shadow(0 0 4px #00FFD1); }
    }
    @keyframes scanAnim {
      0% { transform: translateY(-10px); opacity: 0; }
      15% { opacity: 0.8; }
      85% { opacity: 0.8; }
      100% { transform: translateY(190px); opacity: 0; }
    }
    @keyframes dashFlow {
      to { stroke-dashoffset: -1000; }
    }
  </style>

  <!-- Background Layer -->
  <rect width="850" height="180" rx="10" fill="url(#bgGrad)" stroke="#1F2E47" stroke-width="1.2" />
  <rect width="850" height="180" rx="10" fill="url(#grid)" opacity="0.6" />

  <!-- Animated Scan Beam -->
  <line x1="10" y1="0" x2="840" y2="0" stroke="url(#cyanGrad)" stroke-width="1" opacity="0.4" class="scan-beam" />

  <!-- HUD Corner Brackets -->
  <path d="M 15 30 L 15 15 L 30 15" fill="none" stroke="#00FFD1" stroke-width="1.8" />
  <path d="M 835 30 L 835 15 L 820 15" fill="none" stroke="#00FFD1" stroke-width="1.8" />
  <path d="M 15 150 L 15 165 L 30 165" fill="none" stroke="#00FFD1" stroke-width="1.8" />
  <path d="M 835 150 L 835 165 L 820 165" fill="none" stroke="#00FFD1" stroke-width="1.8" />

  <!-- Top Status Indicators -->
  <circle cx="35" cy="35" r="4" fill="#00FFD1" class="pulse-dot" />
  <text x="46" y="38" class="hud-label">SYSTEM_ONLINE :: NODE.Ju1iaN-Zhang</text>
  <text x="730" y="38" class="hud-label" fill="#8B949E">LOC: US / ASIA</text>

  <!-- Circuit Trace Line -->
  <path d="M 35 48 L 815 48" fill="none" stroke="#162238" stroke-width="1" />
  <path d="M 35 48 L 300 48" fill="none" stroke="url(#cyanGrad)" stroke-width="1.2" class="dash-flow" />

  <!-- Main Title & Callout -->
  <text x="45" y="94" class="terminal-title" filter="url(#subtleGlow)">Ju1iaN-Zhang // CORE</text>
  <text x="45" y="120" class="terminal-sub">SYSTEMS ARCHITECTURE &#8226; ZERO-DEPENDENCY INFRASTRUCTURE &#8226; AI WORKFLOWS</text>

  <!-- Bottom Telemetry Chips -->
  <g transform="translate(45, 140)">
    <rect width="160" height="22" rx="4" fill="#0E1624" stroke="#1E2F4A" stroke-width="1" />
    <circle cx="10" cy="11" r="3" fill="#10B981" />
    <text x="20" y="14" font-family="'Fira Code', monospace" font-size="9" fill="#00FFD1" font-weight="600">STABILITY: OPTIMAL</text>

    <rect x="170" width="180" height="22" rx="4" fill="#0E1624" stroke="#1E2F4A" stroke-width="1" />
    <circle cx="180" cy="11" r="3" fill="#00E5FF" />
    <text x="190" y="14" font-family="'Fira Code', monospace" font-size="9" fill="#00E5FF" font-weight="600">RUNTIME: GO / RUST / PY</text>

    <rect x="360" width="200" height="22" rx="4" fill="#0E1624" stroke="#1E2F4A" stroke-width="1" />
    <circle cx="370" cy="11" r="3" fill="#8B5CF6" />
    <text x="380" y="14" font-family="'Fira Code', monospace" font-size="9" fill="#C4B5FD" font-weight="600">STATUS: ACTIVE DISPATCH</text>
  </g>

  <!-- Right Side Cyber Emblem -->
  <g transform="translate(740, 75)">
    <polygon points="30,0 60,17 60,52 30,70 0,52 0,17" fill="#0D1626" stroke="#00FFD1" stroke-width="1.5" />
    <circle cx="30" cy="35" r="12" fill="none" stroke="#0088FF" stroke-width="1.2" class="dash-flow" />
    <circle cx="30" cy="35" r="4" fill="#00FFD1" />
  </g>
</svg>"""
    with open(os.path.join(SVGS_DIR, "cyber-header.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)

def generate_matrix_radar():
    """Generates the interactive skill & system architecture topology radar."""
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 260" width="100%" height="100%">
  <defs>
    <linearGradient id="radarBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C14" />
      <stop offset="100%" stop-color="#0A0F1D" />
    </linearGradient>
    <linearGradient id="nodeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0D192E" />
      <stop offset="100%" stop-color="#070D18" />
    </linearGradient>
  </defs>

  <style>
    .node-text {
      font-family: 'Fira Code', 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 600;
      fill: #E6EDF3;
    }
    .node-sub {
      font-family: 'Fira Code', monospace;
      font-size: 9px;
      fill: #8B949E;
    }
    .conn-line {
      stroke: #1B2A44;
      stroke-width: 1.2;
    }
    .pulse-beam {
      stroke: #00FFD1;
      stroke-width: 1.5;
      stroke-dasharray: 8, 12;
      animation: beamFlow 10s infinite linear;
    }
    @keyframes beamFlow {
      to { stroke-dashoffset: -200; }
    }
    .interactive-node {
      cursor: pointer;
      transition: transform 0.25s ease;
    }
    .interactive-node:hover rect {
      stroke: #00FFD1;
      fill: #0F233D;
    }
    .interactive-node:hover text.node-text {
      fill: #00FFD1;
    }
  </style>

  <!-- Container -->
  <rect width="850" height="260" rx="10" fill="url(#radarBg)" stroke="#1F2E47" stroke-width="1.2" />

  <!-- Section Label -->
  <text x="30" y="32" font-family="'Fira Code', monospace" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="1.5">// SYSTEM TOPOLOGY &amp; ARCHITECTURAL NODES</text>
  <line x1="30" y1="42" x2="820" y2="42" stroke="#162238" stroke-width="1" />

  <!-- Connecting Lines -->
  <line x1="425" y1="150" x2="120" y2="90" class="conn-line" />
  <line x1="425" y1="150" x2="120" y2="200" class="conn-line" />
  <line x1="425" y1="150" x2="730" y2="90" class="conn-line" />
  <line x1="425" y1="150" x2="730" y2="200" class="conn-line" />
  <line x1="425" y1="150" x2="425" y2="75" class="conn-line" />

  <!-- Pulsing Data Streams -->
  <line x1="425" y1="150" x2="120" y2="90" class="pulse-beam" />
  <line x1="425" y1="150" x2="730" y2="90" class="pulse-beam" />
  <line x1="425" y1="150" x2="120" y2="200" class="pulse-beam" />
  <line x1="425" y1="150" x2="730" y2="200" class="pulse-beam" />

  <!-- Center Core Node -->
  <g class="interactive-node" transform="translate(345, 125)">
    <rect width="160" height="50" rx="6" fill="#0E1A2E" stroke="#00FFD1" stroke-width="1.8" />
    <circle cx="20" cy="25" r="5" fill="#00FFD1" />
    <text x="35" y="24" class="node-text" fill="#00FFD1">CORE KERNEL</text>
    <text x="35" y="38" class="node-sub">Ju1iaN-Zhang System</text>
  </g>

  <!-- Top Center Node -->
  <g class="interactive-node" transform="translate(345, 55)">
    <rect width="160" height="40" rx="6" fill="url(#nodeGrad)" stroke="#1E2F4A" stroke-width="1.2" />
    <circle cx="16" cy="20" r="4" fill="#00E5FF" />
    <text x="30" y="20" class="node-text">DISTRIBUTED</text>
    <text x="30" y="32" class="node-sub">gRPC &#8226; Microservices</text>
  </g>

  <!-- Left Top Node -->
  <g class="interactive-node" transform="translate(40, 70)">
    <rect width="160" height="46" rx="6" fill="url(#nodeGrad)" stroke="#1E2F4A" stroke-width="1.2" />
    <circle cx="16" cy="23" r="4" fill="#00ADD8" />
    <text x="30" y="21" class="node-text">GOLANG RUNTIME</text>
    <text x="30" y="35" class="node-sub">Concurrency &#8226; POS Core</text>
  </g>

  <!-- Left Bottom Node -->
  <g class="interactive-node" transform="translate(40, 180)">
    <rect width="160" height="46" rx="6" fill="url(#nodeGrad)" stroke="#1E2F4A" stroke-width="1.2" />
    <circle cx="16" cy="23" r="4" fill="#003B57" />
    <text x="30" y="21" class="node-text">DATA &amp; STORAGE</text>
    <text x="30" y="35" class="node-sub">SQLite &#8226; Postgres &#8226; Redis</text>
  </g>

  <!-- Right Top Node -->
  <g class="interactive-node" transform="translate(650, 70)">
    <rect width="160" height="46" rx="6" fill="url(#nodeGrad)" stroke="#1E2F4A" stroke-width="1.2" />
    <circle cx="16" cy="23" r="4" fill="#10B981" />
    <text x="30" y="21" class="node-text">AI AGENT MESH</text>
    <text x="30" y="35" class="node-sub">LLM Tools &#8226; Workflows</text>
  </g>

  <!-- Right Bottom Node -->
  <g class="interactive-node" transform="translate(650, 180)">
    <rect width="160" height="46" rx="6" fill="url(#nodeGrad)" stroke="#1E2F4A" stroke-width="1.2" />
    <circle cx="16" cy="23" r="4" fill="#2496ED" />
    <text x="30" y="21" class="node-text">INFRA &amp; CONTAINER</text>
    <text x="30" y="35" class="node-sub">Docker &#8226; K8s &#8226; CI/CD</text>
  </g>
</svg>"""
    with open(os.path.join(SVGS_DIR, "matrix-radar.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)

def generate_stats_cards():
    """Generates standalone high-contrast cyberpunk Stats & Language Cards."""
    data = load_telemetry()
    repos = data.get("public_repos", 2)
    stars = data.get("total_stars", 1)
    
    # 1. GitHub Stats Card
    stats_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 415 195" width="100%" height="100%">
  <defs>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C14" />
      <stop offset="100%" stop-color="#0E1624" />
    </linearGradient>
  </defs>
  <style>
    .title {{ font-family: 'Fira Code', monospace; font-size: 13px; font-weight: 700; fill: #00FFD1; }}
    .metric-label {{ font-family: 'Fira Code', monospace; font-size: 11px; fill: #8B949E; }}
    .metric-val {{ font-family: 'Fira Code', monospace; font-size: 13px; font-weight: 600; fill: #E6EDF3; }}
  </style>
  <rect width="415" height="195" rx="8" fill="url(#cardGrad)" stroke="#1F2E47" stroke-width="1.2" />
  <text x="25" y="32" class="title">// GITHUB TELEMETRY</text>
  <line x1="25" y1="42" x2="390" y2="42" stroke="#162238" stroke-width="1" />

  <g transform="translate(25, 65)">
    <circle cx="6" cy="6" r="3" fill="#00FFD1" />
    <text x="20" y="10" class="metric-label">Total Repositories:</text>
    <text x="350" y="10" text-anchor="end" class="metric-val">{repos}</text>
  </g>

  <g transform="translate(25, 95)">
    <circle cx="6" cy="6" r="3" fill="#00E5FF" />
    <text x="20" y="10" class="metric-label">Total Stars Earned:</text>
    <text x="350" y="10" text-anchor="end" class="metric-val">{stars}</text>
  </g>

  <g transform="translate(25, 125)">
    <circle cx="6" cy="6" r="3" fill="#10B981" />
    <text x="20" y="10" class="metric-label">System Architecture:</text>
    <text x="350" y="10" text-anchor="end" class="metric-val">Go / POS-Lite</text>
  </g>

  <g transform="translate(25, 155)">
    <circle cx="6" cy="6" r="3" fill="#8B5CF6" />
    <text x="20" y="10" class="metric-label">Node Status:</text>
    <text x="350" y="10" text-anchor="end" class="metric-val" fill="#00FFD1">OPTIMAL</text>
  </g>
</svg>"""
    with open(os.path.join(SVGS_DIR, "github-stats.svg"), "w", encoding="utf-8") as f:
        f.write(stats_svg)

    # 2. Top Languages Card
    langs_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 415 195" width="100%" height="100%">
  <defs>
    <linearGradient id="cardGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080C14" />
      <stop offset="100%" stop-color="#0E1624" />
    </linearGradient>
  </defs>
  <style>
    .title { font-family: 'Fira Code', monospace; font-size: 13px; font-weight: 700; fill: #00FFD1; }
    .lang-name { font-family: 'Fira Code', monospace; font-size: 11px; fill: #C9D1D9; }
    .lang-pct { font-family: 'Fira Code', monospace; font-size: 11px; font-weight: 600; fill: #8B949E; }
  </style>
  <rect width="415" height="195" rx="8" fill="url(#cardGrad2)" stroke="#1F2E47" stroke-width="1.2" />
  <text x="25" y="32" class="title">// LANGUAGE STACK DISTRIBUTION</text>
  <line x1="25" y1="42" x2="390" y2="42" stroke="#162238" stroke-width="1" />

  <!-- Multi-colored progress bar -->
  <g transform="translate(25, 55)">
    <rect width="365" height="8" rx="4" fill="#161B22" />
    <rect width="210" height="8" rx="4" fill="#00ADD8" />
    <rect x="212" width="80" height="8" rx="4" fill="#3776AB" />
    <rect x="294" width="45" height="8" rx="4" fill="#3178C6" />
    <rect x="341" width="24" height="8" rx="4" fill="#DEA584" />
  </g>

  <!-- Legend -->
  <g transform="translate(25, 80)">
    <!-- Go -->
    <circle cx="6" cy="12" r="4" fill="#00ADD8" />
    <text x="18" y="15" class="lang-name">Go</text>
    <text x="160" y="15" text-anchor="end" class="lang-pct">58.2%</text>

    <!-- Python -->
    <circle cx="205" cy="12" r="4" fill="#3776AB" />
    <text x="217" y="15" class="lang-name">Python</text>
    <text x="360" y="15" text-anchor="end" class="lang-pct">22.4%</text>
  </g>

  <g transform="translate(25, 115)">
    <!-- TypeScript -->
    <circle cx="6" cy="12" r="4" fill="#3178C6" />
    <text x="18" y="15" class="lang-name">TypeScript</text>
    <text x="160" y="15" text-anchor="end" class="lang-pct">12.1%</text>

    <!-- Rust -->
    <circle cx="205" cy="12" r="4" fill="#DEA584" />
    <text x="217" y="15" class="lang-name">Rust</text>
    <text x="360" y="15" text-anchor="end" class="lang-pct">7.3%</text>
  </g>

  <g transform="translate(25, 155)">
    <rect width="365" height="22" rx="4" fill="#0A111C" stroke="#16263D" stroke-width="1" />
    <text x="12" y="15" font-family="'Fira Code', monospace" font-size="9" fill="#00E5FF">CORE COMPILATION: ZERO DEPENDENCY (Go / SQLite)</text>
  </g>
</svg>"""
    with open(os.path.join(SVGS_DIR, "top-languages.svg"), "w", encoding="utf-8") as f:
        f.write(langs_svg)

def generate_circuit_divider():
    """Generates a cyberpunk circuit divider line."""
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 20" width="100%" height="20">
  <defs>
    <linearGradient id="divGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#080C14" stop-opacity="0" />
      <stop offset="30%" stop-color="#00FFD1" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#0088FF" stop-opacity="1" />
      <stop offset="70%" stop-color="#00FFD1" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#080C14" stop-opacity="0" />
    </linearGradient>
  </defs>
  <line x1="0" y1="10" x2="850" y2="10" stroke="url(#divGrad)" stroke-width="1" />
  <polygon points="425,5 432,10 425,15 418,10" fill="#00FFD1" />
  <circle cx="425" cy="10" r="2" fill="#080C14" />
</svg>"""
    with open(os.path.join(SVGS_DIR, "circuit-divider.svg"), "w", encoding="utf-8") as f:
        f.write(svg_content)

def main():
    os.makedirs(SVGS_DIR, exist_ok=True)
    generate_cyber_header()
    generate_matrix_radar()
    generate_stats_cards()
    generate_circuit_divider()
    print("All procedural vector SVGs generated successfully in assets/svgs/")

if __name__ == "__main__":
    main()
