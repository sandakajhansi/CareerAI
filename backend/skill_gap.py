def analyze_skill_gap(student):

    required_skills = {
        "Python": 8,
        "SQL": 8,
        "Machine Learning": 7,
        "Power BI": 8
    }

    current_skills = {
        "Python": student.python,
        "SQL": student.sql,
        "Machine Learning": student.machine_learning,
        "Power BI": student.power_bi
    }

    skill_gap = {}

    for skill, required in required_skills.items():
        current = current_skills[skill]

        if current < required:
            skill_gap[skill] = {
                "current": current,
                "required": required,
                "gap": required - current
            }

    return {
        "career": student.career_goal,
        "skill_gap": skill_gap
    }