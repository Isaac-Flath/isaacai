# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/42_recording.ipynb.

# %% auto 0
__all__ = ['MetricsCB', 'ProgressCB']

# %% ../nbs/42_recording.ipynb 4
from .utils import *
from .dataloaders import *
from .models import *
from .initialization import *
from .trainer import *
from .training import *

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

# %% ../nbs/42_recording.ipynb 10
class MetricsCB(Callback):
    '''Callback to track train/valid loss + metrics'''
    def __init__(self, **metrics):
        self.metrics = metrics
        self.losses = {'train':Mean(),'valid':Mean()}
        self.metrics_epoch,self.losses_epoch,self.losses_batch = [],[],[]
            
    def after_batch(self,trainer):
        '''stores losses and metrics for batch'''        
        self.losses[f"{'train' if trainer.training else 'valid'}"].update(to_cpu(trainer.loss),weight=len(trainer.batch[1]))
        if not trainer.training:
            preds,batch = map(to_cpu,[trainer.preds,trainer.batch[1]])    
            for k in self.metrics: self.metrics[k].update(preds,batch)
        self.losses_batch.append({'training':trainer.training,'loss':to_cpu(trainer.loss)})
            
    def cleanup_epoch(self,trainer):
        '''compute metrics and append to epoch stats and display'''
        if not trainer.training:
            self.metrics_epoch.append({name:float(metric.compute()) for name, metric in self.metrics.items()})
            self.losses_epoch.append({name:float(metric.compute()) for name, metric in self.losses.items()})

            for metric in self.metrics.values(): metric.reset()
            for metric in self.losses.values(): metric.reset()

# %% ../nbs/42_recording.ipynb 14
class ProgressCB(Callback):
    '''Callback to display progress while training'''
        
    def before_fit(self,trainer):
        '''Initialize Fit Progress Bar'''
        trainer.epochs = master_bar(trainer.epochs)
        
    def before_epoch(self,trainer):
        '''Initialize Epoch Progress Bar'''
        trainer.batches = progress_bar(trainer.batches,parent=trainer.epochs)
        trainer.epochs.child.comment = "Training" if trainer.training else "Validation"
        
    def cleanup_epoch(self,trainer):
        '''Display Loss and Metric'''
        if not trainer.training: 
            df = pd.concat(map(pd.DataFrame,[trainer.MetricsCB.losses_epoch,trainer.MetricsCB.metrics_epoch]),axis=1).tail(1)
            if trainer.epoch != 0: df = df.style.set_table_styles([{'selector': 'thead', 'props': [('display', 'none')]}])
            display(df)
