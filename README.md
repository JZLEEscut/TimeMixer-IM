# TimeMixer-IM public research framework

This repository is a deliberately minimal public scaffold for the TimeMixer-IM research project. It documents the public-facing experiment layout and interfaces without publishing the unpublished model implementation, training code, data, checkpoints, predictions, paper assets, or experimental results.

## Scope

The repository currently contains:

- a dataset-independent experiment layout;
- example configuration files with placeholder paths;
- small interface stubs for a future implementation;
- testing and contribution conventions.

The research manuscript is not included. Reproduction is not currently supported from this repository alone. After publication, additional code and selected assets may be released in reviewed stages.

## Planned layout

```text
configs/       Public, non-sensitive example configurations
docs/          Scope, data, and release notes
src/           Public interfaces only; no model implementation
tests/         Interface-level checks only
```

## Security and release policy

Do not commit datasets, raw transaction files, trained weights, prediction arrays, logs, result tables, private paths, cloud credentials, or unpublished manuscript material. Release additions must be reviewed against this policy and the corresponding paper status.

## Status

This is an initial framework release. It is intended to make the project structure visible while protecting the unpublished implementation. Issues and suggestions about the public interfaces are welcome.

## License

The scaffold is released under the MIT License. This license applies only to files in this repository and does not grant rights to unpublished research materials held elsewhere.
