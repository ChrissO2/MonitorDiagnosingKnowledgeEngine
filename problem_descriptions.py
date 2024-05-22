from enum import Enum


class ProblemDescription(Enum):
    BLACK_SCREEN = 'ekran czarny lub obraz miga'
    DIM_SCREEN = 'wyświetlany obraz jest zbyt ciemny'
    NO_INPUT_SIGNAL = 'komunikat Input Signal Not Found'
    OUT_OF_RANGE = 'komunikat Input Signal Out of Range'
    POWER_SAVING = 'monitor wyłączony, ale nie w trybie uśpienia'
    OSD_LOCKOUT = 'komunikat OSD Lockout'
    POWER_BUTTON_LOCKOUT = 'komunikat Power Button Lockout'
    