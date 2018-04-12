# A program to grade student results.
# Save file as grade.py.
# Run the Module (or type F5).

def grade(score):
    if score >= 70:
        letter = 'A'
    elif score >= 60:
        letter = 'B'
    elif score >= 50:
        letter = 'C'
    elif score >= 40:
        letter = 'D'
    else:
        letter = 'F'
    return letter
