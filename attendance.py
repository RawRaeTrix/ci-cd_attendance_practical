def mark_attendance(name, status):
    print(name, "is", status)

def attendance_report():
    students = ["Ayush", "Rahul", "Amit"]

    print("Student Attendance Report")

    for student in students:
        print(student, "- Present")

mark_attendance("Ayush", "Present")
attendance_report()
