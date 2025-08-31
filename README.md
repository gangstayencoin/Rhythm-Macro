# Rhythm Macro v1.0 🎵

![Python Version](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

**Rhythm Macro** is a high-performance macro for rhythm games (like Roblox music/tile games). It uses real-time screen capture and template matching to detect tiles and press keys with precise timing—including simultaneous multi-key presses.



## Features

- Real-time tile detection using OpenCV and MSS
- Simultaneous multi-key presses with `pynput`
- Modular design: `capture`, `detection`, `input`
- High FPS live capture for responsive gameplay
- Configurable hit line and lane keys
- Off-screen live capture window for debugging


 
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/rhythm-macro.git

    cd rhythm-macro
    ```

2. Install dependencies: 

    ```bash
    pip install -r requirements.txt
    ```

## Usage 

1. Make sure Roblox (or your rhythm game) is running and visible.
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
