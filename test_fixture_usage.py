import pytest



@pytest.fixture
def user():
    return {"name": "Alice", "age": 30, "city": "New York"}


def test_user_name(user):
    
    assert user["name"] == "Alice"
    print(f"the test_user_name has passed successfully with user name: {user['name']}")

def test_user_city(user):
    
    assert user["city"] == "New York"
    print(f"the test_user_city has passed successfully with user city: {user['city']}")

def test_user_age(user):
    
    assert user["age"] == 30
    print(f"the test_user_age has passed successfully with user age: {user['age']}")