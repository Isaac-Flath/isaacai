# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/49_cb_groups.ipynb.

# %% auto 0
__all__ = ['CoreCBs']

# %% ../nbs/49_cb_groups.ipynb 4
from .utils import *
from .dataloaders import *
from .models import *
from .initialization import *
from .trainer import *
from .training import *
from .recording import *
from .visualization import *

from datetime import datetime, timedelta
import torchvision.transforms.functional as TF,torch.nn.functional as F
import math, time

import matplotlib.pyplot as plt
import matplotlib as mpl
import fastcore.all as fc
import torch
from torch import nn, Tensor
from datasets import load_dataset, Dataset
from torch.utils.data import DataLoader
import pandas as pd , numpy as np
from torcheval.metrics import MulticlassAccuracy,Mean
from torch.optim.lr_scheduler import ExponentialLR

import dill as pickle
from fastprogress.fastprogress import master_bar, progress_bar
import inspect
import torchinfo


# %% ../nbs/49_cb_groups.ipynb 9
class CoreCBs:
    def __init__(self,device=def_device,module_filter=fc.noop,**metrics):
        self.callbacks = [DeviceCB(device=device),
                          BasicTrainCB(),
                          MetricsCB(**metrics),
                          ProgressCB(),
                          ActivationStatsCB(module_filter)]
        

