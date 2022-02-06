## @file test_driver.py
# @author
# @brief
# @date
# @details

from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene

from pytest import *

g = 9.81  # accel due to gravity (m/s^2)
m = 1  # mass (kg)


def Fx(t):
    return 5 if t < 5 else 0


def Fy(t):
    return -g * m if t < 3 else g * m


class TestCircleT:

    def setup_method(self, method):
        self.test_circle1 = CircleT(1.0, 10.0, 0.5, 1.0)

    def teardown_method(self, method):
        self.test_circle1 = None

    def test_cm_x(self):
        assert self.test_circle1.cm_x() == 1.0

    def test_cm_y(self):
        assert self.test_circle1.cm_y() == 10.0

    def test_mass(self):
        assert self.test_circle1.mass() == 1.0

    def test_m_inert(self):
        assert approx(self.test_circle1.m_inert()) == approx(0.125)


class TestTriangleT:

    def setup_method(self, method):
        self.test_triangle1 = TriangleT(1.0, -10.0, 5, 17.5)

    def teardown_method(self, method):
        self.test_triangle1 = None

    def test_cm_x(self):
        assert self.test_triangle1.cm_x() == 1.0

    def test_cm_y(self):
        assert self.test_triangle1.cm_y() == -10.0

    def test_mass(self):
        assert self.test_triangle1.mass() == 17.5

    def test_m_inert(self):
        assert approx(self.test_triangle1.m_inert()) == approx(36.4583333)


class TestBodyT:

    def setup_method(self, method):
        self.test_body1 = BodyT([1, -1, -1, 1], [1, 1, -1, -1], [10, 10, 10, 10])

    def teardown_method(self, method):
        self.test_body1 = None

    def test_cm_x(self):
        assert self.test_body1.cm_x() == 0.0

    def test_cm_y(self):
        assert self.test_body1.cm_y() == 0.0

    def test_mass(self):
        assert self.test_body1.mass() == 40

    def test_m_inert(self):
        assert approx(self.test_body1.m_inert()) == approx(80.0)


class TestScene:

    def setup_method(self, method):
        self.test_cricle = CircleT(1, 10.0, 0.5, 1)
        self.test_triangle = TriangleT(1.0, -2.0, 5.0, 10.0)
        self.test_body = BodyT([1, -1, -1, 1], [1, 1, -1, -1], [10, 10, 10, 10])
        self.test_scene1 = Scene(self.test_cricle, Fx, Fy, 0, 0)
        self.test_scene2 = Scene(self.test_triangle, Fx, Fy, 0, 0)
        self.test_scene3 = Scene(self.test_body, Fx, Fy, 0, 0)

    def teardown_method(self, method):
        self.test_scene1 = None
        self.test_scene2 = None
        self.test_scene3 = None

    def test_get_shape_circle(self):
        assert type(self.test_scene1.get_shape()) == CircleT

    def test_get_shape_triangle(self):
        assert type(self.test_scene2.get_shape()) == TriangleT

    def test_get_shape_body(self):
        assert type(self.test_scene3.get_shape()) == BodyT

    def test_get_init_velo1(self):
        assert self.test_scene1.get_init_velo() == (0, 0)

    def test_get_init_vel2(self):
        assert self.test_scene2.get_init_velo() == (0, 0)

    def test_get_init_velo_not(self):
        assert not self.test_scene1.get_init_velo() == (1, 0)

    def test_set_shape(self):
        self.test_scene1.set_shape(TriangleT)
        assert self.test_scene1.get_shape() == TriangleT

    def test_set_shape_not(self):
        self.test_scene2.set_shape(CircleT)
        assert not self.test_scene1.get_shape() == TriangleT

    def test_set_init_vel1(self):
        self.test_scene1.set_init_velo(1, 1)
        assert self.test_scene1.get_init_velo() == (1, 1)

    def test_set_init_vel_not(self):
        self.test_scene2.set_init_velo(1, 1)
        assert self.test_scene1.get_init_velo() == (0, 0)
