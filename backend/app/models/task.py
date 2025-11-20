# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship

# Base = declarative_base()

# class Task(Base):
#     __tablename__ = 'tasks'

#     id = Column(Integer, primary_key=True)
#     title = Column(String, nullable=False)
#     description = Column(String, nullable=True)
#     owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # ForeignKey до таблиці User

#     user = relationship("User", back_populates="tasks")
