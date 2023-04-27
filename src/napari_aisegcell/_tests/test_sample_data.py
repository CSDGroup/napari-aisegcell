import numpy as np

from napari_aisegcell import make_sample_data


def test_make_sample_data():
    data = make_sample_data()
    assert len(data) == 1
    assert isinstance(data, list)
    assert isinstance(data[0], tuple)
    assert isinstance(data[0][0], np.ndarray)
    assert data[0][1]['name'] == 'bf1'
    assert data[0][0].shape == (256, 256)
    assert data[0][0].dtype == 'uint8'
