import requests
import json
from datetime import datetime, timedelta

def get_access_token():
    choice = input("Do you want to use the hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
        access_token = "Bearer " + access_token
    else:
        access_token = "Bearer MTNkZDYzZWEtYzBiMC00NmEzLWE2MzEtYTcyMjYyMDg5NGZmMjVjOWFjOTktN2E5_P0A1_d8874c41-f836-471b-bf45-f4bf285408d0"
    return access_token

def get_rooms(access_token):
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    
    response = requests.get("https://webexapis.com/v1/rooms", headers=headers)
    
    if response.status_code == 200:
        rooms = response.json().get('items', [])
        if not rooms:
            print("No rooms found.")
            return None
        for i, room in enumerate(rooms):
            print(f"{i + 1}: {room['title']} (ID: {room['id']})")
        room_choice = int(input("Select a room by number: ")) - 1
        return rooms[room_choice]['id']
    else:
        print("Failed to retrieve rooms.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

def create_meeting(access_token, title, start_time, duration, room_id):
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    # Calculate end time based on duration
    start_datetime = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%SZ")
    end_datetime = start_datetime + timedelta(minutes=duration)
    
    data = {
        "title": title,
        "start": start_time,  # Format: "YYYY-MM-DDTHH:MM:SSZ"
        "end": end_datetime.strftime("%Y-%m-%dT%H:%M:%SZ"),  # Format end time correctly
        "enabledAutoRecordMeeting": False,  # Change as needed
        "agenda": "Discuss project updates",  # Optional agenda
        "roomId": room_id  # Add room ID here
    }
    
    response = requests.post("https://webexapis.com/v1/meetings", headers=headers, json=data)
    
    if response.status_code == 200:
        print("Meeting created successfully.")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Failed to create meeting.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

def main():
    access_token = get_access_token()
    
    # Get Room ID
    room_id = get_rooms(access_token)
    if room_id is None:
        return  # Exit if no room is found

    title = input("Enter the meeting title: ").strip()
    start_time = input("Enter the meeting start time (YYYY-MM-DDTHH:MM:SSZ): ").strip()
    duration = int(input("Enter the duration of the meeting in minutes: ").strip())
    
    create_meeting(access_token, title, start_time, duration, room_id)

if __name__ == "__main__":
    main()
