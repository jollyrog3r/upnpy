# -*- coding: utf-8 -*-
"""
device.py
~~~~~~~~~

Defines the structure for generic UPnP devices. This can be viewed as a form of
"base device" against which all other UPnP devices are implemented.

A "device" is a slightly abstract notion in UPnP, and does not directly
correspond to a network element. Any given network element may actually be
multiple UPnP devices, or may be only a single UPnP device.
"""

class Device(object):
    """
    The base class for all UPnP devices. This class defines the expected
    interactions for all UPnP device classes. Additionally, when there is no
    suitable more-specific class that applies for a specific UPnP device, this
    class will be used to represent it.
    """
    def __init__(self):
        self.server = ''
        self.service_name = ''
        self.search_target = ''