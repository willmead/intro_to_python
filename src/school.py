grades = [{'Subject': 'Maths',
            'Grade': 99,
            'Topic': 'Shapes'
            },
            {
            'Subject': 'English',
            'Grade': 76,
            'Topic': 'Shakespeare'
            },
            {
            'Subject': 'Science',
            'Grade': 75,
            'Topic': 'Gravity'
            }]

print("Your school report:")
print()
for grade in grades:
    subject = grade['Subject']
    score = grade['Grade']
    topic = grade['Topic']

    print(f"Subject: {subject}")
    print(f"Topic: {topic}")
    print(f"Grade: {score}")

    print()
