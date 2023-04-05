# napari-cellseg

[![License BSD-3](https://img.shields.io/pypi/l/napari-cellseg.svg?color=green)](https://github.com/CSDGroup/napari-cellseg/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-cellseg.svg?color=green)](https://pypi.org/project/napari-cellseg)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-cellseg.svg?color=green)](https://python.org)
[![tests](https://github.com/CSDGroup/napari-cellseg/workflows/tests/badge.svg)](https://github.com/CSDGroup/napari-cellseg/actions)
[![codecov](https://codecov.io/gh/CSDGroup/napari-cellseg/branch/main/graph/badge.svg)](https://codecov.io/gh/CSDGroup/napari-cellseg)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-cellseg)](https://napari-hub.org/plugins/napari-cellseg)

A [napari] plugin to segment cell nuclei and whole cells in bright field microscopy images. `napari-cellseg` uses
[`cellseg`](https://github.com/CSDGroup/cell_segmentation) for segmentation. Please cite
[this paper](#citation) if you are using this plugin in your research.

![Screenshot](https://github.com/CSDGroup/napari-cellseg/raw/main/images/napari-cellseg_screenshot.png)

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Contents
  - [Installation](#installation)
    - [Command line](#command-line)
    - [One-click](#one-click)
  - [Data](#data)
  - [Documentation](#documentation)
  - [Image annotation tools](#image-annotation-tools)
  - [Citation](#citation)
  - [Contributing](#contributing)
  - [License](#license)
  - [Issues](#issues)

## Installation
There are two ways to install `napari-cellseg`: First, you can install `napari-cellseg` from command line. Second, you
have `napari` already installed as a graphical user interface (GUI) and install `napari-cellseg` from the GUI menu.

We recommend the [command line](#command-line) installation as it provides fine-grained control of the
installation to prevent conflicts with existing napari plugins. Use the [one-click](#one-click) installation if
you do not want to concern yourself with virtual environments or the command line. Just be aware that using the
[one-click](#one-click) installation may introduce conflicts with already installed plugins or new plugin installations
may disrupt this plugin.

`napari-cellseg` was tested with
````bash
OS = macOS 12.6.3/ubuntu 22.10/windows 10
python = 3.8.6
torch = 1.10.2
torchvision = 0.11.3
pytorch-lightning = 1.5.9
```

### Command line
Installation requires a command line application (e.g. `Terminal`) with [git] and [python] installed. If you do not
have python installed already, we recommend installing it using the
[Anaconda distribution](https://www.anaconda.com/products/distribution). If you operate on `Windows` we recommend using
[`Ubuntu on Windows`](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview)
as command line application. Alternatively, you can install
[`Anaconda`](https://docs.anaconda.com/anaconda/user-guide/getting-started/) and use `Anaconda Powershell Prompt`.
An introductory tutorial on how to use `git` and GitHub can be found
[here](https://www.w3schools.com/git/default.asp?remote=github).

1) (Optional) If you already [installed napari](https://napari.org/stable/#installation) in a
[virtual environment](https://realpython.com/python-virtual-environments-a-primer/) you can skip this step.
However, you may want to install `napari-cellseg` in a fresh environment to avoid conflicts with existing
plugins. Create a new virtual environment for `napari`. [Here](https://testdriven.io/blog/python-environments/) is a
list of different python virtual environment tools. Open your command line application and create a (e.g. `conda`)
virtual environment

    ```bash
    conda create -n napari python=3.8
    ```

2) Activate your virtual environment that has `napari` installed or you want to install `napari` to

    ```bash
    conda activate napari
    ```

3) (Optional) Skip this step if you have `napari` already installed. Install `napari`

    ```bash
    pip install "napari[all]"
    ```

3) (Optional) If you use `Anaconda Powershell Prompt`, install `git` through `conda`

    ```bash
    conda install -c anaconda git
    ```

4) Install `napari-cellseg`

    1) with [pip] from [PyPI]

      ```bash
      pip install napari-cellseg
      ```
    2) with [pip] from GitHub (= latest development version)

      ```bash
      pip install git+https://github.com/CSDGroup/napari-cellseg.git
      ```

With step 4) completed you have successfully installed `napari-cellseg`. You can proceed with the
[documentation](#documentation) on how to use `napari-cellseg`. *NOTE*, that when opening the plugin for the
first time, the remaining dependencies (`torch, torchvision, pytorch-lightning`) will be automatically installed
via [light-the-torch](https://github.com/pmeier/light-the-torch). If you prefer to manually install the remaining
dependencies (i.e. prevent potential interference with your virtual environment), proceed with step 5).

5) (Optional) `GPUs` greatly speed up training and inference of U-Net and are available for `torch` (`v1.10.2`) for
`Windows` and `Linux`. Check if your `GPU(s)` are CUDA compatible
([`Windows`](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/#verify-you-have-a-cuda-capable-gpu),
 [`Linux`](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#verify-you-have-a-cuda-capable-gpu)) and
 update their drivers if necessary.

6) [Install `torch`/`torchvision`](https://pytorch.org/get-started/previous-versions/) compatible with your system.
`cell_segmentation` was tested with `torch` version `1.10.2`, `torchvision` version `0.11.3`, and `cuda` version
`11.3.1`. Depending on your OS, your `CPU` or `GPU` (and `CUDA` version) the installation may change

```bash
# Windows/Linux CPU
pip install torch==1.10.2+cpu torchvision==0.11.3+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html

# Windows/Linux GPU (CUDA 11.3.X)
pip install torch==1.10.2+cu113 torchvision==0.11.3+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

# macOS CPU
pip install torch==1.10.2 torchvision==0.11.3

```

7) [Install `pytorch-lightning`](https://www.pytorchlightning.ai). `cell_segmentation` was tested with version `1.5.9`.

```bash
# note the installation of v1.5.9 does not use pip install lightning
pip install pytorch-lightning==1.5.9
```

### One-click
Using the one-click installation of `napari-cellseg` is as easy as opening `napari`, selecting
`Plugins>Install/Uninstall Plugins...` and searching for `napari-cellseg` in the search bar. Select `install` and
restart `napari` for `napari-cellseg` to appear in the list of installed plugins in the `Plugins` menu. Please
recall that using

## Data
`napari-cellseg` is currently intended for single-class semantic segmentation. Input images are expected to be 8-bit or
16-bit greyscale images. Segmentation masks are expected to decode background as 0 intensity and all intensities
>0 are converted to a single intensity value (255). Consequently, different instances of a class (instance
segmentation) or multi-class segmentations are handled as single-class segmentations. Have a look at
[this notebook](https://github.com/CSDGroup/cell_segmentation/blob/main/notebooks/data_example.ipynb)
for a data example.

## Documentation

## Image annotation tools
Available tools to annotate segmentations include:

  - [napari](https://napari.org/stable/)
  - [Labkit](https://imagej.net/plugins/labkit/) for [Fiji](https://imagej.net/software/fiji/downloads)
  - [QuPath](https://qupath.github.io)
  - [ilastik](https://www.ilastik.org)

## Citation
t.b.d.

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-cellseg" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/CSDGroup/napari-cellseg/issues

[git]: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
[python]: https://www.python.org
