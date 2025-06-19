---
layout: default
title: HPC in Wuerzburg
---

# HPC in Wuerzburg

## Summary

```markdown
| Partition |  GPUs   | GPU RAM | CPUs |   mem   |   tmpfs  |       Nodes        |  Host  |
| --------- | ------- | ------- | ---- | ------- | -------- | ------------------ | ------ |
| test      | 2x L40  |  48 GB  | 240  |  480 GB |  3380 GB | 1:  jntest01       | Julia2 |
|           |         |         |      |         |          |                    |        |
| standard  | 3x L40  |  48 GB  | 112  |  480 GB |  3380 GB | 20: jn[001-020]    | Julia2 |
| standard  | 3x L40  |  48 GB  | 224  |  480 GB |  3380 GB | 20: jn[101-120]    | Julia2 |
| standard  | 8x L40  |  48 GB  | 128  |  960 GB | 14300 GB | 3:  jnfat[01-03]   | Julia2 |
| standard  | 8x L40  |  48 GB  | 192  |  960 GB | 14300 GB | 2:  jnfat[08-09]   | Julia2 |
|           |         |         |      |         |          |                    |        |
| h100      | 8x H100 |  80 GB  | 224  | 1984 GB | 14300 GB | 2:  jnultra[01-02] | Julia2 |
|           |         |         |      |         |          |                    |        |
| dc-hwai   | 4x H100 | 128 GB  |  64  | ~502 GB | --       | 32: jrc[0910-0941] | Jureca |
```

