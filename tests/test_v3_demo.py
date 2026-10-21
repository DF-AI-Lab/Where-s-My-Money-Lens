"""Lite /demo on the website (21 Oct 2026): same sign-in as the main page. Fake data only."""
import pytest

from tests.v3_helpers import v3_data, v3_app, v3_client, ACME  # noqa: F401

pytest.importorskip("flask")


def test_demo_needs_sign_in(v3_app):
    assert v3_app.test_client().get("/demo").status_code in (302, 303)
    assert v3_app.test_client().get("/demo/static/look.css").status_code in (302, 303, 401)


def test_demo_signed_in(v3_client):
    assert 'data-pay="2500.00"' in v3_client.get("/demo").get_data(as_text=True)
    assert v3_client.get("/demo/static/look.css").status_code == 200
