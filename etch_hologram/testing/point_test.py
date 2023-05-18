import sys
import pytest

# adding Folder_2/subfolder to the system path
sys.path.insert(0, 'G:\My Drive\\random\\etch_hologram\\etch_hologram\\etch_hologram\\app')

def test_create_point_with_valid_values():
    from point import Point
    point = Point(1, 2, 3)
    assert point.x == 1
    assert point.y == 2
    assert point.z == 3



def test_create_point_with_zero_values():
    from point import Point
    point = Point(0, 0, 0)
    assert point.x == 0
    assert point.y == 0
    assert point.z == 0

def test_distance_with_same_point_object():
    from point import Point
    point = Point(1.0, 2.0, 3.0)
    assert point.distance(point) == 0.0

def test_distance_with_non_point_object():
    from point import Point
    point = Point(1.0, 2.0, 3.0)
    with pytest.raises(AttributeError):
        point.distance("not a Point object")

def test_distance_with_same_xyz_values():
    from point import Point
    point1 = Point(1.0, 1.0, 1.0)
    point2 = Point(1.0, 1.0, 1.0)
    assert point1.distance(point2) == 0.0