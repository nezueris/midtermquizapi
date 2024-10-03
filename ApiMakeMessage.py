import requests

def get_access_token():
    choice = input("Do you want to use the hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
        access_token = "Bearer " + access_token
    else:
        access_token = "Bearer MTNkZDYzZWEtYzBiMC00NmEzLWE2MzEtYTcyMjYyMDg5NGZmMjVjOWFjOTktN2E5_P0A1_d8874c41-f836-471b-bf45-f4bf285408d0"
    return access_token

def create_message(access_token, room_id, text):
    headers = {"Authorization": access_token, "Content-Type": "application/json"}
    data = {"roomId": room_id, "text": text}
    response = requests.post("https://webexapis.com/v1/messages", headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def main():
    access_token = get_access_token()
    room_id = input("Enter the ID of the room: ").strip()
    text = input("Enter the message you want to send: ").strip()
    create_message(access_token, room_id, text)
    print("Message sent successfully.")

if __name__ == "__main__":
    main()
