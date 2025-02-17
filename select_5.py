from conf.db import session
from conf.models import Subject, Teacher


def main():
    sub = session.query(Subject.name, Teacher.fullname).join(Teacher).where(Teacher.fullname == 'Козак Софія Давидівна').all()
    for s in sub:
        columns = ['subjects', 'fullname']
        r = [dict(zip(columns, s))]
        print(r)

if __name__ == '__main__':
    main()
