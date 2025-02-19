'''
API
    Application Programming Interface, or API, is a set of protocols, routines, and tools for building software applications

key concepts related to APIs

    1. Endpoint:
            Definition
                An endpoint is a specific URL where an API receives requests for a particular resource or service.
                It is the point of entry in a communication channel that the API exposes to the outside world.
            Structure:
                Typically, an endpoint is structured in a hierarchical manner, reflecting the resource's path within the API's architecture.
                For example, https://api.example.com/v1/users might be an endpoint to access user data, where v1 denotes the API version, and users specifies the resource.
            Operations:
                Endpoints are associated with specific operations that can be performed on the resources.
                These operations are usually tied to HTTP methods
            Parameters:
                Endpoints can accept parameters that modify the request or specify which data to retrieve.
                Parameters can be included in the URL path, as query strings, or within the request body.

                Path Parameters: Embedded directly within the endpoint URL, e.g., /users/{userId} where {userId} is a variable.

                Query Parameters: Appended to the URL after a question mark, e.g., /users?role=admin.

                Body Parameters: Sent within the request body, typically for POST or PUT requests.
            Response:
                When an endpoint is called, it returns a response to the client. This response usually includes:

                Status Code: Indicates the result of the request (e.g., 200 OK, 404 Not Found).

                Headers: Provide metadata about the response.

                Body: Contains the actual data requested or a message regarding the operation's outcome

    2. Request:
            This is the act of asking for data or sending data to be processed by the API.
            A request typically includes a URL, the HTTP method (like GET, POST, PUT, DELETE), headers, and sometimes a body with data.

    3. Response:
            After a request is made, the API sends back a response.
            This response usually includes a status code (like 200 for success or 404 for not found), headers, and often a body with the requested data or a message.

            Status Code: This is a three-digit number that indicates the outcome of the HTTP request. Status codes are grouped into five classes:

            1xx (Informational): The request was received, and the process is continuing.

            2xx (Success): The request was successfully received, understood, and accepted.

            3xx (Redirection): Further action needs to be taken to complete the request.

            4xx (Client Error): The request contains bad syntax or cannot be fulfilled.

            5xx (Server Error): The server failed to fulfill a valid request

            B. Headers: Response headers provide metadata about the response. This can include information such as the content type of the body, caching policies, and CORS (Cross-Origin Resource Sharing) policies. Common headers include:

                    Content-Type: Indicates the media type of the resource (e.g., application/json).

                    Cache-Control: Directives for caching mechanisms in both requests and responses.

                    Set-Cookie: Used to send cookies from the server to the user agent.
            C. Body: The body contains the actual data that the client requested.
                    The format of the body can vary, but common formats include JSON, XML, HTML, or plain text. For example, a JSON response body might look like this:

                        {
                          "userId": 1,
                          "id": 1,
                          "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                          "body": "quia et suscipit\nsuscipit..."
                        }
            D.Error Messages: If the request was not successful, the response body might contain error messages or codes that provide more information about what went wrong.
                For example:

                            {
                              "error": {
                                "code": 404,
                                "message": "Resource not found"
                              }
                            }
            E. Response Time:
                This is the time it takes for the server to process the request and send back the response.
                It is an important performance metric for APIs.


    4. HTTP Methods:
            These are the actions that can be performed on resources. The most common methods are:

            GET: Retrieve data from the server.

            POST: Send new data to the server.

            PUT: Update existing data on the server.

            DELETE: Remove data from the server.

    5. Authentication and Authorization:
            APIs often require some form of authentication to ensure that the client has permission to access the data.
            This can be done through API keys, OAuth tokens, or other security mechanisms.
    6. Rate Limiting:
            To prevent abuse, APIs often limit the number of requests a user can make in a given time period.
            This is known as rate limiting.

    7. Documentation:
            Good APIs come with comprehensive documentation that explains how to use the API,
            including details about the endpoints, request/response formats, error codes, and examples.

    8. Versioning:
            As APIs evolve, it's important to maintain different versions so that changes don't break existing applications that rely on the API.
            Versioning can be done through the URL, headers, or other means.

'''

import requests

# Base URL of the API
BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post():
    # Endpoint to test
    endpoint = f"{BASE_URL}/posts/1"

    # Send GET request
    response = requests.get(endpoint)

    # Assert status code
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # Assert response body
    data = response.json()
    assert data["id"] == 1, f"Expected post ID 1, but got {data['id']}"
    assert data["userId"] == 1, f"Expected user ID 1, but got {data['userId']}"
    assert "title" in data, "Title not found in response"
    assert "body" in data, "Body not found in response"


def test_create_post():
    endpoint = f"{BASE_URL}/posts"

    # Payload for the POST request
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    # Send POST request
    response = requests.post(endpoint, json=payload)

    # Assert status code
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

    # Assert response body
    data = response.json()
    assert data["id"] is not None, "Post ID not found in response"
    assert data["title"] == "foo", f"Expected title 'foo', but got {data['title']}"
    assert data["body"] == "bar", f"Expected body 'bar', but got {data['body']}"

# mocking responses
import responses
import requests


@responses.activate
def test_mock_get_post():
    # Mock the API response
    mock_response = {
        "id": 1,
        "userId": 1,
        "title": "Mocked Title",
        "body": "Mocked Body"
    }
    responses.add(
        responses.GET,
        "https://jsonplaceholder.typicode.com/posts/1",
        json=mock_response,
        status=200
    )

    # Send GET request
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    # Assertions
    assert response.status_code == 200
    assert response.json() == mock_response

from http.client import responses

from packaging.version import VERSION_PATTERN

"""
Query parameters are appended to the end of the request URL, following ? and listed in key-value pairs, separated by & as follows: ?id=1&type=new
Path parameters form part of the request URL, and are referenced using placeholders preceded by : as in the following example: /customer/:id

"""


import requests
API_questions = 'https://katalon.com/resources-center/blog/web-api-testing-interview-questions'
base_url='https://reqres.in/api'

# ************************ GET Method **************************************

def test_list_users():
    path_argument='users?page=2' # two page are there currently
    response=requests.get(f'{base_url}/{path_argument}')
    code= response.status_code
    print(code,'\n')
    data=response.json()
    print(data)

def test_single_user():
    path_argument = 'users/2'
    response= requests.get(f'{base_url}/{path_argument}')
    code= response.status_code
    data=response.json()
    print('done')

def test_single_user_not_found():
    url_path ='users/23'
    response = requests.get(f'{base_url}/{url_path}')
    code = response.status_code
    data = response.json()
    print('done')

def test_list_resource():
    url_path = '/unknown'
    response = requests.get(f'{base_url}{url_path}')
    code = response.status_code
    text= response.text
    data= response.json()
    reason= response.reason
    request = response.request
    assert base_url+url_path == response.request.url,'this is not equal'
    print(10)

def test_single_resource():
    url_path ='/unknown/23'
    response= requests.get(f'{base_url}{url_path}')
    code = response.status_code
    text=response.text
    data= response.json()
    reason=response.reason
    request=response.request
    assert base_url+url_path == response.request.url, "this is not matched"
    print(10)


    # ************************** POST ********************************************

def test_create_user():
        url_path='/users'
        user_payload={
            'name':'balasljc',
            'position':'software engineer'
        }
        response = requests.post(f'{base_url}{url_path}',json=user_payload)
        code=response.status_code
        data=response.json()
        assert response.status_code == 201 ,' user is not created'
        print('done')
        # id is 995

def test_update_user_with_put_patch():
    url_path ='/users/2'
    user={
    "name": "morpheus",
    "job": "zion resident"
    }
    # response = requests.put(f'{base_url}{url_path}',json=user)
    response = requests.patch(f'{base_url}{url_path}',json=user)
    code = response.status_code
    data=response.json()
    reason=response.reason
    assert response.status_code == 200,'it is not success'
    print('done')

def test_delete_user():
    url_path='/users/2'
    response=requests.delete(f'{base_url}{url_path}')
    code = response.status_code
    assert response.status_code == 204, " this is not success"
    print('not updated')

def test_register_user_with_post():
    url_path='/register'
    register_payload={
    "email": "eve.holt@reqres.in",
    "password": "pistol"
    }
    response = requests.post(f'{base_url}{url_path}',json=register_payload)
    code = response.status_code
    data =response.json()
    assert response.status_code == 200,'it is not success'
    print('done')

def test_register_incorrect_user_with_post(): # 400 status code - bad requesst
    url_path ='/register'
    payload={
    "email": "sydney@fife"
    }
    response = requests.post(f'{base_url}{url_path}',json=payload)
    code = response.status_code
    data=response.json()
    print('done')

def test_login_user(): # 200 status code - success
    url_path='/login'
    payload = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }
    response = requests.post(f'{base_url}{url_path}',json=payload)
    code =response.status_code
    data=response.json()
    print('done')

def test_invalid_user_login(): # 400 bad request
    url_path ='/login'
    payload={
    "email": "peter@klaven"
    }
    response= requests.post(f'{base_url}{url_path}',json=payload)
    code = response.status_code
    reason=response.reason
    print('done')