from mss import mss
import pygetwindow as gw

def get_game_region(title="Roblox", top_ratio=0.2, left_ratio=0.2,
                    width_ratio=0.6, height_ratio=0.65):
    windows = [w for w in gw.getWindowsWithTitle(title) if w.visible]
    if not windows:
        raise RuntimeError(f"{title} window not found")
    win = windows[0]
    
    window_box = {
        "top": win.top,
        "left": win.left,
        "width": win.width,
        "height": win.height
    }
    
    game_region = {
        "top": window_box["top"] + int(window_box["height"] * top_ratio),
        "left": window_box["left"] + int(window_box["width"] * left_ratio),
        "width": int(window_box["width"] * width_ratio),
        "height": int(window_box["height"] * height_ratio)
    }
    
    return game_region, mss()
