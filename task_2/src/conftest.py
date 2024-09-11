import pytest
import random

# url
@pytest.fixture
def base_url():
    return "https://qa-internship.avito.com/api/1"

@pytest.fixture
def item_url(base_url):
    return f"{base_url}/item"


# payload
@pytest.fixture
def default_payload(name="Телефон", price=85566, seller_id=3452, contacts=32, like=35, view_count=14):
    return {
        "name": name,
        "price": price,
        "sellerId": seller_id,
        "statistics": {
            "contacts": contacts,
            "like": like,
            "viewCount": view_count
        }
    }


# id
@pytest.fixture
def valid_id():
    return "07d2b4fc-4e4c-4427-bbb0-74a67fa5ce38"

@pytest.fixture
def invalid_id():
    return "07d2b4fc-4e4c-4427-bbb0-74a67fa5ce13"


# sellerId
@pytest.fixture
def seller_url(base_url):
    return f"{base_url}/{{seller_id}}/item"

@pytest.fixture
def existing_seller_id():
    return "3452"

@pytest.fixture
def without_items_seller_id():
    return "2222"

@pytest.fixture
def non_existent_positive_seller_id():
    return random.randint(111111, 999999)

@pytest.fixture
def non_existent_negative_seller_id():
    return -5


# bad cases
@pytest.fixture
def empty_name():
    return ""

@pytest.fixture
def negative_price():
    return -85566

@pytest.fixture
def negative_contacts():
    return -32

@pytest.fixture
def negative_like():
    return -35

@pytest.fixture
def negative_view_count():
    return -14

@pytest.fixture
def stroke():
    return "abc"