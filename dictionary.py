dictionary = {
    'key': 'value',
    'another_key': 'another_value'
}

universities = [
    {
        'name': 'Oxford',
        'country': 'United Kingdom',
        'students': (2000, 3000)
    },
    {
        'name': 'Harvard',
        'country': 'United States',
        'students': (2000, 1500)
    },
    {
        'name': 'Stanford',
        'country': 'United States',
        'students': (4200, 3000)
    }
]

total_students = sum(universities[0]['students'])
print(total_students)
