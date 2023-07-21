import requests

def get_total_cost(api_url):
    total_cost = 0
    while api_url:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            results = data['results']

            for result in results:
                price = result.get('price', None)
                if price is not None and isinstance(price, str):
                    try:
                        total_cost += float(price)
                    except ValueError:
                        print(f"Invalid price format: {price}")

            # Check for next page
            if 'next' in data and data['next']:
                api_url = data['next']
            else:
                api_url = None
        else:
            print(f"Failed to fetch data: {response.status_code} - {response.text}")
            break

    return total_cost

if __name__ == "__main__":
    user = "TheJ" #change me
    api_url = f"https://www.muckrock.com/api_v1/foia/?user={user}&title=&status=done&embargo=unknown&jurisdiction=&agency=&projects=&tags=&has_datetime_submitted=unknown&has_datetime_done=true&ordering="

    total_cost = get_total_cost(api_url)
    print(f"Total cost spent on FOIA requests for user {user}: ${total_cost:.2f}")
