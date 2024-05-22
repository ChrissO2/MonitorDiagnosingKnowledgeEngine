from experta import Fact, Field


class Problem(Fact):
    """Fact representing a problem with a monitor"""
    description = Field(str, mandatory=True)
    is_cable_connected = Field(bool, default=True)
    is_monitor_on = Field(bool, default=True)
    is_sleep_mode_active = Field(bool, default=True)


class Solution(Fact):
    """Fact representing a solution to a problem with a monitor"""
    step = Field(str, mandatory=True)
