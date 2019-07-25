"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys


import numpy as np

@pytest.fixture()
def water_molecule():
	name = "water"
	symbols = ["H", "H", "O"]
	coordinates = np.array([[2,0,0], [0,0,0], [-2,0,0]])

	water = geometry_analysis.Molecule(name,symbols,coordinates)

	return water

def test_create_failuture():
	name = 25
	symbols = ["H", "H", "O"]
	coordinates = np.zeros([3, 3])

	with pytest.raises(TypeError):
		water = geometry_analysis.Molecule(name,symbols,coordinates)


def test_molecule_set_coordinates(water_molecule):
	"""test that bond list, rebuild when we reset document"""

	num_bond = len(water_molecule.bonds)

	assert num_bond == 2

	new_coordinates = np.array([[5, 0, 0], [0,0,0,], [-2,0,0]])
	water_molecule.coordinates = new_coordinates

	new_bond = len(water_molecule.bonds)

	assert new_bond == 1

	assert np.array_equal(new_coordinates,water_molecule.coordinates)



def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules 

def test_calculate_distance():
	""" test calculate distances """
	r1 = np.array([0, 0, -1])
	r2 = np.array([0, 1, 0])

	expected_distance = np.sqrt(2.)

	calculated_distance = geometry_analysis.measure.calculate_distance(r1, r2)

	assert expected_distance == calculated_distance

def test_calculate_angle():
	""" test calculate angle of 90 degrees """

	a1 = np.array([1, 0, 0])
	a2 = np.array([0, 0, 0])
	a3 = np.array([0, 1, 0])

	expected_angle = 90 

	calculated_anlge = geometry_analysis.measure.calculate_angle(a1, a2, a3, degrees = True)
	assert calculated_anlge == expected_angle

def test_calculate_angle_60():
	""" test calculate angle of 60 degrees """

	a1 = np.array([0, 0, -1])
	a2 = np.array([0, 1, 0])
	a3 = np.array([1, 0, 0])

	expected_angle = 60 

	calculated_anlge = geometry_analysis.measure.calculate_angle(a1, a2, a3, degrees = True)
	assert np.isclose(calculated_anlge, expected_angle)

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
	(np.array([1, 0, 0]), np.array([0, 0, 0]), np.array([0, 1, 0]), 90),
	(np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
	])

def test_calculate_angle(p1,p2,p3,expected_angle):
	calculated_angle = geometry_analysis.calculate_angle(p1,p2,p3, degrees = True)
	assert np.isclose(expected_angle, calculated_angle)



