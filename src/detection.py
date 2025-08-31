import cv2
import numpy as np
import os

def load_tile(path):
    tile = cv2.imread(path)
    tile_gray = cv2.cvtColor(tile, cv2.COLOR_BGR2GRAY)
    return tile, tile_gray, tile_gray.shape[::-1]

def detect_tiles(frame_gray, tile_gray, threshold=0.9):
    result = cv2.matchTemplate(frame_gray, tile_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= threshold)
    return list(zip(*loc[::-1]))
