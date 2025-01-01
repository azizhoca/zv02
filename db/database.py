from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Database configuration
DATABASE_URL = "sqlite:///herikli.db"

# Create SQLAlchemy engine and session factory
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)  # SQLite specific option
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the models
Base = declarative_base()

# Models definition


class Season(Base):
    __tablename__ = "seasons"
    id = Column(Integer, primary_key=True, index=True)
    season_name = Column(String)
    season_start = Column(Integer)
    students = relationship("Student", back_populates="season")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_no = Column(String, unique=True, index=True)  # Unique student number
    first_name = Column(String)  # First name of the student
    last_name = Column(String)  # Last name of the student
    tc_no = Column(String, unique=True, index=True)  # Turkish ID number
    birth_date = Column(Date)  # Date of birth
    gender = Column(Integer)  # Gender: 0 = Female, 1 = Male
    status = Column(Integer)  # Status: 0 = Inactive, 1 = Active
    address = Column(String)  # Address
    class_level = Column(Integer)  # Class level (index + 2)
    registration_date = Column(Date)  # Date of registration
    registration_type = Column(Integer)  # 0 = New, 1 = Renewal, 2 = Transfer
    email = Column(String)  # Email address
    phone = Column(String)  # Phone number
    notes = Column(String)  # Additional notes
    total_debt = Column(Float)  # Total debt
    total_paid = Column(Float)  # Total paid
    total_unpaid = Column(Float)  # Total unpaid

    season_id = Column(Integer, ForeignKey("seasons.id"))

    season = relationship("Season", back_populates="students")  # Relationship to Season

    # Relationships
    services = relationship(
        "Service", back_populates="student", cascade="all, delete-orphan"
    )
    parent = relationship(
        "Parent", back_populates="student", uselist=False, cascade="all, delete-orphan"
    )


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    publication_fee = Column(Float)  # Publication fee
    registration_fee = Column(Float)  # Registration fee
    total_fee = Column(Float)  # Total fee for the services

    # Relationship to Student
    student = relationship("Student", back_populates="services")


class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    anne_adi = Column(String)  # Mother's first name
    anne_soyadi = Column(String)  # Mother's last name
    anne_meslek = Column(String)  # Mother's profession
    anne_tel = Column(String)  # Mother's phone number
    baba_adi = Column(String)  # Father's first name
    baba_soyadi = Column(String)  # Father's last name
    baba_meslek = Column(String)  # Father's profession
    baba_tel = Column(String)  # Father's phone number

    # Relationship to Student
    student = relationship("Student", back_populates="parent")


# Initialize the database (create tables)
def init_db():
    """Create the database tables if they don't exist."""
    Base.metadata.create_all(bind=engine)
