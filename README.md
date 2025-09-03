# Rhythm Macro v1.0 🎵

![Python Version](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
[![Discord](https://img.shields.io/badge/Discord-Contact%20Me-7289DA?logo=discord&logoColor=white)](https://discordapp.com/users/1154909932659945585)

**Rhythm Macro** is a high-performance macro for rhythm games (like Roblox music/tile games). It uses real-time screen capture and template matching to detect tiles and press keys with precise timing—including simultaneous multi-key presses.

## Features

- Real-time tile detection using OpenCV and MSS  
- Simultaneous multi-key presses with `pynput`  
- Modular design: `capture`, `detection`, `input`  
- High FPS live capture for responsive gameplay  
- Configurable hit line and lane keys  
- Off-screen live capture window for debugging  

## Install Tutorial:

[![Watch the video](https://img.youtube.com/vi/uD8jP-14Rl4/maxresdefault.jpg)](https://www.youtube.com/watch?v=uD8jP-14Rl4)

## Installation

### Easy method (recommended)
1. [Download ZIP](https://github.com/gangstayencoin/Rhythm-Macro/archive/refs/heads/main.zip)  
2. Extract it anywhere on your computer.  
3. Open a terminal in the extracted folder.  
4. Install dependencies:
  
   ```bash
   pip install -r requirements.txt

### Git Method (Requires Git to be installed on your system.)

```bash
git clone https://github.com/yourusername/rhythm-macro.git

cd rhythm-macro

pip install -r requirements.txt
```

## Usage

1. Make sure Roblox is running and visible.
2. Place your tile template in `assets/tile.png`. (One should already be there.)
3. Run the macro:

   ```bash
   python main.py
   ```
4. Press `Q` in the live capture window to quit the macro.

## Notes:

- The macro will detect tiles and press keys `R`, `T`, `Y`, `U` automatically.
- The green rectangle in the live capture window shows detected tiles for debugging and ETC.
- Ensure the live capture window is **off-screen** to prevent interference with Roblox.

## Configuration

Currently, key parameters are in `main.py`:

```python
lane_keys = ['r', 't', 'y', 'u']
hit_line_y = int(game_region["height"] * 0.58) - 1
threshold = 0.9
```

You can adjust:

- `lane_keys` → keys corresponding to each lane.
- `hit_line_y` → vertical position of the hit line.
- `threshold` → template matching sensitivity.
