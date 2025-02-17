from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)
    group_id = Column(ForeignKey('groups.id', ondelete='Cascade', onupdate='Cascade'))
    group = relationship('Group', backref='student')


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(120), nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    teacher_id = Column(ForeignKey('teachers.id', ondelete='Cascade', onupdate='Cascade'))
    teacher = relationship('Teacher', backref='disciplines')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    grade_date = Column(Date, nullable=False)
    student_id = Column(ForeignKey('students.id', ondelete='Cascade', onupdate='Cascade'))
    subject_id = Column(ForeignKey('subjects.id', ondelete='Cascade', onupdate='Cascade'))
    student = relationship('Student', backref='grade')
    subject = relationship('Subject', backref='grade')