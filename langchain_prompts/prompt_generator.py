from langchain_core.prompts import PromptTemplate

# template
template = PromptTemplate(
    template="""
You are an experienced CBSE curriculum designer and educator.

Generate a structured worksheet based on the following inputs:

Grade: {GRADE}
Subject: {SUBJECT}
Chapter/Topic: {TOPIC}
Difficulty Level: {DIFFICULTY}
Number of Questions: {NUMBER_OF_QUESTIONS}
Learning Objective (optional): {OBJECTIVE}

---

### 📘 CBSE Alignment Requirements:
Ensure the worksheet strictly follows CBSE guidelines:
1. Align with NCERT concepts and terminology.
2. Cover a mix of competencies:
   - Knowledge (recall-based)
   - Understanding (conceptual clarity)
   - Application (real-life/problem-solving)
   - Higher Order Thinking Skills (HOTS)
3. Include competency-based questions as per NEP 2020:
   - Case-based questions
   - Assertion-Reason questions (if applicable)
4. Follow CBSE question patterns:
   - Very Short Answer (1 mark)
   - Short Answer (2–3 marks)
   - Long Answer (4–5 marks)
5. Maintain age-appropriate language and clarity.
6. Avoid ambiguity and ensure questions are unambiguous.
7. Include real-world/contextual examples wherever possible.

---

### 📄 Worksheet Structure:

#### Section A: Very Short Answer (1 mark each)
- Multiple questions

#### Section B: Short Answer (2–3 marks each)
- Multiple questions

#### Section C: Long Answer (4–5 marks each)
- Multiple questions

#### Section D: Case-Based / Competency-Based Questions
- Include 1–2 passages/scenarios followed by 3–5 questions each

#### Section E: Higher Order Thinking Skills (HOTS)
- Include 2–3 challenging analytical questions

---

### 📝 Additional Requirements:
- Provide answer key at the end.
- Ensure answers are crisp and CBSE-evaluation friendly.
- Use diagrams/tables where relevant (describe if needed).
- Keep formatting clean and printable.

---

### 🎯 Output Format:
- Clearly formatted worksheet
- Proper section headings
- Numbered questions
- Separate Answer Key section

Generate the worksheet now.""",
input_variables=['GRADE', 'SUBJECT', 'TOPIC', 'DIFFICULTY', 'NUMBER_OF_QUESTIONS', 'OBJECTIVE'],
validate_template=True
)

template.save('template.json')