---
title: "analyse LST-1 data"
author: "Thomas Vuillaume"
date: "2022-07-27"
format:
  html:
    code-fold: true
    theme: minty
    categories: []
    page-layout: full
---


# How to analyse LST-1 data

## Get the data

From the LST wiki page, or the elogs, find the runs you want to analyse.
Find the corresponding DL1 files on the cluster, probably under `/fefs/aswg/data/real/DL1/.../`.
These files have been automatically produced by LSTOSA, there might be several versions, corresponding to different 
lstchain versions. In doubt, use the last one.

## Select the data

You might want to sub-select the runs to use, following https://indico.cta-observatory.org/event/3984/


## Corresponding MC production

The AllSky MC production follows sources declinations, as explained in:
- https://indico.cta-observatory.org/event/4061/contributions/33409/attachments/21211/29956/Crab_analysis_20220404.pdf
- ??

Random forests models are trained per declination and then used on the MC test data
to produce IRFs on all test pointing directions.

## Produce your DL2 files

From the DL1 files, you will need to produce the DL2 files using the right RF model.

### Standard RF models and IRFs
If you are analysing an extragalactic source, the standard models trained for the closest declination of your source is 
likely enough.
You can find these models under 
```
/fefs/aswg/data/models/AllSky/.../
```

Apply the model to the DL1 files using lstchain `lstchain_dl1_to_dl2`

In this case, you can also use the corresponding standard IRFSs, under `/fefs/aswg/data/IRF/AllSky/.../`.

### Custom RF models and IRFs

If your source needs MC tuning (e.g. for strong NSB / galactic sources):
1. please check that a fitting custom training does not exist from [https://cta-observatory.github.io/lstmcpipe/productions.html](https://cta-observatory.github.io/lstmcpipe/productions.html)
2. if not, you may request a custom training using lstmcpipe pull-requests: [https://cta-observatory.github.io/lstmcpipe/index.html#requesting-a-mc-analysis](https://cta-observatory.github.io/lstmcpipe/index.html#requesting-a-mc-analysis)

The lstchain config must be produced using `lstchain_tune_nsb` on the DL1 files you want to analyse.

The lstmcpipe config must be produced following: [https://cta-observatory.github.io/lstmcpipe/pipeline.html#allsky-production-pipeline](https://cta-observatory.github.io/lstmcpipe/pipeline.html#allsky-production-pipeline)

## Produce your DL3 files

`lstchain_create_dl3_file`

## High-level analysis

Use gammapy to analyse the DL3 files using the corresponding IRFs.