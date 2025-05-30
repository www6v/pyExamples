import requests
import json

def send_post_request(url: str, json_body: dict, headers: dict = None, params: dict = None) -> requests.Response:
    """
    Send an HTTP POST request with a JSON body, custom headers, and query parameters.

    Args:
        url (str): The URL to send the request to.
        json_body (dict): The JSON body of the request.
        headers (dict, optional): Custom HTTP headers. Defaults to None.
        params (dict, optional): Query parameters. Defaults to None.

    Returns:
        requests.Response: The response from the server.
    """
    try:
        response = requests.post(
            url,
            json=json_body,  # Automatically sets Content-Type to application/json
            headers=headers,
            params=params,
        )
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Example JSON body
    json_body = {
        "key1": "value1",
        "key2": "value2",
    }

    # Example headers
    headers = {
        "Authorization": "Bearer your_token_here",
        "Custom-Header": "CustomValue",
    }

    # Example query parameters
    params = {
        "param1": "value1",
        "param2": "value2",
    }

    # URL to send the request to
    url = "https://example.com/api/endpoint"

    # Send the request
    response = send_post_request(url, json_body, headers, params)
    print(f"Response status code: {response.status_code}")
    print(f"Response body: {response.json()}")
