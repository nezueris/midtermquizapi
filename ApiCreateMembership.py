import requests

def get_access_token():
    choice = input("Do you want to use the hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
        access_token = "Bearer " + access_token
    else:
        access_token = "Bearer MTNkZDYzZWEtYzBiMC00NmEzLWE2MzEtYTcyMjYyMDg5NGZmMjVjOWFjOTktN2E5_P0A1_d8874c41-f836-471b-bf45-f4bf285408d0"
    return access_token

def create_membership(access_token, room_id, person_email):
    headers = {"Authorization": access_token, "Content-Type": "application/json"}
    data = {"roomId": room_id, "personEmail": person_email}
    response = requests.post("https://webexapis.com/v1/memberships", headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def main():
    access_token = get_access_token()
    room_id = input("Enter the ID of the room: ").strip()
    
    while True:
        person_email = input("Enter the email of the person (type 'exit' to stop): ").strip()
        if person_email.lower() == "exit":
            break
        create_membership(access_token, room_id, person_email)
        print("Membership created successfully.")

if __name__ == "__main__":
    main()
