import json
import random
import uuid
from pymongo import MongoClient
from pymongo.server_api import  ServerApi
from urllib.parse import quote_plus
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(0)

#Monogo connection details
username = 'kjxsofttechpvtltd'
password = quote_plus('Rz@Fas092311')

#Monogo uri
uri = f"mongodb+srv://{username}:{password}@kjxwebsite.3mup0.mongodb.net/?retryWrites=true&w=majority&appName=kjxwebsite"

#New client to connect to server
client = MongoClient(uri, server_api=ServerApi('1'))

#Pint to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deploymnet. Successfully connected to mongoBD!")
except Exception as e:
    print(f"An error occured: {e}")

#Selecting database
db=client['Reccomendation']

# Generate mentor data for the Recommendation System Database with professional details
def generate_mentor_data(num_entries, starting_id, correct_ratio=0.9):
    mentors = []
    professions = [
        "Software Developer", "Data Scientist", "Financial Analyst", "Digital Marketing Specialist", "Cloud Engineer",
        "Cybersecurity Specialist", "AI Engineer", "Mechanical Engineer", "Graphic Designer", "Teacher",
        "Project Manager", "Marketing Manager", "Fitness Trainer", "Architect", "Pilot",
        "Chef", "Clinical Psychologist", "Real Estate Agent", "Environmental Scientist", "Software Tester",
        "Content Writer", "Sales Manager", "Research Scientist", "Medical Doctor", "Lawyer",
        "Accountant", "Photographer", "UX Designer", "Business Analyst", "Supply Chain Manager",
        "HR Specialist", "Network Engineer", "Investment Banker", "Civil Engineer", "Event Planner",
        "Data Analyst", "Electrical Engineer", "Systems Analyst", "Mobile App Developer", "Quality Assurance Engineer",
        "Full Stack Developer"
    ]

    skills_dict = {
        "Software Developer": ["Python", "Java", "C++", "Software Design", "Agile", "Git", "Algorithms", "Data Structures", "Debugging", "Unit Testing"],
        "Data Scientist": ["Python", "Machine Learning", "Statistics", "Data Analysis", "Deep Learning", "R", "SQL", "Data Visualization", "Pandas", "NumPy"],
        "Financial Analyst": ["Financial Modeling", "Excel", "Investment Analysis", "Risk Management", "Valuation", "Budgeting", "Forecasting", "Accounting"],
        "Digital Marketing Specialist": ["SEO", "Content Marketing", "Google Analytics", "Social Media Marketing", "Email Marketing", "PPC", "SEM", "Copywriting", "Brand Management"],
        "Cloud Engineer": ["AWS", "Azure", "Cloud Security", "Linux", "Kubernetes", "Docker", "Terraform", "CI/CD", "Networking"],
        "Cybersecurity Specialist": ["Network Security", "Penetration Testing", "Firewalls", "Encryption", "Incident Response", "Ethical Hacking", "Security Auditing", "Vulnerability Assessment"],
        "AI Engineer": ["Deep Learning", "Neural Networks", "TensorFlow", "PyTorch", "Natural Language Processing", "Computer Vision", "Reinforcement Learning", "Algorithm Development"],
        "Mechanical Engineer": ["CAD", "SolidWorks", "Thermodynamics", "Product Design", "Manufacturing", "Fluid Mechanics", "Mechanical Systems", "Finite Element Analysis"],
        "Graphic Designer": ["Adobe Photoshop", "Illustrator", "InDesign", "Typography", "Branding", "Sketch", "Figma", "Creative Suite", "Visual Communication"],
        "Teacher": ["Curriculum Development", "Classroom Management", "Subject Expertise", "Pedagogy", "Assessment", "Lesson Planning", "Educational Technology"],
        "Project Manager": ["Project Planning", "Risk Management", "Agile Methodologies", "Team Leadership", "Communication", "Stakeholder Management", "Budgeting"],
        "Marketing Manager": ["Market Research", "Campaign Management", "Brand Strategy", "Digital Marketing", "Public Relations", "Content Strategy", "CRM"],
        "Fitness Trainer": ["Personal Training", "Nutrition Guidance", "Workout Planning", "Motivation", "Group Fitness", "Anatomy", "Injury Prevention"],
        "Architect": ["Building Design", "AutoCAD", "3D Modeling", "Urban Planning", "Sustainable Design", "Revit", "Architectural Rendering", "Construction Documents"],
        "Pilot": ["Flight Operations", "Aircraft Safety", "Navigation", "Crew Coordination", "Communication", "Flight Planning", "Aviation Regulations"],
        "Chef": ["Culinary Arts", "Menu Planning", "Food Safety", "Team Management", "Creativity", "Culinary Techniques", "Pastry", "Nutrition"],
        "Clinical Psychologist": ["Cognitive Behavioral Therapy", "Patient Assessment", "Counseling", "Mental Health Diagnosis", "Treatment Planning", "Psychotherapy", "Crisis Intervention"],
        "Real Estate Agent": ["Property Sales", "Client Relations", "Negotiation", "Market Analysis", "Contract Management", "Property Valuation", "Real Estate Law"],
        "Environmental Scientist": ["Environmental Impact Assessment", "Data Collection", "Research Analysis", "Sustainability Strategies", "Field Work", "Ecology", "GIS"],
        "Software Tester": ["Test Automation", "Manual Testing", "Selenium", "Quality Assurance", "Test Planning", "Bug Tracking", "Performance Testing"],
        "Content Writer": ["SEO Writing", "Copywriting", "Editing", "Content Strategy", "Blogging", "Research", "Storytelling"],
        "Sales Manager": ["Sales Strategy", "Lead Generation", "CRM", "Team Management", "Negotiation", "Customer Service", "Market Analysis"],
        "Research Scientist": ["Data Analysis", "Laboratory Skills", "Scientific Writing", "Experiment Design", "Grant Writing", "Peer Review"],
        "Medical Doctor": ["Patient Care", "Diagnosis", "Treatment Planning", "Medical Research", "Surgery", "Medical Ethics", "Healthcare Management"],
        "Lawyer": ["Legal Research", "Litigation", "Contract Law", "Client Counseling", "Negotiation", "Regulatory Compliance", "Legal Writing"],
        "Accountant": ["Financial Reporting", "Tax Preparation", "Auditing", "Budgeting", "Financial Analysis", "Bookkeeping", "Regulatory Compliance"],
        "Photographer": ["Photo Editing", "Lighting", "Composition", "Digital Photography", "Adobe Lightroom", "Portrait Photography", "Event Photography"],
        "UX Designer": ["User Research", "Wireframing", "Prototyping", "Usability Testing", "Interaction Design", "Adobe XD", "Figma"],
        "Business Analyst": ["Requirement Gathering", "Process Improvement", "Data Modeling", "Stakeholder Engagement", "Business Intelligence", "Agile Methodologies"],
        "Supply Chain Manager": ["Logistics", "Inventory Management", "Procurement", "Vendor Management", "Operations Management", "Demand Forecasting"],
        "HR Specialist": ["Recruitment", "Employee Relations", "HR Policies", "Onboarding", "Training and Development", "Performance Management"],
        "Network Engineer": ["Network Design", "Cisco Technologies", "Routing Protocols", "Firewall Configuration", "VoIP", "Wireless Networking"],
        "Investment Banker": ["Financial Modeling", "Valuation", "Mergers and Acquisitions", "Capital Markets", "Due Diligence", "Pitch Books"],
        "Civil Engineer": ["Structural Analysis", "AutoCAD", "Construction Management", "Surveying", "Geotechnical Engineering", "Project Planning"],
        "Event Planner": ["Event Coordination", "Vendor Negotiation", "Budget Management", "Marketing", "Client Relations", "Logistics"],
        "Data Analyst": ["Data Cleaning", "Visualization", "SQL", "Excel", "Statistical Analysis", "Reporting"],
        "Electrical Engineer": ["Circuit Design", "Microcontrollers", "Embedded Systems", "Signal Processing", "Power Systems", "PCB Design"],
        "Systems Analyst": ["Systems Design", "Requirement Analysis", "UML", "Database Design", "Process Mapping", "Software Development Life Cycle"],
        "Mobile App Developer": ["iOS Development", "Android Development", "Flutter", "React Native", "UI/UX Design", "App Store Deployment"],
        "Quality Assurance Engineer": ["QA Testing", "Test Automation", "Selenium", "Load Testing", "Performance Testing", "JIRA"],
        "Full Stack Developer": ["Front-end Development", "Back-end Development", "JavaScript", "Node.js", "React", "Database Management", "APIs"],
    }

    degrees = {
        "Software Developer": ["BS in Computer Science", "MS in Software Engineering"],
        "Data Scientist": ["BS in Statistics", "MS in Data Science", "PhD in Machine Learning"],
        "Financial Analyst": ["BS in Finance", "MBA in Finance"],
        "Digital Marketing Specialist": ["BS in Marketing", "MBA in Marketing"],
        "Cloud Engineer": ["BS in Information Technology", "MS in Cloud Computing"],
        "Cybersecurity Specialist": ["BS in Cybersecurity", "MS in Information Security"],
        "AI Engineer": ["BS in Computer Science", "MS in Artificial Intelligence"],
        "Mechanical Engineer": ["BS in Mechanical Engineering", "MS in Mechanical Engineering"],
        "Graphic Designer": ["BA in Graphic Design", "BFA in Visual Arts"],
        "Teacher": ["BA in Education", "MA in Education"],
        "Project Manager": ["BS in Business Administration", "MBA in Project Management"],
        "Marketing Manager": ["BS in Marketing", "MBA in Marketing"],
        "Fitness Trainer": ["BS in Kinesiology", "Certified Personal Trainer"],
        "Architect": ["BA in Architecture", "Master of Architecture"],
        "Pilot": ["BS in Aviation", "Commercial Pilot License"],
        "Chef": ["Associate Degree in Culinary Arts", "Diploma in Professional Cooking"],
        "Clinical Psychologist": ["BS in Psychology", "PhD in Clinical Psychology"],
        "Real Estate Agent": ["BS in Business", "Real Estate License"],
        "Environmental Scientist": ["BS in Environmental Science", "MS in Environmental Engineering"],
        "Software Tester": ["BS in Computer Science", "Certification in Software Testing"],
        "Content Writer": ["BA in English", "MA in Creative Writing"],
        "Sales Manager": ["BS in Business Administration", "MBA"],
        "Research Scientist": ["BS in Biology", "PhD in Molecular Biology"],
        "Medical Doctor": ["MD in Medicine"],
        "Lawyer": ["LLB", "JD"],
        "Accountant": ["BS in Accounting", "Certified Public Accountant"],
        "Photographer": ["BA in Photography", "Diploma in Professional Photography"],
        "UX Designer": ["BA in Design", "Certification in UX/UI"],
        "Business Analyst": ["BS in Business Administration", "MBA"],
        "Supply Chain Manager": ["BS in Logistics", "MBA in Operations"],
        "HR Specialist": ["BS in Human Resources", "MBA in HR"],
        "Network Engineer": ["BS in Computer Networking", "Certification in Cisco Networking"],
        "Investment Banker": ["BS in Finance", "MBA"],
        "Civil Engineer": ["BS in Civil Engineering", "MS in Structural Engineering"],
        "Event Planner": ["BA in Hospitality Management", "Certification in Event Planning"],
        "Data Analyst": ["BS in Statistics", "MS in Data Analytics"],
        "Electrical Engineer": ["BS in Electrical Engineering", "MS in Electrical Engineering"],
        "Systems Analyst": ["BS in Computer Science", "MS in Information Systems"],
        "Mobile App Developer": ["BS in Computer Science", "Certification in Mobile Development"],
        "Quality Assurance Engineer": ["BS in Computer Science", "Certification in QA Testing"],
        "Full Stack Developer": ["BS in Computer Science", "MS in Software Engineering"],
    }

    certifications_dict = {
        "Software Developer": ["Oracle Certified Professional, Java SE", "Microsoft Certified: Azure Developer Associate"],
        "Data Scientist": ["Certified Data Scientist", "Cloudera Certified Data Professional"],
        "Financial Analyst": ["Chartered Financial Analyst (CFA)", "Financial Risk Manager (FRM)"],
        "Digital Marketing Specialist": ["Google Ads Certification", "HubSpot Content Marketing Certification"],
        "Cloud Engineer": ["AWS Certified Solutions Architect", "Microsoft Certified: Azure Solutions Architect Expert"],
        "Cybersecurity Specialist": ["Certified Information Systems Security Professional (CISSP)", "Certified Ethical Hacker (CEH)"],
        "AI Engineer": ["Microsoft Certified: Azure AI Engineer Associate", "Google Cloud Professional Data Engineer"],
        "Mechanical Engineer": ["Professional Engineer (PE)", "Certified SolidWorks Professional"],
        "Graphic Designer": ["Adobe Certified Expert (ACE)", "Certified Graphic Designer"],
        "Teacher": ["Teaching Credential", "National Board Certification"],
        "Project Manager": ["Project Management Professional (PMP)", "Certified Scrum Master (CSM)"],
        "Marketing Manager": ["Certified Marketing Management Professional", "Digital Marketing Institute Certification"],
        "Fitness Trainer": ["Certified Personal Trainer (CPT)", "Certified Strength and Conditioning Specialist (CSCS)"],
        "Architect": ["Licensed Architect", "LEED Accredited Professional"],
        "Pilot": ["Airline Transport Pilot License", "Certified Flight Instructor"],
        "Chef": ["Certified Executive Chef", "Certified Culinary Educator"],
        "Clinical Psychologist": ["Licensed Clinical Psychologist", "Board Certified in Clinical Psychology"],
        "Real Estate Agent": ["Real Estate Broker License", "Certified Residential Specialist (CRS)"],
        "Environmental Scientist": ["Certified Environmental Scientist", "LEED Green Associate"],
        "Software Tester": ["ISTQB Certified Tester", "Certified Software Quality Analyst (CSQA)"],
        "Content Writer": ["Certified Professional Technical Communicator", "SEO Copywriting Certification"],
        "Sales Manager": ["Certified Sales Professional (CSP)", "Certified Professional Sales Person (CPSP)"],
        "Research Scientist": ["Certified Research Administrator", "Professional Researcher Certification"],
        "Medical Doctor": ["Board Certified Physician", "Fellowship in Specialty"],
        "Lawyer": ["Bar Admission", "Certified Legal Specialist"],
        "Accountant": ["Certified Public Accountant (CPA)", "Certified Management Accountant (CMA)"],
        "Photographer": ["Certified Professional Photographer", "Adobe Certified Expert"],
        "UX Designer": ["Certified UX Designer", "Interaction Design Foundation Certification"],
        "Business Analyst": ["Certified Business Analysis Professional (CBAP)", "PMI Professional in Business Analysis (PMI-PBA)"],
        "Supply Chain Manager": ["Certified Supply Chain Professional (CSCP)", "Certified in Logistics, Transportation and Distribution (CLTD)"],
        "HR Specialist": ["Professional in Human Resources (PHR)", "SHRM Certified Professional (SHRM-CP)"],
        "Network Engineer": ["Cisco Certified Network Professional (CCNP)", "CompTIA Network+"],
        "Investment Banker": ["Series 7 License", "Chartered Financial Analyst (CFA)"],
        "Civil Engineer": ["Professional Engineer (PE)", "Certified Construction Manager (CCM)"],
        "Event Planner": ["Certified Meeting Professional (CMP)", "Certified Special Events Professional (CSEP)"],
        "Data Analyst": ["Microsoft Certified: Data Analyst Associate", "IBM Data Science Professional Certificate"],
        "Electrical Engineer": ["Professional Engineer (PE)", "Certified Energy Manager (CEM)"],
        "Systems Analyst": ["Certified Systems Analyst Professional", "ITIL Foundation Certification"],
        "Mobile App Developer": ["Certified iOS Developer", "Android Certified Application Developer"],
        "Quality Assurance Engineer": ["Certified Quality Engineer (CQE)", "ISTQB Advanced Level Test Manager"],
        "Full Stack Developer": ["Certified Web Development Professional", "Microsoft Certified Solutions Developer (MCSD)"],
    }

    teaching_styles = ["Structured", "Hands-on", "Interactive", "Creative", "Flexible", "Project-based", "Analytical"]

    mentor_names_set = set()
    num_correct = int(num_entries * correct_ratio)

    for i in range(num_entries):
        mentor_id = f"mentor_{uuid.uuid4()}"
        profession = random.choice(professions)
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

        # Randomly decide how many skills to include (sometimes all, sometimes less)
        num_skills = random.randint(3, len(skills))
        selected_skills = random.sample(skills, num_skills)

        mentor = {
            "_id": str(uuid.uuid4()),
            "mentor_id": mentor_id,
            "full_name": full_name,
            "about": fake.sentence(nb_words=12),
            "location": f"{fake.city()}, {fake.country()}",
            "headline": profession,
            "skills": selected_skills,
            "education": random.sample(education_options, random.randint(1, len(education_options))),
            "experience": experience_text,
            "rating": round(random.uniform(4.0, 5.0), 1),
            "available_day": random.sample(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], random.randint(1, 3)),
            "available_time": f"{random.randint(8, 15)}:00-{random.randint(16, 20)}:00",
            "subject": profession,
            "specialization": random.sample(all_skills, min(2, len(all_skills))),
            "year_of_experience": year_of_experience,
            "language": random.sample(
                ["English", "Spanish", "French", "German", "Mandarin", "Japanese", "Korean", "Italian", "Portuguese", "Russian",
                 "Hindi", "Arabic", "Turkish", "Dutch", "Swedish", "Polish", "Greek", "Hebrew", "Thai", "Vietnamese"],
                random.randint(1, 3)
            ),
            "availability_status": "Yes",
            "mentor_image_url": fake.image_url(),
            "mentor_rating_trend": random.choice(["Stable", "Improving"]),
            "certifications": random.sample(certifications_options, random.randint(0, len(certifications_options))),
            "courses_taught": [f"{profession} Basics", f"Advanced {profession}"],
            "preferred_teaching_style": random.choice(teaching_styles),
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

# Generate mentee data for the Final Rating Prediction Database
def generate_mentee_data(num_entries, starting_id):
    mentees = []
    mentee_names_set = set()
    for i in range(num_entries):
        mentee_id = f"mentee_{uuid.uuid4()}"
        # Ensure unique mentee names if needed
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

# Generate Final Rating Prediction Database entries with mentor-mentee relationships
def generate_final_rating_data(num_entries, correct_ratio=0.9):
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

# Number of entries to generate
num_entries = 10
correct_ratio = 0.9

# Generate data
print("Generating mentor data...")
mentor_data = generate_mentor_data(num_entries, correct_ratio)
print("Generating final rating data...")
final_rating_data=generate_final_rating_data(num_entries, correct_ratio)

#Insert data into mongodb
recommendations_collection=db['RecommendationSystemDatabase']
final_ratings_collection = db['FinalRating']

#Insert mentordata
try:
    recommendations_collection.insert_many(mentor_data)
    print("Mentor data inserted successfully into 'RecommendationSystemDatabase' colleaction.")
except Exception as e:
    print(f"An error occured while inserting the data: {e}")

#Insert final rating data
try:
    final_ratings_collection.insert_many(final_rating_data)
    print("Final rating data inserted successfully into 'FinalRating' collection.")
except Exception as e:
    print(f"An error occurred while  inserting final rating data: {e}")