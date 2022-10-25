# Application Setup using `setup.py`

## Non-PyPI Libraries

Sometimes while developing an application, you may be simultaneously developing other applications, or you may be using applications that are stored in a private repository. In such cases, you do not have a PyPI alias that you can use in your `setup.py` file. Instead, you can tell Python to install these libraries directly from GitHub. This has the following advantages:

- You can simultaneously develop multiple applications
- You can use private dependencies for your applications
- You can pin your applications to a specific branch or tag
- You can install applications from a subdirectory on a repository

Instead of using the PyPI alias, you need to use a valid http or ssh link to point to the repository that you wish to use. Below are examples for GitHub and GitLab.

### GitHub


TODO need to convert this to https to show that as well
```bash
# app from repository. `setup.py` must be at the root of the repo 
{APP_NAME}@git+ssh://git@github.com/{USER}/{REPO_NAME}.git

# private dependency, using ssh OR http (with authentication)
{APP_NAME}@git+ssh://git@github.com/{USER}/{REPO_NAME}.git

# specific branch or tag
{APP_NAME}@git+ssh://git@github.com/{USER}/{REPO_NAME}.git@{TAG/BRANCH}

# app from subdirectory of repository. Useful if `setup.py` appears in a directory
{APP_NAME}@git+ssh://git@github.com/{USER}/{REPO_NAME}.git@{TAG/BRANCH}#subdirectory={SUBDIRECTORY}

```

### GitLab
TODO add the same but for gitlab link

An example `setup.py` using the above is shown below:
```python
from setuptools import setup

base_packages = ['pandas']
private_dev_packages = [
    'in-n-out-sdk@git@github.com/namiyousef/in-n-out.git@develop#subdirectory=sdk'
]

setup(
    install_requires=base_packages+private_dev_packages
)
```