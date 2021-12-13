<a href="https://github.com/Matatika/tap-meltano/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/Matatika/tap-meltano"></a>
# tap-meltano

`tap-meltano` is a Singer tap for meltano.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

- [ ] `Developer TODO:` Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

```bash
pipx install tap-meltano
```

## Configuration

### Settings

Currently the only required setting, or setting at all, for this tap is `meltano_database_uri`. This setting points the tap to the database where you want to get the Meltano jobs from.

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-meltano --about
```

### State

No state support at the moment, this tap will full sync from the target `meltano_database_uri` each time you run it.

## Usage

You can easily run `tap-meltano` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-meltano --version
tap-meltano --help
tap-meltano --config CONFIG --discover > ./catalog.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_meltano/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-meltano` CLI interface directly using `poetry run`:

```bash
poetry run tap-meltano --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-meltano
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-meltano --version
# OR run a test `elt` pipeline:
meltano elt tap-meltano target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.
