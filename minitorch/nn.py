import numpy as np
from .fast_ops import FastOps
from .tensor_functions import rand, Function
from . import operators
from .tensor_data import (
    count,
    index_to_position,
    broadcast_index,
    MAX_DIMS,
)
from numba import njit, prange


def tile(input, kernel):
    """
    Reshape an image tensor for 2D pooling

    Args:
        input (:class:`Tensor`): batch x channel x height x width
        kernel ( pair of ints ): height x width of pooling

    Returns:
        (:class:`Tensor`, int, int) : Tensor of size batch x channel x new_height x new_width x kernel_height x kernel_width as well as the new_height and new_width value.
    """

    batch, channel, height, width = input.shape
    kh, kw = kernel
    assert height % kh == 0
    assert width % kw == 0
    # TODO: Implement for Task 4.2.
    raise NotImplementedError('Need to implement for Task 4.2')

def maxpool2d(input, kernel):
    """
    Tiled max pooling 2D

    Args:
        input (:class:`Tensor`): batch x channel x height x width
        kernel ( pair of ints ): height x width of pooling

    Returns:
        :class:`Tensor` : pooled tensor
    """
    batch, channel, height, width = input.shape
    # TODO: Implement for Task 4.2.
    raise NotImplementedError('Need to implement for Task 4.2')


def avgpool2d(input, kernel):
    """
    Tiled average pooling 2D

    Args:
        input (:class:`Tensor`): batch x channel x height x width
        kernel ( pair of ints ): height x width of pooling

    Returns:
        :class:`Tensor` : pooled tensor
    """
    batch, channel, height, width = input.shape
    # TODO: Implement for Task 4.2.
    raise NotImplementedError('Need to implement for Task 4.2')


def maxpool2d(input, kernel):
    """
    Tiled max pooling 2D

    Args:
        input (:class:`Tensor`): batch x channel x height x width
        kernel ( pair of ints ): height x width of pooling

    Returns:
        :class:`Tensor` : pooled tensor
    """
    batch, channel, height, width = input.shape
    # TODO: Implement for Task 4.2.
    raise NotImplementedError('Need to implement for Task 4.2')


def avgpool2d(input, kernel):
    """
    Tiled average pooling 2D

    Args:
        input (:class:`Tensor`): batch x channel x height x width
        kernel ( pair of ints ): height x width of pooling

    Returns:
        :class:`Tensor` : pooled tensor
    """
    batch, channel, height, width = input.shape
    # TODO: Implement for Task 4.2.
    raise NotImplementedError('Need to implement for Task 4.2')




max_reduce = FastOps.reduce(operators.max, -1e9)


max_reduce = FastOps.reduce(operators.max, -1e9)

def argmax(input, dim):
    """
    Compute the argmax as a 1-hot tensor.

    Args:
        input (:class:`Tensor`): input tensor
        dim (int): dimension to apply argmax


    Returns:
        :class:`Tensor` : tensor with 1 on highest cell in dim, 0 otherwise

    """
    out = max_reduce(input, [dim])
    return out == input


class Max(Function):
    @staticmethod
    def forward(ctx, input, dim):
        "Forward of max should be max reduction"
        # TODO: Implement for Task 4.3.
        raise NotImplementedError('Need to implement for Task 4.3')

    @staticmethod
    def backward(ctx, grad_output):
        "Backward of max should be argmax (see above)"
        # TODO: Implement for Task 4.3.
        raise NotImplementedError('Need to implement for Task 4.3')

max = Max.apply


def softmax(input, dim):
    r"""
    Compute the softmax as a tensor.

    .. math::

        z_i = \frac{e^{x_i}}{\sum_i e^{x_i}}

    Args:
        input (:class:`Tensor`): input tensor
        dim (int): dimension to apply argmax

    Returns:
        :class:`Tensor` : softmax tensor
    """
    # TODO: Implement for Task 4.3.
    raise NotImplementedError('Need to implement for Task 4.3')


def logsoftmax(input, dim):
    r"""
    Compute the log of the softmax as a tensor.

    .. math::

        z_i = x_i - \log \sum_i e^{x_i}

    See https://en.wikipedia.org/wiki/LogSumExp#log-sum-exp_trick_for_log-domain_calculations

    Args:
        input (:class:`Tensor`): input tensor
        dim (int): dimension to apply argmax

    Returns:
        :class:`Tensor` : log of softmax tensor
    """
    # TODO: Implement for Task 4.3.
    raise NotImplementedError('Need to implement for Task 4.3')


def tile(input, kernel):
    """
    Reshape an image tensor for 2D pooling

    Args:
        input (:class:`Tensor`): batch x channel x height x width
        kernel ( pair of ints ): height x width of pooling

    Returns:
        (:class:`Tensor`, int, int) : Tensor of size batch x channel x new_height x new_width x kernel_height x kernel_width as well as the new_height and new_width value.
    """

    batch, channel, height, width = input.shape
    kh, kw = kernel
    assert height % kh == 0
    assert width % kw == 0
    # TODO: Implement for Task 4.2.
    raise NotImplementedError('Need to implement for Task 4.2')


def maxpool2d(input, kernel):
    """
    Tiled max pooling 2D

    Args:
        input (:class:`Tensor`): batch x channel x height x width
        kernel ( pair of ints ): height x width of pooling

    Returns:
        :class:`Tensor` : pooled tensor
    """
    batch, channel, height, width = input.shape
    # TODO: Implement for Task 4.2.
    raise NotImplementedError('Need to implement for Task 4.2')


def dropout(input, rate, ignore=False):
    """
    Dropout dimensions based on random noise

    Args:
        input (:class:`Tensor`): input tensor
        rate (float): probability of dropping out each dimension
        ignore (bool): skip

    Returns:
        :class:`Tensor` : tensor with dropout dimensions
    """
    # TODO: Implement for Task 4.4.
    raise NotImplementedError('Need to implement for Task 4.4')
