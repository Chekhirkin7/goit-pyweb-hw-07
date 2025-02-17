from conf.db import session
from conf.models import Student, Grade

from sqlalchemy import func, cast, Float, desc


def get_students_with_high_average():
    students = session.query(Student.fullname, cast(func.round(func.avg(Grade.grade), 2), Float).label('average_grade')).join(Grade).group_by(
        Student.id).order_by(desc('average_grade')).limit(5).all()
    for s in students:
        columns = ['fullname', 'average_grade']
        r = [dict(zip(columns, s))]
        print(r)

if __name__ == '__main__':
    get_students_with_high_average()