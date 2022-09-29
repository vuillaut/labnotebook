---
title: "conda must config"
author: "Thomas Vuillaume"
date: "2022-07-22"
format:
  html:
    code-fold: true
    theme: minty
    categories: [notes]
    page-layout: full
---


# Use shared conda

```
__conda_setup="$('/usr/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
eval "$__conda_setup"
```

# Setup config

```
conda config
```

Will generate a `.condarc` file in the home directory.

Edit this file to add the following:

```
envs_dirs:
  - /mustfs/CONTAINERS/conda/glearn/envs/

pkgs_dirs:
  - /mustfs/CONTAINERS/conda/glearn/pkgs/

channels:
  - conda-forge
  - defaults
```

Changing `pkgs_dirs` and `envs_dirs` is necessary to avoid hitting disk quotas in your own home directory.
Create new directories to set these paths. This will avoid mutli-users installation and writing rights issues.