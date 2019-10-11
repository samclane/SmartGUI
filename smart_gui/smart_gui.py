import pyautogui
import cv2 as cv
import numpy as np
from typing import List

class WorkflowStep:
    def target(self):
        pass

    def select(self):
        pass

    def input(self):
        pass

    def commit(self):
        pass

    def deselect(self):
        pass

class Workflow(List[WorkflowStep]):
    pass


def fuzzy_find(im_path, show_im=False):
    dt = np.array(pyautogui.screenshot())
    target = cv.imread(im_path)
    res = cv.matchTemplate(dt, target, cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print("Extemes: ", min_val, max_val, min_loc, max_loc)
    if show_im:
        cv.imshow("", res)
        cv.waitKey(0)
    pyautogui.moveTo(*max_loc)
