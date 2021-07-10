# INTRO: There are many reasons to create automated tests. But one reason is
# to ensure your API doesn't deviate from expected behaviour even after
# making changes to your code. This is especially helpful as the codebase
# gets bigger and more people are working on the same codebase.


# 1) Import the TestClient class and our FastAPI app
from fastapi.testclient import TestClient
from grocery_api.main import app


# 2) Create a TestClient instance, passing our FastAPI app
client = TestClient(app)


# PyTest Note: Test functions should start with "test" for PyTest to
# recognize it.
def test_home_should_respond_with_hello_world_message():
    # 3) Use the TestClient instance, client, to simulate making a request
    # to our API. In this case, it is making a `GET` request to the "root"
    # path: `/`. We then save the response to a variable, `response`.
    response = client.get("/")
    # 4) We expect that the response body is a dictionary containing the key
    # "message" and the value "Hello World!" (see main.py).
    # To add a test for this behaviour, we need to get the response body
    # by calling the json() method and then comparing it with the
    # dictionary we expect our response  body to be.
    assert response.json() == {"message": "Hello World!"}

# HOW-TO #5: Test that our user endpoint only returns non-sensitive data.
# Our test strategy for this would be to check that the response
# body only returns certain keys.
def test_get_user_endpoint_should_only_return_non_sensitive_info():
    # 1) Use the `client` variable to simulate a GET request to our API.
    # The User ID is found in the cheatsheet.
    response = client.get("/users/c6fce069-4748-499d-a85d-bf310bfd534b")
    # 2) Save the response body to a new variable for readability's sake.
    response_body = response.json()
    # 3) As in the previous test, we expect the response body for this endpoint
    # to be a dictionary (see main.py). We get the keys of this dictionary by
    # calling the keys() method. Since we will be comparing it to a list, we
    # have to cast the dictionary keys to a list. Let's save it in a variable for
    # readability's sake.
    actual_keys = list(response_body.keys())
    # 4) We then compare this list of keys to what we _expect_ the keys to be.
    assert actual_keys == ["id", "email", "username"]

# To run this test in the terminal:
#
# 1) Ensure your grocery_api virtual environment is activated.
#   - If you see "(grocery_api)" in the beginning of your prompt, then the
#   environment is already activated.
#   - Otherwise, run `source .venv/bin/activate` within the grocery_api directory
#
# 2) Run `pytest -k test_get_user_endpoint_should_only_return_non_sensitive_info`
