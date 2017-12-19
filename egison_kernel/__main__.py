from ipykernel.kernelapp import IPKernelApp
from .kernel import EgisonKernel
IPKernelApp.launch_instance(kernel_class=EgisonKernel)
