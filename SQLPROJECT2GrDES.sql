SELECT * FROM grades;
select * from classes;
select * from scores;
select * from users;
select * from students;
ALTER TABLE classes ADD COLUMN subject VARCHAR;
ALTER TABLE classes
ADD COLUMN user_id INTEGER REFERENCES users(id);
ALTER TABLE grades
ADD COLUMN student_id INTEGER REFERENCES students(id);

ALTER TABLE scores
ADD COLUMN value FLOAT;


