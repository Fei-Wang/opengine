from typing import Optional

import torch

TORCH_VERSION = torch.__version__


def is_rocm_pytorch() -> bool:
    """Check whether the PyTorch is compiled on ROCm."""
    is_rocm = False
    try:
        from torch.utils.cpp_extension import ROCM_HOME
        is_rocm = True if ((torch.version.hip is not None) and
                           (ROCM_HOME is not None)) else False
    except ImportError:
        pass
    return is_rocm


def _get_cuda_home() -> Optional[str]:
    """Obtain the path of CUDA home."""
    if is_rocm_pytorch():
        from torch.utils.cpp_extension import ROCM_HOME
        CUDA_HOME = ROCM_HOME
    else:
        from torch.utils.cpp_extension import CUDA_HOME
    return CUDA_HOME


def get_build_config():
    """Obtain the build information of PyTorch."""
    return torch.__config__.show()


def _get_conv() -> tuple:
    """A wrapper to obtain base classes of Conv layers from PyTorch."""
    from torch.nn.modules.conv import _ConvNd, _ConvTransposeMixin
    return _ConvNd, _ConvTransposeMixin


def _get_dataloader() -> tuple:
    """A wrapper to obtain DataLoader class from PyTorch."""
    from torch.utils.data import DataLoader
    PoolDataLoader = DataLoader
    return DataLoader, PoolDataLoader


def _get_extension():
    """A wrapper to obtain extension class from PyTorch."""
    from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension
    return BuildExtension, CppExtension, CUDAExtension


def _get_pool() -> tuple:
    """A wrapper to obtain base classes of pooling layers from PyTorch."""
    from torch.nn.modules.pooling import _AdaptiveAvgPoolNd, _AdaptiveMaxPoolNd, _AvgPoolNd, _MaxPoolNd
    return _AdaptiveAvgPoolNd, _AdaptiveMaxPoolNd, _AvgPoolNd, _MaxPoolNd


def _get_norm() -> tuple:
    """A wrapper to obtain base classes of normalization layers from PyTorch."""
    from torch.nn.modules.batchnorm import _BatchNorm
    from torch.nn.modules.instancenorm import _InstanceNorm
    SyncBatchNorm_ = torch.nn.SyncBatchNorm
    return _BatchNorm, _InstanceNorm, SyncBatchNorm_


_ConvNd, _ConvTransposeMixin = _get_conv()
DataLoader, PoolDataLoader = _get_dataloader()
_BatchNorm, _InstanceNorm, SyncBatchNorm_ = _get_norm()
_AdaptiveAvgPoolNd, _AdaptiveMaxPoolNd, _AvgPoolNd, _MaxPoolNd = _get_pool()


class SyncBatchNorm(SyncBatchNorm_):  # type: ignore

    def _check_input_dim(self, input):
        super()._check_input_dim(input)
