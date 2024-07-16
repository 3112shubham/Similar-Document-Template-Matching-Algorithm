import pandas as pd
import numpy as np

def generate_claim_data(num_claims):
  data = []
  for _ in range(num_claims):
    id = np.random.randint(10000,99999)
    age = np.random.randint(1,100)
    gender = np.random.randint(1,3)
    location = np.random.randint(1,16)
    Medical_history = np.random.randint(1,7)
    policy_type = np.random.randint(1,7)
    dependents = (np.random.randint(1,6))-1
    procedure = np.random.randint(10000,100000)
    diagnosis_codes = np.random.randint(1,10)
    treatment_cost = np.random.randint(300, 12000)
    date_of_service = str(np.random.randint(1,29))+"/"+str(np.random.randint(1,13))+"/"+str(np.random.randint(2000,2024))
    place_of_service=np.random.randint(1,7)
    Provider_ID = np.random.randint(4389,4598)
    specialization=(Provider_ID%13)+1
    # Add more features and logic for generating fraudulent claims (optional)
    fraudulent = np.random.choice(["No", "Yes"], p=[0.3, 0.7])  # 90% not fraudulent, 10% maybe fraudulent
    data.append({"PolicyHolder ID": id,
                  "Age": age,
                  "Gender": int(gender),
                  "Location": location,
                  "Medical History": Medical_history,
                  "Policy Type": policy_type,
                  "Dependents": dependents,
                  "Procedure Code":procedure,
                  "Diagnosis Codes": diagnosis_codes,
                  "Treatment Cost":treatment_cost,
                  "Date of Service":date_of_service,
                  "Place Of Service":place_of_service,
                  "Provider ID":Provider_ID,
                  "Specialization":specialization,
                  "Fraudulent": fraudulent})
  return pd.DataFrame(data)

# Generate 1000 dummy claims (adjust as needed)
data = generate_claim_data(1000)

data.to_csv('data.csv',index = False)