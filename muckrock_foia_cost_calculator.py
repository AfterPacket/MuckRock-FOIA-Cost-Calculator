import requests

# Function to calculate the total cost spent on FOIA requests
def get_total_cost(api_url):
    total_cost = 0

    while api_url:
        response = requests.get(api_url)

        # Check if the API call is successful
        if response.status_code == 200:
            data = response.json()
            results = data['results']

            # Process each FOIA request and add the price to the total cost
            for result in results:
                price = result.get('price', None)
                if price is not None and isinstance(price, (int, float)):
                    total_cost += price

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
    user = "YourUsernameHere"  # Change this to your MuckRock username
    api_url = f"https://www.muckrock.com/api_v1/foia/?user={user}&title=&status=done&embargo=unknown&jurisdiction=&agency=&projects=&tags=&has_datetime_submitted=unknown&has_datetime_done=true&ordering="

    total_cost = get_total_cost(api_url)
    print(f"Total cost spent on FOIA requests for user {user} on MuckRock: ${total_cost:.2f}")

# License: GNU General Public License (GPL) version 3.0
# This script is licensed under the GNU General Public License (GPL) version 3.0.
# For more details, see the LICENSE file.


# Special thanks to AfterPacket for their support and resources in developing this script.
# Check out AfterPacket.io 
# Website: https://afterpacket.io
