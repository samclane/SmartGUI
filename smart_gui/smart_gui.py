import pyautogui
import cv2 as cv
import numpy as np
from typing import List
from abc import ABC, abstractmethod


class WorkflowStep(ABC):
    def __init__(self):
        self._failed = False
        self.run_order = [
            self.target,
            self.select,
            self.input,
            self.commit,
            self.deselect
        ]

    @property
    def running(self):
        return not self._failed

    @property
    def failed(self):
        return self._failed

    @failed.setter
    def failed(self, value):
        if value == True:
            self.failover()
        self._failed = value

    @abstractmethod
    def failover(self):
        raise NotImplementedError
    
    @abstractmethod
    def target(self):
        raise NotImplementedError
    
    def select(self):
        pass

    def input(self):
        pass

    def commit(self):
        pass

    def deselect(self):
        pass


class Workflow(List[WorkflowStep]):
    def run_flow(self):
        for step in self:
            for func in step.run_order:
                if step.running:
                    func()

def basic_find(im_path, show_im=False):
    target = cv.imread(im_path)
    center = pyautogui.locateCenterOnScreen(target)
    print("Center:", *center)
    pyautogui.moveTo(*center)


def fuzzy_find(im_path, show_im=False):
    dt = np.array(pyautogui.screenshot())
    target = cv.imread(im_path)
    res = cv.matchTemplate(dt, target, cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    print("Extemes:", min_val, max_val, min_loc, max_loc)
    if show_im:
        cv.imshow("Screenshot", dt)
        cv.waitKey(0)
        cv.imshow("Target", target)
        cv.waitKey(0)
        cv.imshow("Search", res)
        cv.waitKey(0)
    pyautogui.moveTo(*max_loc)
