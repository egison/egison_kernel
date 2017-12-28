# Egison kernel for Jupyter

## How to install

```sh
git clone https://github.com/egison/egison_kernel.git
cd egison_kernel
pip install .  # install dependencies
python -m egison_kernel.install  # install Egison kernel itself
```

After that, copy `egison_kernel/codemirror/mode/egison/egison.js` to Jupyter's CodeMirror directory.

## How to use

```
jupyter notebook
# In the notebook interface, select Egison from the 'New' menu
```

<img width="100%" src="https://raw.githubusercontent.com/egison/egison_kernel/master/images/RiemannCurvatureOfS2.png" />

## Acknowledgement

I learned how to implement a Jupyter kernel from [bash_kernel](https://github.com/takluyver/bash_kernel).

I thank Shunsuke Gotoh for [his article](https://qiita.com/antimon2/items/7d9c084b142d38b67b1f) on the initial Python program of this kernel.
