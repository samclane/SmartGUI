import pyautogui, time, os, logging, sys, random, copy
from smart_gui import Workflow, WorkflowStep, fuzzy_find, basic_find

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment to block debug log messages

JOIN_TEAM_OFF = ".\smart_gui\images\discord\join_team_off.png"
LEAVE_TEAM_OFF = ".\smart_gui\images\discord\leave_team_off.png"
JOIN_TEAM_ON = ".\smart_gui\images\discord\join_team_on.png"
LEAVE_TEAM_ON = ".\smart_gui\images\discord\leave_team_on.png"


class JoinStep(WorkflowStep):
    def target(self):
        try:
            basic_find(JOIN_TEAM_OFF, show_im=False)
        except TypeError as e:
            pyautogui.alert("Image not found!")
            self.failed = True

    def select(self):
        if not self.failed:
            pyautogui.click()
    
    def failover(self):
        print("JOIN FAILOVER")

join_workflow = Workflow()
join_workflow.append(JoinStep())
join_workflow.run_flow()