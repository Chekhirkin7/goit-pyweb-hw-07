from conf.db import session
from conf.models import Grade

from sqlalchemy import func, cast, Float


def main():
    groups = session.query(cast(func.round(func.avg(Grade.grade), 2), Float).label('average_grade')).scalar()
    print(groups)


if __name__ == '__main__':
    main()
