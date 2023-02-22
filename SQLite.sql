-- create students table
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(50)
);

-- create courses table
CREATE TABLE courses (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  instructor VARCHAR(50)
);

-- create registeredcourses table
CREATE TABLE registeredcourses (
  student_id INT,
  course_id INT,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- insert student data
INSERT INTO students (id, name, email) VALUES 
  (1, 'Abdullah', 'abdullah@example.com'),
  (2, 'Jamil', 'jamil@example.com');

-- register students in courses
INSERT INTO registeredcourses (student_id, course_id) VALUES
  (1, 1), 
  (1, 2), 
  (2, 1), 
  (2, 2),
  (2, 3); 
SELECT * FROM students;
SELECT * FROM courses;

SELECT courses.name, courses.instructor FROM courses
JOIN registeredcourses ON courses.id = registeredcourses.course_id
JOIN students ON students.id = registeredcourses.student_id
WHERE students.name = 'Abdullah';

