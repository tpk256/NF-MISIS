from vkbottle import BaseStateGroup


class MenuStates(BaseStateGroup):
    MAIN_STATE = "MAIN_STATE"

class ScheduleStates(BaseStateGroup):
    WAIT_COURSE_STATE = "WAIT_COURSE_STATE"
    WAIT_PARITY_STATE = "WAIT_COURSE_STATE"