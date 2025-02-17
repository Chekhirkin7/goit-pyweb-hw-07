from conf.db import session
from conf.models import Group, Subject, Grade, Student
from sqlalchemy.sql import and_


def main():
    sub = session.query(Group.name, Subject.name, Grade.grade).join(Student, Student.id == Grade.student_id).join(Group, Group.id == Student.group_id).join(Subject, Subject.id == Grade.subject_id).where(and_(Group.name == 'Group-A', Subject.name == 'English')).all()
    for s in sub:
        columns = ['grade', 'group', 'subject']
        r = [dict(zip(columns, s))]
        print(r)

if __name__ == '__main__':
    main()
