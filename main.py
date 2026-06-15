import os
import sys
from pyautogui import locateOnScreen, center, click
from time import sleep
from configparser import ConfigParser

# Default values
delay_between_tries = 0.2
delay_after_succeding = 1
reference_images = ["reference1.png", "reference2.png", "reference3.png"]

# If the config has values, use those instead
config = ConfigParser()
config.read('settings.ini')

if config.has_option("SETTINGS", "delay_between_tries"):
    delay_between_tries = float(config["SETTINGS"]["delay_between_tries"])
if config.has_option("SETTINGS", "delay_after_succeding"):
    delay_after_succeding = float(config["SETTINGS"]["delay_after_succeding"])
if config.has_option("SETTINGS", "reference_images"):
    reference_images = [img.strip() for img in config["SETTINGS"]["reference_images"].split(",")]

# --- STARTUP VALIDATION ---
valid_images = []
print("Checking reference images...")
for img in reference_images:
    if os.path.exists(img):
        valid_images.append(img)
        print(f"  [OK] Found: {img}")
    else:
        print(f"  [WARNING] Missing: {img} (Will be skipped)")

# If no valid images are left, exit gracefully instead of crashing or looping uselessly
if not valid_images:
    print("\nError: No valid reference images found. Please check your files or settings.ini")
    sys.exit(1)

print(f"Starting loop with {len(valid_images)} valid image(s)...\n")
# --------------------------

# Main loop
while True:
    sleep(delay_between_tries)
    
    clicked = False
    for img in valid_images:
        try:
            download_location = locateOnScreen(img)
        except Exception:
            # Failsafe: if pyautogui throws an error for a specific image, skip it
            continue
            
        if download_location is not None:
            download_point_location = center(download_location)
            click(download_point_location.x, download_point_location.y)
            clicked = True
            break  # Stop checking other images once the first match is found and clicked
    
    if clicked:
        sleep(delay_after_succeding)