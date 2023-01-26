"""
    File name: train
    Description: run code start from here
    Author: Botian Lan
    Time: 2023/01/25
"""

from options import *
import model

arg = HierP2POptions()
options = arg.parse()

if __name__ == "__main__":
    trainer = model.Trainer(options)
    trainer.train()
