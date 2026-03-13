import csv
import random

# Define the possible responses for each question
responses = {
    "role": ["Pilot", "Co-pilot", "Flight Attendant", "Air Traffic Controller", "Other"],
    "experience": ["Less than 1 year", "1-5 years", "6-10 years", "More than 10 years"],
    "crm_training": ["Yes", "No"],
    "crm_effectiveness": ["Very Effective", "Effective", "Neutral", "Ineffective", "Very Ineffective"],
    "crm_frequency": ["Annually", "Bi-annually", "Every 2-3 years", "Rarely", "Never"],
    "crm_areas": [1, 2, 3, 4, 5],
    "crm_contribution": ["Significantly", "Moderately", "Slightly", "Not at all", "I’m not sure"],
    "crm_helped": ["Yes", "No"],
    "crm_improvement": ["To a great extent", "Somewhat", "Very little", "Not at all"],
    "crm_application": ["Always", "Frequently", "Sometimes", "Rarely"],
    "crm_aspect": ["Communication", "Teamwork", "Decision-making", "Fatigue management", "Other"],
    "crm_challenges": ["Time constraints", "Lack of team cooperation", "Poor communication", "Pressure from management", "Other"],
    "crm_preparation": ["Yes", "No"],
}

# Generate random responses
def generate_random_response():
    return {
        "role": random.choice(responses["role"]),
        "experience": random.choice(responses["experience"]),
        "crm_training": random.choice(responses["crm_training"]),
        "crm_effectiveness": random.choice(responses["crm_effectiveness"]),
        "crm_frequency": random.choice(responses["crm_frequency"]),
        "crm_training_addresses": random.choice(responses["crm_areas"]),
        "crm_contribution": random.choice(responses["crm_contribution"]),
        "crm_helped": random.choice(responses["crm_helped"]),
        "crm_improvement": random.choice(responses["crm_improvement"]),
        "crm_application": random.choice(responses["crm_application"]),
        "crm_aspect": random.choice(responses["crm_aspect"]),
        "crm_challenges": random.choice(responses["crm_challenges"]),
        "crm_preparation": random.choice(responses["crm_preparation"]),
        "general_comments": "N/A",
        "additional_comments": "N/A"
    }

# Generate 400 responses
responses_list = [generate_random_response() for _ in range(400)]

# Define the CSV file headers
headers = [
    "Role", "Experience", "CRM_Training", "CRM_Effectiveness", "CRM_Frequency",
    "CRM_Training_Addresses", "CRM_Contribution", "CRM_Helped", "CRM_Improvement", "CRM_Application",
    "CRM_Aspect", "CRM_Challenges", "CRM_Preparation", "General_Comments", "Additional_Comments"
]

# Write responses to CSV file
with open('./@questionaire/questionaire_responses.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for response in responses_list:
        writer.writerow({
            "Role": response["role"],
            "Experience": response["experience"],
            "CRM_Training": response["crm_training"],
            "CRM_Effectiveness": response["crm_effectiveness"],
            "CRM_Frequency": response["crm_frequency"],
            "CRM_Training_Addresses": response["crm_training_addresses"],
            "CRM_Contribution": response["crm_contribution"],
            "CRM_Helped": response["crm_helped"],
            "CRM_Improvement": response["crm_improvement"],
            "CRM_Application": response["crm_application"],
            "CRM_Aspect": response["crm_aspect"],
            "CRM_Challenges": response["crm_challenges"],
            "CRM_Preparation": response["crm_preparation"],
            "General_Comments": response["general_comments"],
            "Additional_Comments": response["additional_comments"]
        })