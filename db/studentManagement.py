from datetime import datetime
from db.database import SessionLocal, Student, Service, Parent, Season


class StudentManagement:
    def __init__(self):
        # Initialize the database session
        self.db = SessionLocal()

    def add_student(self, student_data, services_data, parent_data):
        """Add a new student along with services and parent details."""
        try:
            # Create a new student object
            student = Student(
                student_no=student_data["student_no"],
                first_name=student_data["first_name"],
                last_name=student_data["last_name"],
                tc_no=student_data["tc_no"],
                birth_date=datetime.strptime(student_data["birth_date"], "%Y-%m-%d"),
                gender=student_data["gender"],
                status=student_data["status"],
                address=student_data["address"],
                class_level=student_data["class_level"],
                registration_date=datetime.strptime(
                    student_data["registration_date"], "%Y-%m-%d"
                ),
                registration_type=student_data["registration_type"],
                email=student_data["email"],
                city=student_data["city"],
                district=student_data["district"],
                phone=student_data["phone"],
                notes=student_data["notes"],
                total_debt=student_data["total_debt"],
                total_paid=student_data["total_paid"],
                total_unpaid=student_data["total_unpaid"],
            )

            self.db.add(student)
            self.db.commit()
            self.db.refresh(student)

            # Add services related to the student
            self._add_services(student.id, services_data)

            # Add parent information
            self._add_parent(student.id, parent_data)

            self.db.commit()  # Commit everything
        except Exception as e:
            self.db.rollback()  # Rollback in case of an error
            raise Exception(f"Error while adding student: {e}")

    def _add_services(self, student_id, services_data):
        """Helper function to add service records for the student."""
        for service_data in services_data:
            service = Service(
                student_id=student_id,
                total_fee=service_data["total_fee"],
                publication_fee=service_data["publication_fee"],
                registration_fee=service_data["registration_fee"],
            )
            self.db.add(service)

    def _add_parent(self, student_id, parent_data):
        """Helper function to add parent details for the student."""
        parent = Parent(
            student_id=student_id,
            anne_adi=parent_data["anne_adi"],
            anne_soyadi=parent_data["anne_soyadi"],
            anne_meslek=parent_data["anne_meslek"],
            anne_tel=parent_data["anne_tel"],
            baba_adi=parent_data["baba_adi"],
            baba_soyadi=parent_data["baba_soyadi"],
            baba_meslek=parent_data["baba_meslek"],
            baba_tel=parent_data["baba_tel"],
        )
        self.db.add(parent)

    def remove_student_by_tcno(self, student_tcno):
        """Remove a student by their TC number."""
        try:
            student = (
                self.db.query(Student).filter(Student.tc_no == student_tcno).first()
            )
            if student:
                self.db.delete(student)
                self.db.commit()
            else:
                raise ValueError(f"No student found with TC number: {student_tcno}")
        except Exception as e:
            raise Exception(f"Error while removing student: {e}")

    def update_student(self, student_tcno, student_data):
        """Update a student's details based on TC number."""
        try:
            student = (
                self.db.query(Student).filter(Student.tc_no == student_tcno).first()
            )
            if student:
                for key, value in student_data.items():
                    setattr(student, key, value)
                self.db.commit()
                self.db.refresh(student)
            else:
                raise ValueError(f"No student found with TC number: {student_tcno}")
        except Exception as e:
            raise Exception(f"Error while updating student: {e}")

    def get_students(self):
        """Retrieve a list of all students."""
        return self.db.query(Student).all()

    def close(self):
        """Close the session after use."""
        self.db.close()
