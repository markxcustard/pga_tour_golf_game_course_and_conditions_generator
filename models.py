from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class GolfCourseResult(Base):
    __tablename__ = 'golf_course_results'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course = Column(String)
    crowd = Column(String)
    time_of_day = Column(String)
    tee = Column(String)
    pin = Column(String)
    wind_direction = Column(String)
    wind_speed = Column(String)
    green_firmness = Column(String)
    green_speed = Column(String)
    fringe_firmness = Column(String)
    fringe_speed = Column(String)
    fairway_firmness = Column(String)
    fairway_speed = Column(String)
    first_cut_firmness = Column(String)
    first_cut_length = Column(String)
    second_cut_firmness = Column(String)
    second_cut_length = Column(String)
    timestamp = Column(String)  # Change this to String

DATABASE_URL = 'sqlite:///golf_course_results.db'

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
