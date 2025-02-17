from conf.db import session
from conf.models import Teacher, Grade, Subject
from sqlalchemy import func, cast, Float


def main():
    sub = session.query(Teacher.fullname, Subject.name,
                        cast(func.round(func.avg(Grade.grade), 2), Float).label('average_grade')).join(Subject,
                                                                                                       Subject.teacher_id == Teacher.id).join(
        Grade, Grade.subject_id == Subject.id).where(Teacher.fullname == 'Козак Софія Давидівна').group_by(Teacher.id, Subject.name).all()
    for s in sub:
        columns = ['fullname', 'group', 'subject']
        r = [dict(zip(columns, s))]
        print(r)


if __name__ == '__main__':
    main()
