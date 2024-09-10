import pytest

# Базовый URL для всех тестов
@pytest.fixture
def base_url():
    return "https://qa-internship.avito.com/api/1"

# Для методов, где меняется только id
@pytest.fixture
def item_url(base_url):
    return f"{base_url}/item"

@pytest.fixture
def valid_id():
    return "07d2b4fc-4e4c-4427-bbb0-74a67fa5ce38"

@pytest.fixture
def invalid_id():
    return "07d2b4fc-4e4c-4427-bbb0-74a67fa5ce13"

# Для методов, где меняется sellerId
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
def non_existent_negative_seller_id():
    return "-5"
