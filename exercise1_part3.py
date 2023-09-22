import requests

def http_request(is_admin=1, user_agent=None):
    url = "https://httpbin.org/anything"
    headers = {"User-Agent": user_agent} if user_agent else {}

    payload = {"isadmin": is_admin}

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()  # Raise an exception for any HTTP error
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
response_body = http_request(is_admin=1)
print("Response body with the default user-agent:")
print(response_body)

response_body_with_custom_user_agent = http_request(is_admin=1, user_agent="MyCustomUserAgent")
print("\nResponse body with a custom user-agent:")
print(response_body_with_custom_user_agent)
