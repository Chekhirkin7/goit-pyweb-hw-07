from conf.db import session
from conf.models import Subject, Student, Grade, Teacher
from sqlalchemy import and_


def main():
    sub = session.query(Student.fullname, Teacher.fullname, Subject.name).join(Grade, Grade.student_id == Student.id).join(Subject, Subject.id == Grade.subject_id).join(Teacher, Teacher.id == Subject.teacher_id).where(and_(Teacher.fullname == 'Козак Софія Давидівна', Student.fullname == 'Верес Гаврило Богданович')).group_by(Subject.name, Student.fullname, Teacher.fullname).all()
    for s in sub:
        columns = ['student', 'teacher', 'subject']
        r = [dict(zip(columns, s))]
        print(r)


if __name__ == '__main__':
    main()
