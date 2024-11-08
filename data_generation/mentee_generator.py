# data_generation/mentee_generator.py

import uuid
import random
from faker import Faker

fake = Faker()
Faker.seed(0)

def generate_mentee_data(num_entries):
    """
    Generates mentee data for the Final Rating Prediction Database.
    """
    mentees = []
    mentee_names_set = set()

    for i in range(num_entries):
        mentee_id = f"mentee_{uuid.uuid4()}"
        # Ensure unique mentee names
        while True:
            full_name = fake.name()
            if full_name not in mentee_names_set:
                mentee_names_set.add(full_name)
                break

        requested_date = fake.date_between(start_date='-1y', end_date='today').isoformat()
        requested_slot_start = random.randint(8, 17)
        requested_slot_end = requested_slot_start + random.randint(1, 3)
        session_duration = random.choice([30, 60, 90, 120])
        mentee = {
            "mentee_id": mentee_id,
            "full_name": full_name,
            "requested_slot_date": requested_date,
            "requested_slot": f"{requested_slot_start}:00 - {requested_slot_end}:00",
            "status": random.choice(["Accepted", "Pending", "Rejected", "Cancelled"]),
            "session_type": random.choice(["One-on-One", "Group", "Workshop"]),
            "session_actual_duration": f"{session_duration} mins" if random.random() > 0.1 else "0 mins",
            "session_held": random.choice(["On time", "Delayed", "Cancelled"]),
            "mentor_response_time": random.choice(["within 12 hours", "within 24 hours", "within 48 hours"]),
            "feedback": fake.sentence(nb_words=10) if random.random() > 0.1 else "",
            "mentee_rating": random.randint(3, 5),
            "mentee_satisfaction_level": random.choice(["Positive", "Neutral", "Negative"])
        }
        mentees.append(mentee)
    return mentees
