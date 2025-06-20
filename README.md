#    Regestration_check_up

# 🎓 Student Information Analyzer

A command-line tool developed in Python to manage and update student details from a CSV file. Designed for schools or educational institutions to maintain and review student information efficiently.

---

## 📂 Features

- Reads student data from a CSV file using the Admission Number as the unique identifier.
- Displays full student details with an easy lookup.
- Allows editing of fields like:
  - Student's Name
  - Parents’ Names
  - Date of Birth
  - Aadhar Number
  - Gender, Caste
  - Contact and Income Details
  - Only Child and PwD (Persons with Disabilities) status
- Saves updates in real-time after user confirmation.
- Keeps the user in control with repeated prompts and confirmations.

---

## ⚙️ Technologies Used

- Python
- pandas 🐼
- numpy 🔢

---

## 🗂️ How to Run

1. Clone or download the script.
2. Make sure your CSV file is updated with accurate headers and student data.
3. Update the file path here in the script:

   ```python
   sheet = pd.read_csv(r"C:\\Users\\YourUsername\\Path\\to\\your\\CSVfile.csv", index_col='Admission Number')
