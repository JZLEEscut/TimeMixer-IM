# Initial public release scope

This repository is intentionally not a reproduction package. The current release exposes only project structure and stable interface contracts.

## Included

- README and license;
- example JSON schemas without local paths or result values;
- dataset-independent Python interfaces;
- one interface-level test;
- a release policy recording the exclusions.

## Excluded

The private project remains outside this repository. In particular, the following are excluded: TimeMixer or TimeMixer-IM source, model heads, loss functions, data adapters, training and cloud runners, raw M5/Favorita data, checkpoints, predictions, logs, paper LaTeX/PDF files, figures, result tables, and asset manifests.

## Future staged releases

After the paper is publicly available, each additional release should be reviewed separately. A possible sequence is: data-free utilities, synthetic-data examples, selected baseline implementations, and finally the core implementation if the authors decide that release is appropriate.
