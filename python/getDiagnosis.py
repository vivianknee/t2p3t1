#import selenium
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

# medical website base address
medical_website = "https://medlineplus.gov/"


# user_symptoms will come in as a string ("0,3,7") from front end, the string will be parsed into a list like [0, 3, 7]
user_symptoms = [0, 3, 7]

# possible symptoms that the user can check mark
symptoms_database = [
  "Cough", "Sore throat", "Headache", "Fever", "Muscle pain", "Stomach ache",
  "Congested nose", "Runny nose", "Painful coughing", "Swollen mouth",
  "Swollen face", "Pimples", "Sneezing", "Vomiting", "Fatigue", "Sore Throat",
  "Itchy Eyes", "Watery Eyes", "Mucus", "Ear Pain", "Increased heart rate",
  "Hyperventilation", "Sweating", "Trembling", "Bleeding", "Discharge",
  "Insomnia", "Agitation", "Depression", "Anxiety", "Paranoia", "Hallucination"
]

# diseases database (dictionary)
diagnosis_database = {
  "acute Bronchitis": ['Cough', 'Mucus'],
  "allergy": ['Runny nose', 'Sneezing', 'Itchy Eyes', 'Watery Eyes'],
  "anxiety": ['Increased heart rate', 'Hyperventilation', 'Sweating', 'Trembling'],
  "brain Cancer": ['Headache', 'Blurred vision'],
  "chlamydia": ['Bleeding', 'Discharge'],
  "COVID-19": ['Fever', 'Sore throat', 'Runny nose'],
  "depression": ['Fatigue', 'Insomnia', 'Agitation'],
  "diarrhea": ['Fever', 'Cramps', 'Bloating', 'Nausea', 'Vomiting'],
  "ear infection": ['Fever', 'Ear Pain'],
  "endometriosis": ['Stomach ache', 'Bleeding'],
  "fibromyalgia": ['Fatigue', 'Depression', 'Anxiety', 'Insomnia', 'Headache'],
  "flu": ['Fever', 'Cough', 'Runny nose'],
  "lupus": ['Fatigue', 'Fever'],
  "lyme disease": ['Fever', 'Fatigue', 'Headache'],
  "mononucleosis": ['Fatigue', 'Fever', 'Sore Throat', 'Headache'],
  "pink eye": ['Runny nose', 'Blurred vision'],
  "pneumonia": ['Cough', 'Fatigue', 'Fever', 'Nausea', 'Vomiting'],
  "schizophrenia": ['Anxiety', 'Paranoia', 'Hallucination'],
}

#array that includes treatment advice


treatment_database = {
  "acute Bronchitis": "Get plenty of rest! Drink fluids but avoid caffeine and alcohol. Bring a humidifier into your house. If the symptoms are too painful pain relievers and fever reducers, such as acetaminophen (Tylenol).",
  "allergy": "Go to the doctor, try saline nasal irrigation, use an air filter indoors",
  "anxiety": "Try arranging a meeting with a therapist, visit the doctor for Anti-anxiety medications, listen to calming music, take leisurely walks outside",
  "brain Cancer": "Visit the doctor right away",
  "chlamydia": "Visit the doctor to see what medication you need",
  "COVID-19": "Go to bed early, drink lots of warm water, Take advil in moderation if you have muscle pain",
  "depression": "Visit a doctor for medication, Try arranging a meeting with a therapist, listen to music, take walks outside",
  "diarrhea": "Drink plenty of liquids, including water, broths and juices. Avoid caffeine and alcohol. Add semisolid and low-fiber foods gradually as your bowel movements return to normal. Try soda crackers, toast, eggs, rice or chicken.",
  "ear infection": "Take antibiotics so that the infection doesn't spread to other parts of the body",
  "endometriosis": "Effective treatments such as hormones and excision surgery can help, staying hydrated and putting a heating pad in the uterus area",
  "fibromyalgia": "Relax your body by stretching daily and going to physical therapy",
  "flu": "Get plenty of rest, drink lots of water, and if you feel pain, take pain relievers",
  "lupus": "Take care of your skin by wearing plenty of sun block and keeping skin safe by wearing sun protective clothes",
  "lyme disease": "Take oral and Intravenous antibiotics",
  "mononucleosis": "Get plenty of rest and take antiflammatory drugs",
  "pink eye":"Use artificial tears, clean your eyelids with a wet cloth, and apply cold or warm compresses several times daily. ",
  "pneumonia": "Mild pneumonia can usually be treated at home with rest, antibiotics (if it's likely be caused by a bacterial infection) and by drinking plenty of fluids. More severe cases may need hospital treatment.",
  "schizophrenia": "Treatment with medications and psychosocial therapy can help manage the condition. In some cases, hospitalization may be needed. A psychiatrist experienced in treating schizophrenia usually guides treatment.",
}

#connect user input with algorithm 

def get_symptoms():
    return symptoms_database

def get_all_diagnosis():
    return diagnosis_database

def get_treatment(): 
    return treatment_database

def get_diagnosis(user_symptoms):
    
    # initialize match result for all sicknesses
    match_result_array = [0] * 18

    # iterate through each symptom in each disease
    match_disease_index = 0
    max_match_result = 0
    max_match_result_disease = ""
    max_match_result_treatment = ""
    max_match_result_report = ""
    max_match_result_medical_website = medical_website

    for key, values in diagnosis_database.items():
        for value in values:
            for i in user_symptoms:
                user_symptom = symptoms_database[i]
                if value == user_symptom:
                    match_result_array[match_disease_index] = match_result_array[match_disease_index] + 1
                    break
        if match_result_array[match_disease_index] > max_match_result:
            max_match_result = match_result_array[match_disease_index]
            max_match_result_disease = key
        match_disease_index = match_disease_index + 1
    
    for key, value in treatment_database.items(): 
      if key == max_match_result_disease:
        max_match_result_treatment = value 
        break 
    
    max_match_result_report = "Based on your current symptoms, your mostly likely sickness is the " + max_match_result_disease + ". We advise you to " + max_match_result_treatment
    return max_match_result_report, max_match_result_medical_website

report, website = get_diagnosis(user_symptoms)

print(report)
print("Check out this link to learn more: " + website)