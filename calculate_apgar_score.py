def calculate_apgar_score(appearance, pulse, grimace, activity, respiration):
    score = 0

    # Appearance
    if appearance == "pink":
        score += 2
    elif appearance == "blue":
        score += 1

    # Pulse
    if pulse >= 100:
        score += 2
    elif pulse < 100 and pulse >= 60:
        score += 1

    # Grimace (reflex irritability)
    if grimace == "cough/sneeze" or grimace == "active motion":
        score += 2
    elif grimace == "grimace":
        score += 1

    # Activity (muscle tone)
    if activity == "active motion":
        score += 2
    elif activity == "some flexion of extremities":
        score += 1

    # Respiration
    if respiration >= 30:
        score += 2
    elif respiration < 30 and respiration >= 0:
        score += 1

    return score


# Get input from the user
appearance = input("Enter the appearance (pink/blue): ")
pulse = int(input("Enter the pulse rate: "))
grimace = input("Enter the grimace (cough/sneeze/active motion/grimace): ")
activity = input("Enter the activity (active motion/some flexion of extremities): ")
respiration = int(input("Enter the respiration rate: "))

# Calculate the APGAR score
apg_score = calculate_apgar_score(appearance, pulse, grimace, activity, respiration)

# Display the APGAR score
print("The APGAR score is:", apg_score)
