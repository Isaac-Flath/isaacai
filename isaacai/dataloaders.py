# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/10_dataloaders.ipynb.

# %% auto 0
__all__ = ['get_dataloaders', 'collate_dataset_dict', 'DataLoaders', 'sample_dataset_dict']

# %% ../nbs/10_dataloaders.ipynb 4
from .utils import *
import pandas as pd, numpy as np, fastcore.all as fc
import matplotlib.pyplot as plt,matplotlib as mpl
import random
import torch
from torch import nn, Tensor
from torch.utils.data import DataLoader
from datasets import Dataset, load_dataset
import torchvision.transforms.functional as TF,torch.nn.functional as F
from torch.utils.data import default_collate
from operator import itemgetter

# %% ../nbs/10_dataloaders.ipynb 6
@fc.delegates(DataLoader)
def get_dataloaders(train_dataset, valid_dataset, batch_size, **kwargs):
    return (DataLoader(train_dataset, batch_size=batch_size, shuffle=True, **kwargs),
            DataLoader(valid_dataset, batch_size=batch_size*2, shuffle=False, **kwargs))

# %% ../nbs/10_dataloaders.ipynb 7
def collate_dataset_dict(dataset):
    get = itemgetter(*dataset.features)
    def _f(b): return get(default_collate(b))
    return _f

# %% ../nbs/10_dataloaders.ipynb 8
class DataLoaders():
    def __init__(self, train, valid): fc.store_attr()
    
    @classmethod
    def from_dataset_dict(cls, dataset_dict, batch_size, **kwargs):
        f = collate_dataset_dict(dataset_dict['train'])
        return cls(*get_dataloaders(*dataset_dict.values(), batch_size=batch_size, collate_fn=f))

    @fc.delegates(get_grid)
    def show_batch(self, n=9, train_dataset=True, **kwargs):
        _dataset = getattr(self, 'train').dataset if train_dataset else getattr(self, 'valid').dataset
        batch = list(zip(*_dataset[random.sample(range(len(_dataset)),n)].values()))
        fig,axs = get_grid(n=n,**kwargs)
        for (image,label),ax in zip(batch,axs.flat):
            show_image(image,ax=ax,title=_dataset.features['label'].names[label])

# %% ../nbs/10_dataloaders.ipynb 9
@inplace
def sample_dataset_dict(dataset, sample_sizes=(2000,2000)):
    for sample_size,name in zip(sample_sizes,dataset):
        sample_idxs = random.sample(range(len(dataset[name])),sample_size)
        dataset[name] = dataset[name].select(sample_idxs)
