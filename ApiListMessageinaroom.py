import requests
import json

def get_access_token():
    choice = input("Do you want to use the hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
        access_token = "Bearer " + access_token
    else:
        access_token = "Bearer MTNkZDYzZWEtYzBiMC00NmEzLWE2MzEtYTcyMjYyMDg5NGZmMjVjOWFjOTktN2E5_P0A1_d8874c41-f836-471b-bf45-f4bf285408d0"
    return access_token

def get_rooms(access_token):
    headers = {"Authorization": access_token}
    response = requests.get("https://webexapis.com/v1/rooms", headers=headers)
    response.raise_for_status()
    return response.json()

def find_room(rooms):
    while True:
        room_name_to_search = input("Which room are you looking for? (Can use partial name of the room): ").strip()
        for room in rooms["items"]:
            if room["title"].lower().find(room_name_to_search.lower()) != -1:
                print(f"Found room: {room['title']}")
                return room["id"]
        print(f"Sorry, no rooms found with '{room_name_to_search}' in the name. Please try again.")

def get_messages(access_token, room_id):
    headers = {"Authorization": access_token}
    params = {"roomId": room_id, "max": 50}
    response = requests.get("https://webexapis.com/v1/messages", headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def list_messages(messages):
    if not messages["items"]:
        print("No messages found in this room.")
        return
    
    for message in messages["items"]:
        print(f"Message: {message['text']}")
        print(f"From (email): {message['personEmail']}")
        print(f"Created: {message['created']}\n")

def main():
    access_token = get_access_token()
    rooms = get_rooms(access_token)
    print("List of rooms:")
    for room in rooms["items"]:
        print(room["title"])
    
    room_id = find_room(rooms)
    messages = get_messages(access_token, room_id)
    list_messages(messages)

if __name__ == "__main__":
    main()
