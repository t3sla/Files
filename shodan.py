import sys
import shodan

API_KEY = "HSbKvP7dMWK7c7doTw5dIhI0LHEL694n"

def search_shodan(filter_type, query):
    api = shodan.Shodan(API_KEY)

    try:
        result = api.search(f"{filter_type}:{query}")
        return result['matches']
    except shodan.APIError as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    filter_type = input("Enter in your organization or domain name): ").strip().lower()

    if filter_type not in ['ssl', 'org']:
        print("invalid filter type")
        sys.exit(1)

    query = input(f"Enter value for {filter_type} filter: ").strip()
    results = search_shodan(filter_type,query)

    if not results:
        print("No result found")
        sys.exit(0)

    for result in results:
        print(f"IP: {result['ip_str']}")
        print(f"Data: {result['data']}")
        print("="*30)

if __name__ == "__main__":
    main()
