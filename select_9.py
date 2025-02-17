from conf.db import session
from conf.models import Subject, Student, Grade
from sqlalchemy import func, cast, Float


def main():
    sub = session.query(Student.fullname, Subject.name).join(Grade, Grade.student_id == Student.id).join(Subject, Subject.id == Grade.subject_id).where(Student.fullname == 'Верес Гаврило Богданович').group_by(Student.id, Subject.name).all()
    for s in sub:
        columns = ['fullname', 'subject']
        r = [dict(zip(columns, s))]
        print(r)


if __name__ == '__main__':
    main()
