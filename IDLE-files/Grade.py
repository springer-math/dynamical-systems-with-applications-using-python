def Grade(score):
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
