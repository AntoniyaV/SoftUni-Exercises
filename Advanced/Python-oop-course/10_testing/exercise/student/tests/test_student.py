from project.student import Student
import unittest


class StudentTests(unittest.TestCase):
    def setUp(self):
        courses = {"math": ["math notes", "more math"], "bio": ["bio notes", "more bio"]}
        self.student = Student("Anna", courses)

    def test_student_init__when_courses_are_none_expect_courses_to_be_empty_dict(self):
        student = Student("Anna")
        self.assertEqual("Anna", student.name)
        self.assertEqual({}, student.courses)

    def test_student_init__when_courses_are_not_none_expect_courses_to_be_filled(self):
        expected_courses = {"math": ["math notes", "more math"], "bio": ["bio notes", "more bio"]}
        self.assertEqual("Anna", self.student.name)
        self.assertEqual(expected_courses, self.student.courses)

    def test_student_enroll__when_course_already_in_courses_expect__msg_and_updated_notes(self):
        expected_msg = "Course already added. Notes have been updated."
        actual_msg = self.student.enroll("math", ["more", "and more"])
        self.assertEqual(expected_msg, actual_msg)

        expected_courses = {"math": ["math notes", "more math", "more", "and more"], "bio": ["bio notes", "more bio"]}
        actual_courses = self.student.courses
        self.assertEqual(expected_courses, actual_courses)

    def test_student_enroll__when_course_not_in_courses_and_add_notes_is_y_expect_msg_and_added_course_with_notes(
            self):
        expected_msg = "Course and course notes have been added."
        actual_msg = self.student.enroll("chem", ["chem notes", "more chem"], "Y")
        self.assertEqual(expected_msg, actual_msg)

        expected_courses = {"math": ["math notes", "more math"],
                            "bio": ["bio notes", "more bio"],
                            "chem": ["chem notes", "more chem"]
                            }
        actual_courses = self.student.courses
        self.assertEqual(expected_courses, actual_courses)

    def test_student_enroll__when_course_not_in_courses_and_add_notes_is_empty_expect_msg_and_added_course_with_notes(
            self):
        expected_msg = "Course and course notes have been added."
        actual_msg = self.student.enroll("chem", ["chem notes", "more chem"])
        self.assertEqual(expected_msg, actual_msg)

        expected_courses = {"math": ["math notes", "more math"],
                            "bio": ["bio notes", "more bio"],
                            "chem": ["chem notes", "more chem"]
                            }
        actual_courses = self.student.courses
        self.assertEqual(expected_courses, actual_courses)

    def test_student_enroll__when_course_not_in_courses_and_add_notes_is_not_y_or_empty_expect_msg_and_added_course_without_notes(
            self):
        expected_msg = "Course has been added."
        actual_msg = self.student.enroll("chem", ["chem notes", "more chem"], "N")
        self.assertEqual(expected_msg, actual_msg)

        expected_courses = {"math": ["math notes", "more math"],
                            "bio": ["bio notes", "more bio"],
                            "chem": []
                            }
        actual_courses = self.student.courses
        self.assertEqual(expected_courses, actual_courses)

    def test_student_add_notes__when_course_already_in_courses_expect__msg_and_updated_notes(self):
        expected_msg = "Notes have been updated"
        actual_msg = self.student.add_notes("math", "more")
        self.assertEqual(expected_msg, actual_msg)

        expected_courses = {"math": ["math notes", "more math", "more"], "bio": ["bio notes", "more bio"]}
        actual_courses = self.student.courses
        self.assertEqual(expected_courses, actual_courses)

    def test_student_add_notes__when_course_not_in_courses_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("chem", "notes")

        expected_msg = "Cannot add notes. Course not found."
        actual_msg = str(ex.exception)
        self.assertEqual(expected_msg, actual_msg)

    def test_student_leave_course__when_course_already_in_courses_expect__msg_and_remove_course_from_courses(self):
        expected_msg = "Course has been removed"
        actual_msg = self.student.leave_course("math")
        self.assertEqual(expected_msg, actual_msg)

        expected_courses = {"bio": ["bio notes", "more bio"]}
        actual_courses = self.student.courses
        self.assertEqual(expected_courses, actual_courses)

    def test_student_leave_course__when_course_not_in_courses_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("chem")

        expected_msg = "Cannot remove course. Course not found."
        actual_msg = str(ex.exception)
        self.assertEqual(expected_msg, actual_msg)


if __name__ == "__main__":
    unittest.main()
