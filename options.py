"""
    File name: options
    Description: provide basic options for model
    Author: Botian Lan
    Time: 2023/01/25
"""

import os
import argparse


class HierP2POptions:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Hierarchical Point to Point Transformer options")

        # Hyper parameters
        self.parser.add_argument("--epoch",
                                 type=int,
                                 help="the epoch that model runs",
                                 default=30)
        self.parser.add_argument("--batch_size",
                                 type=int,
                                 help="batch size",
                                 default=4)
        self.parser.add_argument("--lr",
                                 type=float,
                                 help="learning rate",
                                 default=1e-4)
        self.parser.add_argument("--scheduler_step_size",
                                 type=int,
                                 help="step size of scheduler",
                                 default=10)



        self.opt = self.__getArg()

    def __getArg(self):
        opt = self.parser.parse_args()
        return opt

    def parse(self):
        """
            return the initialized option
        """
        return self.opt
