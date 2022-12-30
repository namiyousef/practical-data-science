# practical-data-science
Notes on Practical Data Science

# Build book
```bash
pip install jupyter-book
jupyter-book build {PATH_TO_BOOK_DIRECTORY}
```

# Troubleshooting

## During book build

### No such kernel
This means that one of the Jupyter Notebooks in your book requires a Python 
kernel that you have not added to your Jupyter kernels list. You can check 
if this is the case using: `jupyter kernelspec list`.

If you don't find it there, then you can install the kernel as follows:
```bash
pip install ipython
ipython kernel install --name {KERNEL_NAME} --user
```

The `--user` command is necessary to circumvent potential Permission Denied 
errors.

# Build book
```bash
pip install jupyter-book
jupyter-book build {PATH_TO_BOOK_DIRECTORY}
```

# Troubleshooting

## During book build

### No such kernel
This means that one of the Jupyter Notebooks in your book requires a Python 
kernel that you have not added to your Jupyter kernels list. You can check 
if this is the case using: `jupyter kernelspec list`.

If you don't find it there, then you can install the kernel as follows:
```bash
pip install ipython
ipython kernel install --name {KERNEL_NAME} --user
```

The `--user` command is necessary to circumvent potential Permission Denied 
errors.