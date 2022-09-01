---
title: "ctapipe generate R1/DL0 HDF5"
author: "Thomas Vuillaume"
date: "2022-09-01"
format:
  html:
    code-fold: true
    theme: minty
    categories: []
    page-layout: full
---

# ctapipe generate HDF5 with R1/DL0 waveforms

```
ctapipe-quickstart
```

will generate a base config

Edit the config with:

``` 
  write_showers: true # store DL2 stereo geometry
  write_raw_waveforms: true # write R0 waveforms
  write_waveforms: true # write R1 waveforms
  transform_waveform: true
  waveform_dtype: "uint16"
  waveform_offset: 400
  waveform_scale: 80
```

The waveforms are scaled to fit in `uint16` and scaled back at reading.

Then run:

```
ctapipe-process --config base_config.yaml --input ../Simtel/prod5/gamma_20deg_0deg_run5___cta-prod5-paranal_desert-2147m-Paranal-dark.simtel.zst --output gamma_20deg_0deg_run5___cta-prod5-paranal_desert-2147m-Paranal-dark.h5
```