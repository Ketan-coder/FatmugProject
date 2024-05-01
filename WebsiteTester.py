import requests

# List of URLs to test
urls = [
    "http://127.0.0.1:5050/api/vendors/",
    "http://127.0.0.1:5050/api/purchase_orders/",

]

def test_websites(urls) -> None:
    for url in urls:
        try:
            response = requests.get(url)

            # Check for HTTP errors
            response.raise_for_status()

            # Check for specific content or conditions
            if "Error" in response.text:
                print(f"Error found on {url}")
            else:
                print(f"No errors found on {url}")

        except requests.exceptions.RequestException as e:
            # Handle request-related errors
            print(f"Request error on {url}: {e}")
    print("Done!")

if __name__ == "__main__":
    test_websites(urls)
