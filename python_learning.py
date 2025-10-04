"""A simple Python learning module demonstrating boolean variables."""

import grade_average_service as grade_service

homework_assignment_grades = {
    "homework_1": 85,
    "homework_2": 92,
    "homework_3": 78,
    "homework_4": 88,
}


grade_service.calculate_homework(homework_assignment_grades)
