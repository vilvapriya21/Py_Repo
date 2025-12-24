from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float,Date

Base = declarative_base()
class Employee(Base):
    __tablename__ = 'employee'

    emp_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    salary = Column(Float, nullable=False)
    dob = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Employee id={self.emp_id}, name='{self.name}', salary={self.salary}, dob={self.dob}>"
# class Employee(Base):
#     __tablename__='employee'
#
#     emp_id=Column(Integer,primary_key=True)
#     name=Column(String)
#     salary=Column(Float)
#     dob=Column(Date)