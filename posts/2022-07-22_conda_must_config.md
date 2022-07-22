---
title: "conda must config"
author: "Thomas Vuillaume"
date: "2022-07-22"
format:
  html:
    code-fold: true
    theme: minty
    categories: []
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

Edit this file:

```
envs_dirs:
  - /mustfs/CONTAINERS/conda/glearn/envs/

pkgs_dirs:
  - /mustfs/CONTAINERS/conda/glearn/pkgs/

channels:
  - conda-forge
  - defaults
```
