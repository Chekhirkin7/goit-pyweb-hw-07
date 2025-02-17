from conf.db import session
from conf.models import Group, Subject, Grade, Student

from sqlalchemy import func, cast, Float, desc


def main():
    groups = session.query(Group.name, cast(func.round(func.avg(Grade.grade), 2), Float).label('average_grade'),
                           Subject.name).join(Student, Student.group_id == Group.id).join(Grade,
                                                                                          Grade.student_id == Student.id).join(
        Subject, Subject.id == Grade.subject_id).where(Subject.name == 'Biology').group_by(Group.id, Subject.name).all()
    for g in groups:
        columns = ['group', 'average_grade', 'subject']
        r = [dict(zip(columns, g))]
        print(r)


if __name__ == '__main__':
    main()
