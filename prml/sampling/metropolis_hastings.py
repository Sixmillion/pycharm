import random
import numpy as np


def metropolis_hastings(func, rv, n, downsample=1):
    """
    Metropolis Hastings algorithm

    Parameters
    ----------
    func : callable
        (un)normalized distribution to be sampled from
    rv : RandomVariable
        proposal distribution
    n : int
        number of samples to draw
    downsample : int
        downsampling factor

    Returns
    -------
    sample : (n, ndim) ndarray
        generated sample
    """
    x = np.zeros((1, rv.ndim))
    sample = []
    for i in range(n * downsample):
        x_new = x + rv.draw()   #因为rv.draw是从均值为0的高斯分布采样，所以此处x_new就相当于从q(z|z(τ))中采样   PRML p370
        accept_proba = func(x_new) * rv.pdf(x - x_new) / (func(x) / rv.pdf(x_new - x)) #后一个除号原本是称号，我认为其有误，改为除号，，，，，此处减号就是在改变高斯分布的均值
        if random.random() < accept_proba:
            x = x_new
        if i % downsample == 0:
            sample.append(x[0])
    sample = np.asarray(sample)
    assert sample.shape == (n, rv.ndim), sample.shape
    return sample
