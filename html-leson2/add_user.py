from app import *


def add_user_data(name, age, city, educations):
    user = User(name=name, age=age, city=city)
    db.session.add(user)
    db.session.commit()

    for edu in educations:
        education = Education(
            institution=edu['institution'],
            graduation_year=edu['graduation_year'],
            link=edu['link'],
            user=user
        )
        db.session.add(education)

    db.session.commit()


educations = [
    {'institution': 'РАНХиГС', 'graduation_year': 2022, 'link': 'https://www.ranepa.ru/'},
    {'institution': 'НОВГУ (Информатика и вычислительная техника)', 'graduation_year': 2024,
     'link': 'https://www.novsu.ru/'},
    {'institution': 'НЕТОЛОГИЯ', 'graduation_year': 2023, 'link': 'https://netology.ru/'},
    {'institution': 'Школа 21 (Сбер)', 'graduation_year': None, 'link': 'https://21-school.ru/'}
]

db.create_all()
add_user_data('Сидоренко Владимир Сергеевич', 22, 'Великий Новгород', educations)
