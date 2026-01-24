[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=22081748)

# Habit Tracker – End-of-Semester Lab Test (Introduction to Programming)

This repository provides the required structure for the end-of-semester lab assignment.  
Use **`app.py`** for the application logic and **`tests.py`** for the unit tests. You may add additional files if needed.

---

## 📌 Assignment Overview

Create a Python program that:

- Asks users questions about their **weekly healthy habits and routines**.
- Computes a **score for each habit category** based on user responses.
- Interprets the total score for each category as **Low**, **Moderate**, or **High adherence**.
- Handles invalid inputs using exception handling.
- Includes at least one **unit test** for a calculation or interpretation function.

---

## 🧩 Functional Requirements

### Habit Quiz Structure
- The quiz contains **15 questions**.
- Each question belongs to one of the following categories:
  - **SleepRoutine**
  - **PhysicalActivity**
  - **HealthyEating**
  - **Mindfulness**
  - **SocialConnection**
  
  *(You may choose different categories if desired.)*

- Each question asks the user how many days per week (**0–7**) they engage in a specific habit or behavior.

---

### Scoring
- Each answer contributes to a **total score** for its category.
- The score for each category is the **sum of all responses** associated with that habit category.

---

### Interpretation

Interpretation is based on the **total score** for each category:

| Score Range       | Interpretation | Meaning |
|-------------------|----------------|---------|
| **≥ 12**          | High           | Strong adherence to healthy habits |
| **6–11**          | Moderate       | Partial/occasional adherence |
| **< 6**           | Low            | Insufficient healthy habits |

The interpretation logic must be implemented in a **pure function**, which will be **unit tested**.

---

## 🛠️ Output Requirements

Your program must:

- Display the **total score** for each habit category.
- Show the **interpretation** (High / Moderate / Low) for each category.

---

## ✔️ Input Validation

If the user enters invalid input:

- If the input is **non-numeric**, prompt them again.
- If the input is outside the valid range **0–7**, show an error and ask again.
- Use `try/except` to handle such cases without crashing the program.

---

## 🗂️ Data Structure

You may store questions using a **list of dictionaries**, or another suitable structure.

Each dictionary includes:

- `text`: The question text  
- `habit`: The associated habit category  

**Example:**

```python
items = [
    {"text": "How many days per week do you go to bed at a consistent hour?", "habit": "SleepRoutine"},
    {"text": "How many days per week do you eat at least one healthy meal?", "habit": "HealthyEating"},
    {"text": "How many days per week do you practice mindfulness or relaxation?", "habit": "Mindfulness"}
]
````

---

## 🧾 Non-Functional Requirements

Your code should:

* Be **modular** (use meaningful functions).
* Be **testable** through unit tests.
* Follow **good naming and writing conventions**.
* Handle errors properly, including invalid user input.

---

## 📝 Grading Criteria (Total: 9 points)

A minimum of **4 points** is required to pass.

| Criterion                                                                          | Points |
| ---------------------------------------------------------------------------------- | ------ |
| Runs without errors or warnings                                                    | 1      |
| Produces correct expected output                                                   | 1      |
| Contains at least one meaningful unit test                                         | 1      |
| Implements a requested live modification within 5 minutes                          | 3      |
| Answers questions about own code correctly (1 point/question, 1 minute per answer) | 3      |

Evaluation may occur during the **last lab session** or during **exam sessions**.

---

## 🧪 Example Input

```
How many days per week do you go to bed at a consistent hour? 5
How many days per week do you exercise for at least 20 minutes? 3
How many days per week do you eat at least one healthy meal? 6
How many days per week do you practice mindfulness? 2
How many days per week do you spend meaningful time with others? 4
...
```

---

## 🧾 Example Output

```
SleepRoutine: Score 5 → Low
PhysicalActivity: Score 7 → Moderate
HealthyEating: Score 13 → High
Mindfulness: Score 2 → Low
SocialConnection: Score 8 → Moderate
```

---


