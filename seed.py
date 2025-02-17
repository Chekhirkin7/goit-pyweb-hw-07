import random
from random import randint
from faker import Faker
from sqlalchemy.exc import SQLAlchemyError
from conf.db import session
from conf.models import Student, Group, Grade, Teacher, Subject

fake = Faker('uk_UA')


def insert_teachers():
    for _ in range(4):
        teacher = Teacher(
            fullname=fake.full_name()
        )
        session.add(teacher)


def insert_groups():
    groups_name = ['Group-A', 'Group-B', 'Group-C']
    for i in groups_name:
        group = Group(
            name=i
        )
        session.add(group)


def insert_students():
    groups_sel = session.query(Group).all()
    for _ in range(35):
        student = Student(
            fullname=fake.full_name(),
            group_id=random.choice(groups_sel).id
        )
        session.add(student)


def insert_subjects():
    teachers_sel = session.query(Teacher).all()
    subjects_name = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography']
    for i in subjects_name:
        subject = Subject(
            name=i,
            teacher_id=random.choice(teachers_sel).id
        )
        session.add(subject)


def insert_grades():
    students_sel = session.query(Student).all()
    subjects_sel = session.query(Subject).all()
    for _ in range(35):
        for _ in range(17):
            grd = Grade(
                grade=randint(50, 100),
                grade_date=fake.date_this_year(),
                student_id=random.choice(students_sel).id,
                subject_id=random.choice(subjects_sel).id
            )
            session.add(grd)

if __name__ == '__main__':
    try:
        insert_teachers()
        insert_groups()
        session.commit()
        insert_students()
        insert_subjects()
        session.commit()
        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()