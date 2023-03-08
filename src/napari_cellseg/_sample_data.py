"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/stable/plugins/guides.html?#sample-data

Replace code below according to your needs.
"""
from __future__ import annotations

import os

import pooch
from skimage import io


def make_sample_data():
    """Generates an image"""
    # Return list of tuples
    # [(data1, add_image_kwargs1), (data2, add_image_kwargs2)]
    # Check the documentation for more information about the
    # add_image_kwargs
    # https://napari.org/stable/api/napari.Viewer.html#napari.Viewer.add_image

    # Fetch image
    # TODO: change location of image
    THATCHER = pooch.create(
        path=pooch.os_cache("napari_cellseg"),
        base_url="https://polybox.ethz.ch/remote.php/webdav/unet_models/",
        registry={
            "sample1.png": (
                "6b533f7c1e2bb23c08fe17b91a8a4beff1bf2cc5eeec"
                "15465bc7f0e5795cb7c9"
            ),
        },
    )
    polybox_acc = os.environ.get("POLYBOX_ACC")
    polybox_pw = os.environ.get("POLYBOX_PW")
    download_auth = pooch.HTTPDownloader(auth=(polybox_acc, polybox_pw))

    # update image
    path_img = THATCHER.fetch("sample1.png", downloader=download_auth)
    img = io.imread(path_img)

    return [(img, {"name": "sample1"})]
