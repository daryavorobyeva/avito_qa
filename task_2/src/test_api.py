import requests
from conftest import default_payload

class TestGetById:

    def test_1_1_valid_id(self, item_url, valid_id):
        response = requests.get(f'{item_url}/{valid_id}')
        assert response.status_code == 200

        response_json = response.json()
        assert any(item['id'] == valid_id for item in response_json)

    def test_1_2_invalid_id(self, item_url, invalid_id):
        response = requests.get(f'{item_url}/{invalid_id}')
        assert response.status_code == 404

class TestGetBySellerId:

    def test_2_1_valid_seller_id(self, seller_url, existing_seller_id):
        response = requests.get(seller_url.format(seller_id=existing_seller_id))
        assert response.status_code == 200

        response_json = response.json()
        for item in response_json:
            assert item['sellerId'] == int(existing_seller_id)

    def test_2_2_invalid_seller_id(self, seller_url, without_items_seller_id):
        response = requests.get(seller_url.format(seller_id=without_items_seller_id))
        assert response.status_code == 200

        response_json = response.json()
        assert response_json == []

class TestPostSaveItem:

    def test_3_1_existing_seller_id(self, item_url, default_payload):
        response = requests.post(item_url, json=default_payload)
        assert response.status_code == 200

    def test_3_2_non_existent_positive_seller_id(self, item_url, default_payload,
                                                 non_existent_positive_seller_id):
        payload = default_payload.copy()
        payload['sellerId']=non_existent_positive_seller_id

        response = requests.post(item_url, json=payload)
        assert response.status_code == 200

    def test_3_3_non_existent_negative_seller_id(self, item_url, default_payload,
                                                 non_existent_negative_seller_id):

        payload = default_payload.copy()
        payload['sellerId'] = non_existent_negative_seller_id

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json

    def test_3_4_item_with_empty_name(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['name'] = ""

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json

    def test_3_5_item_with_negative_price(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['price'] = -85566

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json


    def test_3_6_item_with_negative_contacts(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['contacts'] = -32

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json

    def test_3_7_item_with_negative_like(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['like'] = -35

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json

    def test_3_8_item_with_negative_view_count(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['viewCount'] = -14

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json

    def test_3_9_item_with_incorrect_price_type(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['price'] = "abc"

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json

    def test_3_10_item_with_incorrect_contacts_type(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['contacts'] = "abc"

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json

    def test_3_11_item_with_incorrect_like_type(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['like'] = "abc"

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json

    def test_3_12_item_with_incorrect_view_count_type(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['viewCount'] = "abc"

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json

    def test_3_13_item_with_incorrect_seller_id_type(self, item_url, default_payload):
        payload = default_payload.copy()
        payload['sellerId'] = "abc"

        response = requests.post(item_url, json=payload)
        assert response.status_code == 400

        response_json = response.json()
        assert "error" in response_json or "message" in response_json
