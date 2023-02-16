# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_utils.ipynb.

# %% auto 0
__all__ = ['def_device', 'set_seed', 'inplace', 'mask2idxs', 'PPDict', 'copy_func', 'clean_ipython_hist', 'clean_traceback',
           'clean_mem', 'to_device', 'to_cpu', 'show_image', 'subplots', 'get_grid', 'run_callbacks', 'add_callback',
           'add_callbacks', 'remove_callback', 'remove_callbacks', 'with_cbs']

# %% ../nbs/00_utils.ipynb 4
import fastcore.all as fc
import random
import torch
from typing import Mapping
import matplotlib.pyplot as plt
import math
import numpy as np
from itertools import zip_longest
from datetime import timedelta

import types
import inspect
import functools

# %% ../nbs/00_utils.ipynb 6
def set_seed(seed, deterministic=False):
    torch.use_deterministic_algorithms(deterministic)
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)

# %% ../nbs/00_utils.ipynb 7
def inplace(f):
    '''Return the object passed to the function for in place mods'''
    def _f(b):
        f(b)
        return b
    return _f

# %% ../nbs/00_utils.ipynb 8
def mask2idxs(mask): return [i for i, e in enumerate(mask) if e == True]

# %% ../nbs/00_utils.ipynb 10
class PPDict(dict):
    def __str__(self):
        out = {}
        for k,v in self.items():
            if isinstance(v,float): out[k] = round(v,4)
            elif isinstance(v,timedelta): out[k] = str(timedelta(seconds=math.ceil(v.total_seconds())))
            else: out[k] = v
        return str(out)  

# %% ../nbs/00_utils.ipynb 11
def copy_func(f):
    """Based on http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)"""
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__,
                           argdefs=f.__defaults__,
                           closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g

# %% ../nbs/00_utils.ipynb 13
def clean_ipython_hist():
    # Code in this function mainly copied from IPython source
    if not 'get_ipython' in globals(): return
    ip = get_ipython()
    user_ns = ip.user_ns
    ip.displayhook.flush()
    pc = ip.displayhook.prompt_count + 1
    for n in range(1, pc): user_ns.pop('_i'+repr(n),None)
    user_ns.update(dict(_i='',_ii='',_iii=''))
    hm = ip.history_manager
    hm.input_hist_parsed[:] = [''] * pc
    hm.input_hist_raw[:] = [''] * pc
    hm._i = hm._ii = hm._iii = hm._i00 =  ''

# %% ../nbs/00_utils.ipynb 14
def clean_traceback():
    '''Objects in tracebacks are stored in memory, even cuda memory.
    This clears that traceback memory up'''
    # h/t Piotr Czapla
    if hasattr(sys, 'last_traceback'):
        traceback.clear_frames(sys.last_traceback)
        delattr(sys, 'last_traceback')
    if hasattr(sys, 'last_type'): delattr(sys, 'last_type')
    if hasattr(sys, 'last_value'): delattr(sys, 'last_value')

# %% ../nbs/00_utils.ipynb 15
def clean_mem():
    '''Cleans all memory from hist and tracebacks'''
    clean_tb()
    clean_ipython_hist()
    gc.collect()
    torch.cuda.empty_cache()

# %% ../nbs/00_utils.ipynb 17
def_device = 'mps' if torch.backends.mps.is_available() else 'cuda' if torch.cuda.is_available() else 'cpu'

def to_device(x, device=def_device):
    if isinstance(x, torch.Tensor): return x.to(device)
    if isinstance(x, Mapping): return {k:v.to(device) for k,v in x.items()}
    return type(x)(to_device(o, device) for o in x)

def to_cpu(x):
    if isinstance(x, Mapping): return {k:to_cpu(v) for k,v in x.items()}
    if isinstance(x, list): return [to_cpu(o) for o in x]
    if isinstance(x, tuple): return tuple(to_cpu(list(x)))
    return x.detach().cpu()

# %% ../nbs/00_utils.ipynb 19
@fc.delegates(plt.Axes.imshow)
def show_image(im, ax=None, figsize=None, title=None, noframe=True, **kwargs):
    '''Show a PIL or PyTorch image on `ax`
        + Moves to cpu & detach
        + converts to numpy
        + remove axis ticks
    '''
    if fc.hasattrs(im, ('cpu','permute','detach')):
        im = im.detach().cpu()
        if len(im.shape)==3 and im.shape[0]<5: im=im.permute(1,2,0)
    elif not isinstance(im,np.ndarray): im=np.array(im)
    if im.shape[-1]==1: im=im[...,0]
    if ax is None: _,ax = plt.subplots(figsize=figsize)
    ax.imshow(im, **kwargs)
    if title is not None: ax.set_title(title)
    ax.set_xticks([]) 
    ax.set_yticks([]) 
    if noframe: ax.axis('off')
    return ax

# %% ../nbs/00_utils.ipynb 20
@fc.delegates(plt.subplots, keep=True)
def subplots(
    nrows:int=1, # Number of rows in returned axes grid
    ncols:int=1, # Number of columns in returned axes grid
    figsize:tuple=None, # Width, height in inches of the returned figure
    imsize:int=3, # Size (in inches) of images that will be displayed in the returned figure
    suptitle:str=None, # Title to be set to returned figure
    **kwargs
): # fig and axs
    "A figure and set of subplots to display images of `imsize` inches"
    if figsize is None: figsize=(ncols*imsize, nrows*imsize)
    fig,ax = plt.subplots(nrows, ncols, figsize=figsize, **kwargs)
    if suptitle is not None: fig.suptitle(suptitle)
    if nrows*ncols==1: ax = np.array([ax])
    return fig,ax

# %% ../nbs/00_utils.ipynb 21
@fc.delegates(subplots)
def get_grid(
    n:int, # Number of axes
    nrows:int=None, # Number of rows, defaulting to `int(math.sqrt(n))`
    ncols:int=None, # Number of columns, defaulting to `ceil(n/rows)`
    title:str=None, # If passed, title set to the figure
    weight:str='bold', # Title font weight
    size:int=14, # Title font size
    **kwargs,
): # fig and axs
    "Return a grid of `n` axes, `rows` by `cols`"
    if nrows: ncols = ncols or int(np.floor(n/nrows))
    elif ncols: nrows = nrows or int(np.ceil(n/ncols))
    else:
        nrows = int(math.sqrt(n))
        ncols = int(np.floor(n/nrows))
    fig,axs = subplots(nrows, ncols, **kwargs)
    for i in range(n, nrows*ncols): axs.flat[i].set_axis_off()
    if title is not None: fig.suptitle(title, weight=weight, size=size)
    return fig,axs

# %% ../nbs/00_utils.ipynb 23
def run_callbacks(callbacks, method_name, trainer=None):
    for callback in sorted(callbacks, key=lambda x: getattr(x, 'order',0)):
        callback_method = getattr(callback, method_name,None)
        if callback_method is not None: callback_method(trainer)

# %% ../nbs/00_utils.ipynb 25
def add_callback(trainer,callback,force=False):
    trainer.callbacks = getattr(trainer,'callbacks',fc.L())
    if callback is None: return None
    cb_name = callback.__class__.__name__
    
    if cb_name in trainer.callbacks: 
        if force: remove_callback(trainer,callback,True)
        else: assert cb_name not in trainer.callbacks
    
    trainer.callbacks.append(cb_name)
    setattr(trainer,cb_name,callback)
    
def add_callbacks(trainer,callbacks,force=False):
    trainer.callbacks = getattr(trainer,'callbacks',fc.L())
    for callback in callbacks: add_callback(trainer,callback, force)

# %% ../nbs/00_utils.ipynb 26
def remove_callback(trainer,callback,delete=False):
    cb_name = callback.__class__.__name__
    trainer.callbacks.remove(cb_name)
    if delete: delattr(trainer,cb_name)
    
def remove_callbacks(trainer,callbacks,delete=False):
    for callback in callbacks: remove_callback(trainer, callback, delete)

# %% ../nbs/00_utils.ipynb 27
class with_cbs:
    def __init__(self, nm, exception): fc.store_attr()
    def __call__(self, f):
        def _f(o, *args, **kwargs):
            try:
                o.run_callbacks(f'before_{self.nm}')
                f(o, *args, **kwargs)
                o.run_callbacks(f'after_{self.nm}')
            except self.exception: pass
            finally: o.run_callbacks(f'cleanup_{self.nm}')
        return _f
