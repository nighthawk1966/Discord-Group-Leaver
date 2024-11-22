import requests

user_token = "TOKEN" # TOKEN YAZ BURAYA

def get_headers(token):
    return {
        "Authorization": token,
        "Content-Type": "application/json"
    }

def fetch_group_dms(token):
    url = "https://discord.com/api/v9/users/@me/channels"
    headers = get_headers(token)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return [channel for channel in response.json() if channel['type'] == 3]
    else:
        print(f"Failed to fetch channels. Status code: {response.status_code}, Response: {response.text}")
        return []

def leave_group_dm(token, channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}"
    headers = get_headers(token)
    response = requests.delete(url, headers=headers)

    if response.status_code == 200 or response.status_code == 204:
        print(f"Successfully left group DM: {channel_id}")
    else:
        print(f"Failed to leave group DM: {channel_id}. Status code: {response.status_code}, Response: {response.text}")

def quit_all_group_dms(token):
    group_dms = fetch_group_dms(token)
    if not group_dms:
        print("No group DMs found.")
        return

    for dm in group_dms:
        leave_group_dm(token, dm['id'])

if __name__ == "__main__":
    quit_all_group_dms(user_token)
