#!/usr/bin/env python3
# Author ID: jtuma
import os
def free_space():
    return os.popen("df -h | grep '/$' | awk '{print $4}'").read().strip()