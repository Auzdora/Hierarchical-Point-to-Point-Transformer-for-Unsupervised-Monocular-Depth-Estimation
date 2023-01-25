"""
    File name: train
    Description: run code start from here
    Author: Botian Lan
    Time: 2023/01/25
"""

from options import *

arg = HierP2POptions()
options = arg.parse()

print(options.epoch)
