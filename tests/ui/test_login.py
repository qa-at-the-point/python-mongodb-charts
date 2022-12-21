import pytest
from pylenium.driver import Pylenium


@pytest.fixture(scope="function")
def login_with(py):
    def _login(username: str, password: str = "secret_sauce"):
        py.visit("https://saucedemo.com")
        py.get("#user-name").type(username)
        py.get("#password").type(password)
        py.get("#login-button").click()

    return _login


def test_login_with_standard_user(py: Pylenium, login_with):
    login_with("standard_user")
    assert py.get(".title").should().have_text("PRODUCTS")


def test_login_with_locked_out_user(py: Pylenium, login_with):
    login_with("locked_out_user")
    assert py.get("[data-test=error]").should().contain_text("this user has been locked out")


def test_login_with_problem_user(py: Pylenium, login_with):
    """This specific scenario is better as another type of test, like Visual, but we expect this test to fail"""
    expected_images = [  # maybe we grab this list of expected products and images from our API or DB
        "/static/media/bolt-shirt-1200x1500.c0dae290.jpg",
        "/static/media/bike-light-1200x1500.a0c9caae.jpg",
        "/static/media/bolt-shirt-1200x1500.c0dae290.jpg",
        "/static/media/sauce-pullover-1200x1500.439fc934.jpg",
        "/static/media/red-onesie-1200x1500.1b15e1fa.jpg",
        "/static/media/red-tatt-1200x1500.e32b4ef9.jpg",
    ]
    login_with("problem_user")
    for i, product in enumerate(py.find("img.inventory_item_img")):
        assert "Sauce Labs" in product.get_attribute("alt")
        assert product.get_attribute("src") == expected_images[i]


def test_login_with_performance_glitch_user(py: Pylenium, login_with):
    """Because of the undeterministic performance, this test may sometimes pass and sometimes fail"""
    login_with("performance_glitch_user")
    assert py.get(".title").should().have_text("PRODUCTS"), "Took too long to login and render Products Page"
