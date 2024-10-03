from faker import Faker

def generate_fake_data(num_entries):
    fake = Faker()
    fake_data = []

    for _ in range(num_entries):
        name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        fake_data.append({
            "name": name,
            "email": email,
            "phone_number": phone_number
        })

    return fake_data

def print_fake_data(fake_data):
    for entry in fake_data:
        print(f"Name: {entry['name']}, Email: {entry['email']}, Phone: {entry['phone_number']}")

if __name__ == "__main__":
    num_entries = 10
    fake_data = generate_fake_data(num_entries)
    print_fake_data(fake_data)
