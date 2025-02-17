from conf.db import session
from conf.models import Student, Grade, Subject

from sqlalchemy import func, cast, Float, desc


def get_student_with_high_average_for_subject():
    student = session.query(Student.fullname, cast(func.round(func.avg(Grade.grade), 2), Float).label('average_grade'),
                            Subject.name).join(Grade, Grade.student_id == Student.id).join(Subject, Subject.id == Grade.subject_id).where(Subject.name == 'Biology').group_by(
        Student.id, Subject.name).order_by(desc("average_grade")).limit(1).all()
    for s in student:
        columns = ['fullname', 'average_grade', 'subject']
        r = [dict(zip(columns, s))]
        print(r)

if __name__ == '__main__':
    get_student_with_high_average_for_subject()