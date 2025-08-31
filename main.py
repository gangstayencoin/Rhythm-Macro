import cv2
import numpy as np
import time
import os
from src import capture, detection, input

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TILE_PATH = os.path.join(BASE_DIR, "assets", "tile.png")

tile, tile_gray, (w, h) = detection.load_tile(TILE_PATH)

lane_keys = ['r', 't', 'y', 'u']
num_lanes = len(lane_keys)
active_hits = {key: False for key in lane_keys}

game_region, sct = capture.get_game_region()
lane_width = game_region["width"] / num_lanes
margin = w // 2
hit_line_y = int(game_region["height"] * 0.58) - 1
threshold = 0.9

cv2.namedWindow("Live Capture", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Capture", 400, 400)
cv2.moveWindow("Live Capture", -100, -100)

while True:
    frame = np.array(sct.grab(game_region))
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.line(frame, (0, hit_line_y), (game_region["width"], hit_line_y), (0,0,255), 2)

    keys_to_press = set()

    for lane_index, key in enumerate(lane_keys):
        lane_x_start = max(0, int(lane_index * lane_width) - margin)
        lane_x_end = min(game_region["width"], int((lane_index + 1) * lane_width) + margin)
        lane_img = gray_frame[:, lane_x_start:lane_x_end]

        locs = detection.detect_tiles(lane_img, tile_gray, threshold)
        tile_over_line = False
        for pt in locs:
            x, y = pt
            tile_bottom = y + h
            tile_center_x = x + w // 2 + lane_x_start

            cv2.rectangle(frame, (tile_center_x - w//2, y),
                          (tile_center_x - w//2 + w, y + h), (0,255,0), 2)

            if y <= hit_line_y <= tile_bottom:
                tile_over_line = True
                break

        if tile_over_line and not active_hits[key]:
            keys_to_press.add(key)
            active_hits[key] = True
        elif not tile_over_line:
            active_hits[key] = False

    if keys_to_press:
        input.press_keys(keys_to_press)

    cv2.imshow("Live Capture", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    time.sleep(0.001)

cv2.destroyAllWindows()
