# how to use libs(package)
## pip(without anaconda)
```shell
pip install package_name
```
## conda
Activate the conda env first.
```shell
conda install package_name
```
# numpy(data structure)
"The fundamental package for scientific computing with Python"
[numpy website](https://numpy.org/)
Support a large number of **dimensional arrays** and matrix operations.
It also provides a large number of mathematical functions library for array operations.
## why numpy?
 - fast
 - easy
 - wildly used
## How to use?
[A very good introduction to numpy](https://jalammar.github.io/visual-numpy/)
or official tutorial

# scipy(algorithm)
"Fundamental algorithms for scientific computing in Python"
[scipy website](https://scipy.org/)
Scipy contains modules for optimization, linear algebra, integration, interpolation, special functions, Fast Fourier transform, signal processing and image processing, ordinary differential equation, and other computations commonly used in science and engineering.
## You may use
```python
import scipy.stats as st
```
## how to use
Official tutorial
# matplotlib(plot)
"Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python."
[matplotlib website](https://matplotlib.org/)
## how to use
Official tutorial
 - tips: for beginners, skip the first tutorial and only read [pyplot](https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py). I think in this class plot is not so important and we can use a easier way.
## loglog
The official document is [loglog](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.loglog.html#matplotlib.pyplot.loglog)
This is just a thin wrapper around `plot` which additionally changes both the x-axis and the y-axis to log scaling. All of the concepts and parameters of plot can be used here as well.

```python
import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(1e-5, 10, 100)
print(x)
y = x ** 5

fig = plt.figure(figsize=(5.5,8))

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(x, y)
ax1.set_title("x-y")

ax2.loglog(x, y)
ax2.set_title("loglog")

ax3.plot(x, y)
ax3.set_xscale('log')
ax3.set_title("logx")

ax4.plot(x, y)
ax4.set_yscale('log')
ax4.set_title("logy")
plt.show()
```
# basic conda commands
```shell
conda --version
conda config --show
conda update conda
conda create -n env_name python=python_version
# the follow 3 commands are the same
conda env list
conda info -e
conda info --envs

conda activate env_name
conda deactivate
conda remove --name env_name --all # delete env + all pkgs
conda remove --name env_name  package_name # delete specific pkg
# get env info
conda env export --name myenv > myenv.yml
# create env with info
conda env create -f  myenv.yml

conda list
conda install package_name
conda install package_name=version
conda update package_name
conda uninstall package_name

# change python version
conda install python=version

conda update python
```