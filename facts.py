from experta import Fact, Field


class Problem(Fact):
    """Fakt reprezentujący problem z monitorem"""
    description = Field(str, mandatory=True)
    is_cable_connected = Field(bool, default=True)
    is_monitor_on = Field(bool, default=True)
    is_sleep_mode_active = Field(bool, default=True)


class Solution(Fact):
    """Fakt reprezentujący sugerowane rozwiązanie problemu"""
    step = Field(str, mandatory=True)