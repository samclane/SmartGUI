from imutils import paths

IMAGE_PATHS = paths.list_images("./images")
EAST_PATH = "./smart_gui/frozen_east_text_detection.pb"

min_confidence = 0.5
width = 32
height = 32
padding = 0.05