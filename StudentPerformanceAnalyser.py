student_records = {}

#Add a new student record with their subject marks.
def add_student(student_id, subjects_marks):
    if student_id in student_records:
        print(f"Student ID {student_id} already exists.")
    else:
        student_records[student_id] = subjects_marks
        print(f"Student ID {student_id} added successfully.")

#Update an existing student record.
def update_student(student_id, subjects_marks):
    if student_id in student_records:
        student_records[student_id] = subjects_marks
        print(f"Student ID {student_id} updated successfully.")
    else:
        print(f"Student ID {student_id} not found.")

#Delete a student record.
def delete_student(student_id):
    if student_id in student_records:
        del student_records[student_id]
        print(f"Student ID {student_id} deleted successfully.")
    else:
        print(f"Student ID {student_id} not found.")

#Calculate the total marks for a student.
def calculate_total_marks(student_id):
    if student_id in student_records:
        total_marks = sum(student_records[student_id].values())
        return total_marks
    else:
        print(f"Student ID {student_id} not found.")
        return None

#Calculate the percentage for a student.
def calculate_percentage(student_id):
    if student_id in student_records:
        total_marks = calculate_total_marks(student_id)
        num_subjects = len(student_records[student_id])
        if total_marks is not None:
            return (total_marks / (num_subjects * 100)) * 100
    else:
        print(f"Student ID {student_id} not found.")
        return None

#Calculate and display the rank of students based on total marks.
def calculate_rank():
    student_scores = []
    
    for student_id in student_records:
        total_marks = calculate_total_marks(student_id)
        if total_marks is not None:
            student_scores.append((student_id, total_marks))

    student_scores.sort(key=lambda x: x[1], reverse=True)

    print("Student Ranks:")
    rank = 1
    for student_id, total_marks in student_scores:
        percentage = calculate_percentage(student_id)
        print(f"Rank {rank}: Student ID {student_id}, Total Marks: {total_marks}, Percentage: {percentage:.2f}%")
        rank += 1

#Display individual student information.
def display_student(student_id):
    if student_id in student_records:
        total_marks = calculate_total_marks(student_id)
        percentage = calculate_percentage(student_id)
        print(f"Student ID {student_id}:")
        print(f"  Subject Marks: {student_records[student_id]}")
        print(f"  Total Marks: {total_marks}")
        print(f"  Percentage: {percentage:.2f}%")
    else:
        print(f"Student ID {student_id} not found.")

# Example usage
if __name__ == "__main__":
    add_student("S001", {"Math": 85, "English": 78, "Science": 92})
    add_student("S002", {"Math": 90, "English": 85, "Science": 88})
    add_student("S003", {"Math": 78, "English": 80, "Science": 70})

    update_student("S001", {"Math": 88, "English": 80, "Science": 94})

    display_student("S001")

    calculate_rank()

    delete_student("S002")

    calculate_rank()
