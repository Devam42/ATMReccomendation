# data_generation/mentor_generator.py

import uuid
import random
from faker import Faker
from data_generation.utils import (
    PROFESSIONS, TEACHING_STYLES, select_random_elements,
    skills_dict, degrees, certifications_dict
)

fake = Faker()
Faker.seed(0)

def generate_mentor_data(num_entries, correct_ratio=0.9):
    """
    Generates mentor data for the Recommendation System Database with professional details.
    """
    mentors = []
    mentor_names_set = set()
    num_correct = int(num_entries * correct_ratio)

    for i in range(num_entries):
        mentor_id = f"mentor_{uuid.uuid4()}"
        profession = random.choice(PROFESSIONS)
        skills = skills_dict.get(profession, ["Communication", "Problem Solving", "Teamwork", "Time Management", "Leadership"])
        education_options = degrees.get(profession, ["BS in General Studies"])
        certifications_options = certifications_dict.get(profession, [])
        all_skills = skills.copy()

        # Ensure unique full names
        while True:
            full_name = fake.name()
            if full_name not in mentor_names_set:
                mentor_names_set.add(full_name)
                break

        year_of_experience = random.randint(3, 20)
        experience_text = f"{year_of_experience} years of experience as a {profession}"

        selected_skills = select_random_elements(skills, min_count=3)

        mentor = {
            "_id": str(uuid.uuid4()),
            "mentor_id": mentor_id,
            "full_name": full_name,
            "about": fake.sentence(nb_words=12),
            "location": f"{fake.city()}, {fake.country()}",
            "headline": profession,
            "skills": selected_skills,
            "education": select_random_elements(education_options, min_count=1),
            "experience": experience_text,
            "rating": round(random.uniform(4.0, 5.0), 1),
            "available_day": select_random_elements(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], min_count=1, max_count=3),
            "available_time": f"{random.randint(8, 15)}:00-{random.randint(16, 20)}:00",
            "subject": profession,
            "specialization": select_random_elements(all_skills, min_count=2),
            "year_of_experience": year_of_experience,
            "language": select_random_elements(
                ["English", "Spanish", "French", "German", "Mandarin", "Japanese", "Korean", "Italian", "Portuguese", "Russian",
                 "Hindi", "Arabic", "Turkish", "Dutch", "Swedish", "Polish", "Greek", "Hebrew", "Thai", "Vietnamese"],
                min_count=1, max_count=3
            ),
            "availability_status": "Yes",
            "mentor_image_url": fake.image_url(),
            "mentor_rating_trend": random.choice(["Stable", "Improving"]),
            "certifications": select_random_elements(certifications_options, min_count=0),
            "courses_taught": [f"{profession} Basics", f"Advanced {profession}"],
            "preferred_teaching_style": random.choice(TEACHING_STYLES),
            "background_image": fake.image_url()
        }

        # Introduce flaws in 10% of the entries
        if i >= num_correct:
            # Randomly introduce missing values or incorrect values
            fields_to_alter = random.sample(list(mentor.keys()), random.randint(1, 3))
            for field in fields_to_alter:
                if field in ["full_name", "about", "experience", "available_time", "mentor_image_url", "background_image"]:
                    mentor[field] = None  # Missing value
                elif field in ["skills", "education", "language", "available_day", "certifications"]:
                    mentor[field] = []  # Empty list
                elif field in ["rating", "year_of_experience"]:
                    # Introduce outliers
                    mentor[field] = round(random.uniform(0, 2), 1)  # Unusually low rating or experience
                elif field == "mentor_id":
                    mentor[field] = f"invalid_{uuid.uuid4()}"  # Incorrect value
                elif field == "availability_status":
                    mentor[field] = "Maybe"  # Incorrect value
                elif field == "mentor_rating_trend":
                    mentor[field] = "Declining"  # Possible but perhaps incorrect
                elif field == "courses_taught":
                    mentor[field] = []  # Empty list

        mentors.append(mentor)
    return mentors
