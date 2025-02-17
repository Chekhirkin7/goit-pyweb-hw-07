from conf.db import session
from conf.models import Group, Student


def main():
    sub = session.query(Student.fullname, Group.name).join(Group).where(Group.name == 'Group-A').all()
    for s in sub:
        columns = ['fullname', 'group']
        r = [dict(zip(columns, s))]
        print(r)

if __name__ == '__main__':
    main()
