"""
    File name: model
    Description: all important logic computing define in class Model
    Author: Botian Lan
    Time: 2023/01/26
"""

import time
import torch
import torch.nn.functional as F
import torch.optim as optim
import utils


class Trainer:
    def __init__(self, options):
        self.opt = options

        self._epoch_cnt = 0

    def train(self):
        """main logic of training process
        """
        for self._epoch_cnt in range(self.opt.epoch):
            self.train_epoch()

    def train_epoch(self):
        """training logic per epoch, handle the patch data
        """
        pass

    def validate(self):
        """validate the performance of the model
        """
        pass

    # loss computation
    def compute_loss(self):
        """compute the general loss
        """
        pass

    def proj_loss(self):
        """re-projection loss for the wrap images and the source image
           in different scales
        """
        pass

    def point2point_loss(self):
        """compute 3D point to point loss in different scales
        """
        pass
