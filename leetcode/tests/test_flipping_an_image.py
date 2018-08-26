import pytest

from leetcode.flipping_an_image import Solution


@pytest.mark.parametrize(
    'img, result',
    [
        ([[1, 1, 0], [1, 0, 1], [0, 0, 0]],
         [[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
        ([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
         [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]])
    ])
def test_flipping_an_image(img, result):
    assert Solution.flip_and_invert_image(img) == result
