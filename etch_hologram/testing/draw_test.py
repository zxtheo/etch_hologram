import sys
from unittest import mock
sys.path.insert(0, 'G:\My Drive\\random\\etch_hologram\\etch_hologram\\etch_hologram\\app')

from etch_hologram.app.draw import Draw

# def test_draw_point():
#     """
#     This function tests the `Draw` class by mocking a canvas and a point, and then calling the `draw` method of the `Draw` class with the point. It then asserts that the `delete` method of the canvas was called once with the argument "all", and that the `create_oval` method of the canvas was called once with the arguments 50, 50, 10, and fill="red".
#     """
#     # Happy path test
#     from draw import Draw
#     canvas_mock = mock.Mock()
#     draw = Draw(canvas_mock)
#     point = mock.Mock(x=50, y=50)
#     draw.draw(point)
#     canvas_mock.delete.assert_called_once_with("all")
#     canvas_mock.create_oval.assert_called_once_with(50, 50, 10, fill="red")
