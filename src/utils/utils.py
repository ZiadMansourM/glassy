import datetime
import os
from pathlib import Path
from typing import Final, Optional
import cv2
import numpy as np


BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent
DATA_DIR: Final[Path] = os.path.join(BASE_DIR, "data")
LOGGING_DIR: Final[Path] = os.path.join(BASE_DIR, "logs")
TEST_DIR: Final[Path] = os.path.join(DATA_DIR, "test")


def show_image(image: np.ndarray, title: str) -> None:
    cv2.startWindowThread()
    cv2.imshow(title, image)
    while cv2.waitKey(1) & 0xFF != ord("q"):
        pass
    cv2.destroyWindow(title)
    for _ in range(5):
        cv2.waitKey(1)


def log_to_file(message: str, custom_file: str="tune.log"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}"
    logs_file_path: Path = os.path.join(LOGGING_DIR, custom_file)
    with open(logs_file_path, "a") as f:
        f.write(f"{log_message}\n")
