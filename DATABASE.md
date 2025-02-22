**Users:**
  
  - id (Primary Key)
  - username
  - email
  - role (student, teacher)
  - password

**Tests:**

  - id (Primary Key)
  - title
  - created_by (ForeignKey to User)
  - time_limit

**Questions:**

  - id (Primary Key)
  - test (ForeignKey to Test)
  - question_text
  - question_type (MCQ, written)
  - options (JSON for multiple choice)
  - correct_answer
