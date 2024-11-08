# data_generation/final_rating_generator.py

import uuid
import random
from data_generation.mentee_generator import generate_mentee_data

def generate_final_rating_data(num_entries, correct_ratio=0.9):
    """
    Generates Final Rating Prediction Database entries with mentor-mentee relationships.
    """
    final_ratings = []
    num_correct = int(num_entries * correct_ratio)

    for i in range(num_entries):
        mentor_id = f"mentor_{uuid.uuid4()}"
        mentor_final_rating = round(random.uniform(4.0, 5.0), 1)
        mentee_entries = generate_mentee_data(random.randint(1, 5))

        mentor = {
            "_id": str(uuid.uuid4()),
            "mentor_id": mentor_id,
            "mentor_final_rating": mentor_final_rating,
            "mentees": mentee_entries
        }

        # Introduce flaws in 10% of the entries
        if i >= num_correct:
            # Randomly introduce missing values or incorrect values
            fields_to_alter = random.sample(list(mentor.keys()), random.randint(1, 2))
            for field in fields_to_alter:
                if field == "mentor_final_rating":
                    mentor[field] = round(random.uniform(0, 2), 1)  # Unusually low rating
                elif field == "mentor_id":
                    mentor[field] = f"invalid_{uuid.uuid4()}"  # Incorrect value
                elif field == "mentees":
                    # Introduce flaws in mentee data
                    for mentee in mentor["mentees"]:
                        mentee_fields_to_alter = random.sample(list(mentee.keys()), random.randint(1, 3))
                        for m_field in mentee_fields_to_alter:
                            if m_field in ["feedback", "requested_slot_date", "session_actual_duration", "full_name"]:
                                mentee[m_field] = None  # Missing value
                            elif m_field == "mentee_rating":
                                mentee[m_field] = random.randint(1, 2)  # Low rating
                            elif m_field == "mentee_satisfaction_level":
                                mentee[m_field] = "Very Negative"  # Incorrect value
        final_ratings.append(mentor)
    return final_ratings
