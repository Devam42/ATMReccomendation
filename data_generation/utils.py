import random

PROFESSIONS = [
    "Ethical Hacker",
    "Renewable Energy Consultant",
    "Urban Planner",
    "Environmental Engineer",
    "Marine Biologist",
    "Geneticist",
    "AI Ethicist",
    "Virtual Reality Designer",
    "Blockchain Analyst",
    "Data Privacy Consultant",
    "E-Commerce Manager",
    "Digital Marketing Specialist",
    "Content Creator",
    "Social Media Influencer",
    "Yoga Instructor",
    "Life Coach",
    "Dietitian",
    "Zookeeper",
    "Museum Curator",
    "Archivist",
    "Librarian",
    "Sound Technician",
    "Voiceover Artist",
    "Fashion Designer",
    "Makeup Artist",
    "Hairstylist",
    "Wedding Planner",
    "Interior Decorator",
    "Floral Designer",
    "Landscape Architect",
    "Dog Trainer",
    "Pet Groomer",
    "Veterinary Assistant",
    "Childcare Provider",
    "Speech Therapist",
    "Occupational Therapist",
    "Physical Therapist",
    "Personal Assistant",
    "Event Coordinator",
    "Humanitarian Aid Worker",
    "Nonprofit Manager",
    "Policy Analyst",
    "Lobbyist",
    "Diplomat",
    "Foreign Language Teacher",
    "ESL Teacher",
    "Travel Agent",
    "Tour Guide",
    "Flight Attendant",
    "Hotel Manager"
]

skills_dict = {
    "Ethical Hacker": [
        "Penetration Testing", "Vulnerability Assessment", "Network Security",
        "Scripting Languages", "Intrusion Detection", "Ethical Hacking Techniques",
        "Encryption", "Firewalls", "Social Engineering", "Compliance Standards"
    ],
    "Renewable Energy Consultant": [
        "Energy Auditing", "Sustainability Strategies", "Project Management",
        "Environmental Regulations", "Solar Energy", "Wind Energy",
        "Data Analysis", "Communication Skills", "Business Development", "Technical Writing"
    ],
    "Urban Planner": [
        "Urban Design", "GIS", "Zoning Regulations", "Environmental Planning",
        "Community Engagement", "Policy Analysis", "Project Management",
        "Sustainability", "Analytical Skills", "Communication Skills"
    ],
    "Environmental Engineer": [
        "Waste Management", "Water Treatment", "Environmental Impact Assessment",
        "Regulatory Compliance", "Sustainability", "Project Management",
        "Data Analysis", "Technical Writing", "Problem Solving", "Communication Skills"
    ],
    "Marine Biologist": [
        "Marine Ecology", "Field Research", "Data Analysis", "SCUBA Diving",
        "GIS", "Conservation Strategies", "Laboratory Skills",
        "Report Writing", "Critical Thinking", "Communication Skills"
    ],
    "Geneticist": [
        "Molecular Biology", "DNA Sequencing", "Bioinformatics",
        "Laboratory Techniques", "Data Analysis", "Research Skills",
        "Critical Thinking", "Genetic Counseling", "Teaching", "Communication Skills"
    ],
    "AI Ethicist": [
        "Ethical Frameworks", "Artificial Intelligence", "Policy Development",
        "Research Skills", "Critical Thinking", "Communication Skills",
        "Public Speaking", "Philosophy", "Regulatory Knowledge", "Problem Solving"
    ],
    "Virtual Reality Designer": [
        "3D Modeling", "Unity", "Unreal Engine", "C# Programming",
        "User Experience Design", "Graphic Design", "Animation",
        "Virtual Reality SDKs", "Creativity", "Problem Solving"
    ],
    "Blockchain Analyst": [
        "Blockchain Technology", "Smart Contracts", "Cryptography",
        "Data Analysis", "Solidity", "Ethereum", "Bitcoin Protocol",
        "Problem Solving", "Critical Thinking", "Communication Skills"
    ],
    "Data Privacy Consultant": [
        "Data Protection Regulations", "Risk Assessment", "Policy Development",
        "Compliance Standards", "Cybersecurity", "Communication Skills",
        "Problem Solving", "Critical Thinking", "Training", "Legal Knowledge"
    ],
    "E-Commerce Manager": [
        "Online Marketing", "SEO", "Data Analysis", "Product Management",
        "Customer Service", "Content Management Systems", "Digital Advertising",
        "Inventory Management", "Communication Skills", "Problem Solving"
    ],
    "Digital Marketing Specialist": [
        "SEO", "Content Marketing", "Google Analytics",
        "Social Media Marketing", "Email Marketing", "PPC Advertising",
        "Copywriting", "Brand Management", "Communication Skills", "Creativity"
    ],
    "Content Creator": [
        "Writing Skills", "SEO", "Social Media Platforms",
        "Graphic Design", "Photography", "Videography",
        "Editing", "Creativity", "Communication Skills", "Time Management"
    ],
    "Social Media Influencer": [
        "Content Creation", "Brand Collaboration", "Engagement Strategies",
        "Photography", "Videography", "Social Media Platforms",
        "Communication Skills", "Networking", "Creativity", "Marketing"
    ],
    "Yoga Instructor": [
        "Yoga Techniques", "Anatomy", "Physiology", "Instruction Skills",
        "Class Planning", "Motivation Techniques", "Communication Skills",
        "Mindfulness", "First Aid", "CPR"
    ],
    "Life Coach": [
        "Coaching Techniques", "Communication Skills", "Goal Setting",
        "Motivation Techniques", "Active Listening", "Empathy",
        "Problem Solving", "Time Management", "Business Development", "Ethics"
    ],
    "Dietitian": [
        "Nutrition Planning", "Health Assessment", "Patient Counseling",
        "Meal Planning", "Clinical Nutrition", "Food Safety",
        "Communication Skills", "Empathy", "Research Skills", "Regulatory Compliance"
    ],
    "Zookeeper": [
        "Animal Care", "Animal Behavior", "Habitat Maintenance",
        "Feeding and Nutrition", "Record Keeping", "Conservation Education",
        "Physical Stamina", "Safety Protocols", "Teamwork", "Communication Skills"
    ],
    "Museum Curator": [
        "Collection Management", "Exhibition Design", "Art History",
        "Research Skills", "Conservation Techniques", "Public Speaking",
        "Grant Writing", "Event Planning", "Communication Skills", "Attention to Detail"
    ],
    "Archivist": [
        "Archival Research", "Document Preservation", "Cataloging",
        "Database Management", "Attention to Detail", "Historical Knowledge",
        "Research Skills", "Organization", "Communication Skills", "Digital Archiving"
    ],
    "Librarian": [
        "Information Management", "Cataloging", "Reference Services",
        "Research Skills", "Digital Literacy", "Customer Service",
        "Organization", "Communication Skills", "Collection Development", "Information Technology"
    ],
    "Sound Technician": [
        "Audio Equipment Setup", "Sound Mixing", "Recording Techniques",
        "Troubleshooting", "Attention to Detail", "Communication Skills",
        "Teamwork", "Technical Knowledge", "Live Sound", "Acoustics"
    ],
    "Voiceover Artist": [
        "Vocal Techniques", "Acting Skills", "Script Interpretation",
        "Recording Equipment", "Editing Software", "Communication Skills",
        "Creativity", "Time Management", "Self-Promotion", "Adaptability"
    ],
    "Fashion Designer": [
        "Design Software", "Sketching", "Fabric Knowledge",
        "Sewing Techniques", "Trend Analysis", "Creativity",
        "Attention to Detail", "Business Skills", "Communication Skills", "Pattern Making"
    ],
    "Makeup Artist": [
        "Makeup Techniques", "Color Theory", "Skin Care",
        "Customer Service", "Creativity", "Attention to Detail",
        "Hygiene Practices", "Time Management", "Communication Skills", "Product Knowledge"
    ],
    "Hairstylist": [
        "Hair Cutting", "Styling Techniques", "Coloring Techniques",
        "Customer Service", "Creativity", "Attention to Detail",
        "Hygiene Practices", "Time Management", "Communication Skills", "Product Knowledge"
    ],
    "Wedding Planner": [
        "Event Coordination", "Vendor Negotiation", "Budget Management",
        "Creativity", "Organization", "Time Management",
        "Communication Skills", "Problem Solving", "Attention to Detail", "Customer Service"
    ],
    "Interior Decorator": [
        "Space Planning", "Color Theory", "Material Selection",
        "Creativity", "Communication Skills", "Client Relations",
        "Budgeting", "Project Management", "Attention to Detail", "Trend Analysis"
    ],
    "Floral Designer": [
        "Flower Arranging", "Creativity", "Customer Service",
        "Time Management", "Color Theory", "Plant Care",
        "Event Planning", "Attention to Detail", "Communication Skills", "Business Management"
    ],
    "Landscape Architect": [
        "Landscape Design", "Plant Knowledge", "CAD Software",
        "Environmental Planning", "Sustainability", "Project Management",
        "Creativity", "Communication Skills", "Problem Solving", "Regulatory Knowledge"
    ],
    "Dog Trainer": [
        "Animal Behavior", "Training Techniques", "Patience",
        "Communication Skills", "Customer Service", "Problem Solving",
        "Physical Stamina", "First Aid", "Observation Skills", "Business Management"
    ],
    "Pet Groomer": [
        "Grooming Techniques", "Animal Handling", "Customer Service",
        "Creativity", "Attention to Detail", "Time Management",
        "Hygiene Practices", "Safety Protocols", "Communication Skills", "Business Management"
    ],
    "Veterinary Assistant": [
        "Animal Care", "Medical Terminology", "Laboratory Skills",
        "Customer Service", "Communication Skills", "Attention to Detail",
        "Physical Stamina", "Teamwork", "Record Keeping", "Ethics"
    ],
    "Childcare Provider": [
        "Child Development", "First Aid", "CPR",
        "Communication Skills", "Patience", "Creativity",
        "Behavior Management", "Organization", "Safety Protocols", "Problem Solving"
    ],
    "Speech Therapist": [
        "Communication Disorders", "Patient Assessment", "Therapy Techniques",
        "Anatomy", "Physiology", "Critical Thinking",
        "Compassion", "Record Keeping", "Communication Skills", "Ethics"
    ],
    "Occupational Therapist": [
        "Therapeutic Techniques", "Patient Assessment", "Activity Planning",
        "Anatomy", "Physiology", "Communication Skills",
        "Compassion", "Problem Solving", "Documentation", "Adaptability"
    ],
    "Physical Therapist": [
        "Rehabilitation Techniques", "Anatomy", "Physiology",
        "Patient Assessment", "Exercise Therapy", "Communication Skills",
        "Compassion", "Problem Solving", "Manual Therapy", "Documentation"
    ],
    "Personal Assistant": [
        "Organization", "Time Management", "Communication Skills",
        "Scheduling", "Problem Solving", "Confidentiality",
        "Multitasking", "Attention to Detail", "Travel Coordination", "Office Management"
    ],
    "Event Coordinator": [
        "Event Planning", "Vendor Management", "Budgeting",
        "Marketing", "Communication Skills", "Time Management",
        "Creativity", "Problem Solving", "Negotiation", "Customer Service"
    ],
    "Humanitarian Aid Worker": [
        "Crisis Management", "Cultural Sensitivity", "Project Management",
        "Communication Skills", "Problem Solving", "Foreign Languages",
        "Teamwork", "Adaptability", "First Aid", "Logistics"
    ],
    "Nonprofit Manager": [
        "Fundraising", "Grant Writing", "Project Management",
        "Budgeting", "Communication Skills", "Leadership",
        "Strategic Planning", "Team Management", "Networking", "Problem Solving"
    ],
    "Policy Analyst": [
        "Research Skills", "Data Analysis", "Critical Thinking",
        "Communication Skills", "Writing Skills", "Policy Development",
        "Problem Solving", "Analytical Skills", "Public Speaking", "Attention to Detail"
    ],
    "Lobbyist": [
        "Communication Skills", "Networking", "Negotiation",
        "Public Speaking", "Political Knowledge", "Research Skills",
        "Writing Skills", "Critical Thinking", "Strategic Planning", "Ethics"
    ],
    "Diplomat": [
        "Foreign Languages", "Cultural Awareness", "Negotiation",
        "Communication Skills", "Political Knowledge", "Problem Solving",
        "Analytical Skills", "Adaptability", "Leadership", "Confidentiality"
    ],
    "Foreign Language Teacher": [
        "Language Proficiency", "Teaching Skills", "Lesson Planning",
        "Cultural Knowledge", "Communication Skills", "Patience",
        "Creativity", "Assessment Skills", "Classroom Management", "Technology Integration"
    ],
    "ESL Teacher": [
        "English Language Proficiency", "Teaching Skills", "Lesson Planning",
        "Cultural Sensitivity", "Communication Skills", "Patience",
        "Creativity", "Assessment Skills", "Classroom Management", "Technology Integration"
    ],
    "Travel Agent": [
        "Destination Knowledge", "Customer Service", "Sales Skills",
        "Communication Skills", "Attention to Detail", "Organization",
        "Problem Solving", "Reservation Systems", "Budgeting", "Foreign Languages"
    ],
    "Tour Guide": [
        "Historical Knowledge", "Storytelling", "Public Speaking",
        "Customer Service", "Communication Skills", "Foreign Languages",
        "Navigation Skills", "First Aid", "Time Management", "Enthusiasm"
    ],
    "Flight Attendant": [
        "Customer Service", "Safety Protocols", "First Aid",
        "Communication Skills", "Foreign Languages", "Problem Solving",
        "Conflict Resolution", "Teamwork", "Adaptability", "Attention to Detail"
    ],
    "Hotel Manager": [
        "Hospitality Management", "Customer Service", "Leadership",
        "Budgeting", "Communication Skills", "Problem Solving",
        "Sales and Marketing", "Team Management", "Organization", "Attention to Detail"
    ]
}

degrees = {
    "Ethical Hacker": ["Bachelor's in Computer Science", "Certified Ethical Hacker Certification"],
    "Renewable Energy Consultant": ["Bachelor's in Environmental Science", "Master's in Renewable Energy"],
    "Urban Planner": ["Bachelor's in Urban Planning", "Master's in Urban Design"],
    "Environmental Engineer": ["Bachelor's in Environmental Engineering", "Master's in Environmental Engineering"],
    "Marine Biologist": ["Bachelor's in Marine Biology", "Master's in Marine Science"],
    "Geneticist": ["Bachelor's in Genetics", "PhD in Genetics"],
    "AI Ethicist": ["Bachelor's in Philosophy", "Master's in Ethics and Technology"],
    "Virtual Reality Designer": ["Bachelor's in Computer Science", "Bachelor's in Game Design"],
    "Blockchain Analyst": ["Bachelor's in Computer Science", "Certification in Blockchain Technology"],
    "Data Privacy Consultant": ["Bachelor's in Information Technology", "Certification in Data Privacy"],
    "E-Commerce Manager": ["Bachelor's in Business Administration", "Certification in E-Commerce"],
    "Digital Marketing Specialist": ["Bachelor's in Marketing", "Certification in Digital Marketing"],
    "Content Creator": ["Bachelor's in Communications", "Bachelor's in Journalism"],
    "Social Media Influencer": ["Bachelor's in Marketing", "Experience in Social Media"],
    "Yoga Instructor": ["Yoga Teacher Training Certification"],
    "Life Coach": ["Certification in Life Coaching"],
    "Dietitian": ["Bachelor's in Nutrition", "Registered Dietitian Nutritionist"],
    "Zookeeper": ["Bachelor's in Zoology", "Associate Degree in Animal Science"],
    "Museum Curator": ["Bachelor's in Art History", "Master's in Museum Studies"],
    "Archivist": ["Bachelor's in History", "Master's in Library Science"],
    "Librarian": ["Bachelor's in Library Science", "Master's in Library and Information Science"],
    "Sound Technician": ["Associate Degree in Audio Engineering", "Certification in Sound Technology"],
    "Voiceover Artist": ["Training in Voice Acting", "Experience in Acting"],
    "Fashion Designer": ["Bachelor's in Fashion Design", "Associate Degree in Fashion Merchandising"],
    "Makeup Artist": ["Certification in Cosmetology", "Diploma in Makeup Artistry"],
    "Hairstylist": ["Certification in Cosmetology", "Apprenticeship"],
    "Wedding Planner": ["Bachelor's in Event Management", "Certification in Wedding Planning"],
    "Interior Decorator": ["Associate Degree in Interior Design", "Certification in Interior Decorating"],
    "Floral Designer": ["Certification in Floral Design", "Experience in Horticulture"],
    "Landscape Architect": ["Bachelor's in Landscape Architecture", "Master's in Landscape Architecture"],
    "Dog Trainer": ["Certification in Dog Training", "Experience in Animal Behavior"],
    "Pet Groomer": ["Certification in Pet Grooming", "Apprenticeship"],
    "Veterinary Assistant": ["Associate Degree in Veterinary Technology"],
    "Childcare Provider": ["Certification in Early Childhood Education", "First Aid and CPR Certification"],
    "Speech Therapist": ["Bachelor's in Communication Disorders", "Master's in Speech-Language Pathology"],
    "Occupational Therapist": ["Master's in Occupational Therapy"],
    "Physical Therapist": ["Doctor of Physical Therapy (DPT)"],
    "Personal Assistant": ["Associate Degree in Business Administration", "Experience as an Administrative Assistant"],
    "Event Coordinator": ["Bachelor's in Hospitality Management", "Certification in Event Planning"],
    "Humanitarian Aid Worker": ["Bachelor's in International Relations", "Master's in Humanitarian Action"],
    "Nonprofit Manager": ["Bachelor's in Nonprofit Management", "Master's in Public Administration"],
    "Policy Analyst": ["Bachelor's in Political Science", "Master's in Public Policy"],
    "Lobbyist": ["Bachelor's in Political Science", "Law Degree (JD)"],
    "Diplomat": ["Bachelor's in International Relations", "Master's in Diplomacy"],
    "Foreign Language Teacher": ["Bachelor's in Education", "Bachelor's in Foreign Language"],
    "ESL Teacher": ["Bachelor's in English", "TESOL Certification"],
    "Travel Agent": ["Associate Degree in Travel and Tourism", "Certification in Travel Consultancy"],
    "Tour Guide": ["High School Diploma", "Certification in Tour Guiding"],
    "Flight Attendant": ["High School Diploma", "Flight Attendant Training"],
    "Hotel Manager": ["Bachelor's in Hospitality Management", "Associate Degree in Hotel Management"]
}

certifications_dict = {
    "Ethical Hacker": [
        "Certified Ethical Hacker (CEH)", "CompTIA Security+",
        "Offensive Security Certified Professional (OSCP)"
    ],
    "Renewable Energy Consultant": [
        "LEED Accredited Professional", "Certified Energy Manager (CEM)",
        "Renewable Energy Professional Certification"
    ],
    "Urban Planner": [
        "American Institute of Certified Planners (AICP)", "LEED Green Associate"
    ],
    "Environmental Engineer": [
        "Professional Engineer (PE)", "Certified Environmental Engineer"
    ],
    "Marine Biologist": [
        "SCUBA Certification", "Marine Biology Certification"
    ],
    "Geneticist": [
        "Certification in Genetics", "Medical Genetics Board Certification"
    ],
    "AI Ethicist": [
        "AI Ethics Certification", "Membership in Ethics Societies"
    ],
    "Virtual Reality Designer": [
        "Unity Certified Developer", "Unreal Engine Certification"
    ],
    "Blockchain Analyst": [
        "Certified Blockchain Professional", "Blockchain Council Certifications"
    ],
    "Data Privacy Consultant": [
        "Certified Information Privacy Professional (CIPP)",
        "Certified Information Privacy Manager (CIPM)"
    ],
    "E-Commerce Manager": [
        "Certified E-Commerce Manager", "Google Analytics Certification"
    ],
    "Digital Marketing Specialist": [
        "Google Ads Certification", "HubSpot Inbound Marketing Certification"
    ],
    "Content Creator": [
        "Content Marketing Certification", "SEO Certification"
    ],
    "Social Media Influencer": [
        "Social Media Marketing Certification", "Influencer Marketing Certification"
    ],
    "Yoga Instructor": [
        "Yoga Alliance Registered Yoga Teacher (RYT)", "CPR and First Aid Certification"
    ],
    "Life Coach": [
        "Certified Professional Coach (CPC)", "International Coach Federation (ICF) Certification"
    ],
    "Dietitian": [
        "Registered Dietitian Nutritionist (RDN)", "Certified Nutrition Specialist (CNS)"
    ],
    "Zookeeper": [
        "Certified Zoo Professional", "Animal Care Certifications"
    ],
    "Museum Curator": [
        "Certification in Museum Studies", "Membership in Curator Associations"
    ],
    "Archivist": [
        "Certified Archivist", "Digital Archives Specialist (DAS)"
    ],
    "Librarian": [
        "Master of Library Science (MLS)", "Public Librarian Certification"
    ],
    "Sound Technician": [
        "Certified Audio Engineer", "Pro Tools Certification"
    ],
    "Voiceover Artist": [
        "Voice Acting Workshops", "Demo Reel"
    ],
    "Fashion Designer": [
        "Fashion Design Certification", "Membership in Fashion Associations"
    ],
    "Makeup Artist": [
        "Cosmetology License", "Makeup Artist Certification"
    ],
    "Hairstylist": [
        "Cosmetology License", "Barber License"
    ],
    "Wedding Planner": [
        "Certified Wedding Planner", "Event Planning Certification"
    ],
    "Interior Decorator": [
        "Certified Interior Decorator (CID)", "National Council for Interior Design Qualification (NCIDQ)"
    ],
    "Floral Designer": [
        "Certified Floral Designer (CFD)", "American Institute of Floral Designers (AIFD) Certification"
    ],
    "Landscape Architect": [
        "Landscape Architect License", "LEED Accredited Professional"
    ],
    "Dog Trainer": [
        "Certified Professional Dog Trainer (CPDT)", "Animal Behavior College Certification"
    ],
    "Pet Groomer": [
        "National Certified Master Groomer", "Professional Pet Groomer Certification"
    ],
    "Veterinary Assistant": [
        "Approved Veterinary Assistant (AVA)", "Certified Veterinary Assistant (CVA)"
    ],
    "Childcare Provider": [
        "Child Development Associate (CDA)", "First Aid and CPR Certification"
    ],
    "Speech Therapist": [
        "Certificate of Clinical Competence in Speech-Language Pathology (CCC-SLP)"
    ],
    "Occupational Therapist": [
        "Occupational Therapist License", "NBCOT Certification"
    ],
    "Physical Therapist": [
        "Physical Therapist License", "Board Certification in Specialty Areas"
    ],
    "Personal Assistant": [
        "None", "Administrative Assistant Certification"
    ],
    "Event Coordinator": [
        "Certified Meeting Professional (CMP)", "Certified Special Events Professional (CSEP)"
    ],
    "Humanitarian Aid Worker": [
        "None", "Certificates in Humanitarian Studies"
    ],
    "Nonprofit Manager": [
        "Certified Nonprofit Professional (CNP)", "Fundraising Certification"
    ],
    "Policy Analyst": [
        "None", "Certifications in Policy Analysis"
    ],
    "Lobbyist": [
        "Registration as Lobbyist", "Law License"
    ],
    "Diplomat": [
        "Foreign Service Officer Test (FSOT)", "Diplomatic Training"
    ],
    "Foreign Language Teacher": [
        "Teaching Credential", "Certification in Foreign Language Teaching"
    ],
    "ESL Teacher": [
        "Teaching English as a Foreign Language (TEFL) Certification", "TESOL Certification"
    ],
    "Travel Agent": [
        "Certified Travel Associate (CTA)", "Certified Travel Counselor (CTC)"
    ],
    "Tour Guide": [
        "Tour Guide Certification", "First Aid and CPR Certification"
    ],
    "Flight Attendant": [
        "Flight Attendant Certification", "First Aid and CPR Certification"
    ],
    "Hotel Manager": [
        "Certified Hotel Administrator (CHA)", "Hospitality Management Certification"
    ]
}

TEACHING_STYLES = ["Structured", "Hands-on", "Interactive", "Creative", "Flexible", "Project-based", "Analytical"]

def select_random_elements(data_list, min_count=1, max_count=None):
    """
    Select a random number of elements from a list.
    """
    if max_count is None or max_count > len(data_list):
        max_count = len(data_list)
    count = random.randint(min_count, max_count)
    return random.sample(data_list, count)
