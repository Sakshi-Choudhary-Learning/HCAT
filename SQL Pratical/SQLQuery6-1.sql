
--CREATE TABLE Students (
--    StudentID INT PRIMARY KEY,
--    Name VARCHAR(50) NOT NULL,
--    Age INT,
--    City VARCHAR(50),
--    AdmissionDate DATE
--);


INSERT INTO Students (StudentID, Name, Age, City, AdmissionDate)
VALUES 
(1, 'Sakshi', 23, 'Pune', '2024-06-01'),
(2, 'Neha', 24, 'Mumbai', '2024-06-05'),
(3, 'Swapna', 22, 'Hyderabad', '2024-06-10'),
(4, 'Rahul', 25, 'Nashik', '2024-06-12'),
(5, 'Amit', 23, 'Nagpur', '2024-06-15');

select * from Students;

SELECT Name, City FROM Students;

SELECT * FROM Students WHERE Age > 22;

SELECT * FROM Students WHERE City = 'Pune';

SELECT * FROM Students ORDER BY Age ASC;

SELECT * FROM Students ORDER BY Name DESC;

SELECT COUNT(*) AS TotalStudents FROM Students;

SELECT AVG(Age) AS AvgAge FROM Students;

SELECT MIN(Age) AS Youngest FROM Students;

SELECT MAX(Age) AS Oldest FROM Students;

SELECT SUM(Age) AS TotalAge FROM Students;

--CREATE TABLE Department (
--    DepartmentID INT PRIMARY KEY,
--    DepartmentName VARCHAR(50)
--);

INSERT INTO Department VALUES
(101, 'Computer'),
(102, 'IT'),
(103, 'EXTC'),
(104, 'Mechanical'),
(105, 'Civil');

SELECT * FROM Department;
SELECT * FROM Students;

SELECT 
    Students.Name,
    Department.DepartmentName
FROM Students
LEFT JOIN Department
ON Students.StudentID = Department.DepartmentID;


SELECT 
    Students.Name,
    Department.DepartmentName
FROM Students
RIGHT JOIN Department
ON Students.StudentID = Department.DepartmentID;

SELECT 
    Students.Name,
    Department.DepartmentName
FROM Students
FULL OUTER JOIN Department
ON Students.StudentID = Department.DepartmentID;

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50) NOT NULL,
    Age INT,
    Salary DECIMAL(10,2),
    City VARCHAR(50)
);


--ALTER TABLE Employees
--ADD JoiningDate DATE;

EXEC sp_rename 'EmployeeDetails', 'Employees'; /*Msg 15225, Level 11, State 1, Procedure sp_rename, Line 636 [Batch Start Line 87]
No item by the name of 'Employees' could be found in the current database 'LearningDB', given that @itemtype was input as '(null)'.
*/ 
-- A to B, B to C can't B to A

-- DROP TABLE EmployeeDetails;


INSERT INTO EmployeeDetails (EmpID, EmpName, Age, Salary, City)
VALUES 
(1, 'Sakshi', 23, 45000, 'Pune'),
(2, 'Neha', 24, 50000, 'Mumbai'),
(3, 'Swapna', 25, 55000, 'Hyderabad'),
(4, 'Rahul', 26, 60000, 'Nashik'),
(5, 'Amit', 27, 48000, 'Nagpur');

UPDATE EmployeeDetails
SET Salary = 52000, City = 'Delhi'
WHERE EmpID = 2;

select * from EmployeeDetails;

SELECT EmpName, City FROM EmployeeDetails;

SELECT * FROM EmployeeDetails WHERE City = 'Pune';

SELECT * FROM EmployeeDetails ORDER BY Age DESC;

SELECT COUNT(*) AS TotalEmployees FROM EmployeeDetails;

SELECT AVG(Salary) AS AvgSalary FROM EmployeeDetails;

SELECT MIN(Salary), MAX(Salary) FROM EmployeeDetails;

SELECT City, COUNT(*) AS TotalPeople
FROM EmployeeDetails
GROUP BY City;

ALTER TABLE EmployeeDetails
DROP COLUMN JoiningDate;













