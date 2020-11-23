"""
Author: Ryan Hartman
Date: 11/10/2020
TA: Amanda Ly
I pledge my honor that I have abided by the Stevens Honor System.

To finish this lab session, you need to do the following tasks:
  · Task 1 & 2:  The skeleton code only creates the table branch and driver, you need to create the tables license and exam.
  · Task 3 & 4: The skeleton code only inserts part of records into the table branch and driver, you need to insert the remaining ones into these two tables.
  · Task 5 & 6: Enter the tuples of the tables license and exam.
  · Task 7: Display the answer of the following queries:
    · Q1:  Find the name of the drivers who got the license from the branch “NYC”.
    · Q2:  Find the name of the drivers whose driver license expire by 12/31/2022.  
    · Q3:  Find the name of the drivers who took at least 2 exams for the same driver license type at the same branch.
    · Q4:  Find the name of the drivers whose exam scores get consecutively lower when he/she took more exams.  
"""
import sys
import mysql.connector
from mysql.connector import errorcode

USER="ryan"
HOST="localhost"
PWD="tpisjkg11239"
DATABASE_NAME="VehicleOffice"

db = None
cursor = None

print("Connecting to database...")
while db == None or cursor == None:
  try:
    db = mysql.connector.connect(
      host=HOST,
      user=USER,
      password=PWD,
      database=DATABASE_NAME
    )
    cursor = db.cursor()
  except mysql.connector.Error:
    temp_db = mysql.connector.connect(
      host=HOST,
      user=USER,
      password=PWD
    )
    temp_cursor = temp_db.cursor()
    print("Creating database...")
    temp_cursor.execute(f"CREATE DATABASE { DATABASE_NAME }")
    temp_db.close()
    print("Database created successfully...")


def create_tables():
  global cursor
  # · branch( branch_id integer, branch_name varchar(20), branch_addr varchar(50), 
  #           branch_city varchar(20), branch_phone integer);
  sql = []
  sql.append( "CREATE TABLE branch(branch_id INTEGER NOT NULL PRIMARY KEY, " + \
              "branch_name VARCHAR(20) NOT NULL," + \
              "branch_addr VARCHAR(50)," + \
              "branch_city VARCHAR(20) NOT NULL," + \
              "branch_phone INTEGER)")

  # · driver( driver_ssn integer, driver_name varchar(20), driver_addr varchar(50), 
  #           driver_city varchar(20), driver_birthdate date, driver_phone integer);
  sql.append( "CREATE TABLE driver(driver_ssn INTEGER NOT NULL PRIMARY KEY," + \
              "driver_name VARCHAR(20) NOT NULL," + \
              "driver_addr VARCHAR(50) NOT NULL," + \
              "driver_city VARCHAR(20) NOT NULL," + \
              "driver_birthdate DATE NOT NULL," + \
              "driver_phone INTEGER)")
  
  # TODO Task 1, 5.3: Create Table License
  # · license(license_no integer, driver_ssn integer, license_type char, 
  #           license_class integer, license_expiry date, issue_date date, 
  #           branch_id integer);
  sql.append( "CREATE TABLE license(" + \
              "license_no INTEGER NOT NULL PRIMARY KEY," + \
              "driver_ssn INTEGER NOT NULL," + \
              "license_type CHAR NOT NULL," + \
              "license_class INTEGER NOT NULL," + \
              "license_expiry DATE NOT NULL," + \
              "issue_date DATE NOT NULL," + \
              "branch_id INTEGER NOT NULL," + \
              "FOREIGN KEY (branch_id) REFERENCES branch (branch_id)," + \
              "FOREIGN KEY (driver_ssn) REFERENCES driver (driver_ssn))")
  
  # TODO Task 2, 5.4: Create Table Exam
  # · exam( driver_ssn integer, branch_id integer, exam_date date, exam_type char, 
  #         exam_score integer);
  sql.append( "CREATE TABLE exam(" + \
              "driver_ssn INTEGER NOT NULL," + \
              "branch_id INTEGER NOT NULL," + \
              "exam_date DATE NOT NULL," + \
              "exam_type CHAR NOT NULL," + \
              "exam_score INTEGER NOT NULL," + \
              "PRIMARY KEY (driver_ssn, branch_id, exam_date)," + \
              "FOREIGN KEY (driver_ssn) REFERENCES driver (driver_ssn)," + \
              "FOREIGN KEY (branch_id) REFERENCES branch (branch_id))")
  
  for statement in sql:
    cursor.execute(statement)

def insert_records():
  sql = []
  sql.append("INSERT INTO branch values(10, 'Main', '1234 Main St.', 'Hoboken', 5551234)")
  sql.append("INSERT INTO branch values(20, 'NYC', '23 No.3 Road', 'NYC', 5552331)")

  # TODO Task 3, insert the rest of tuples in Table Branch
  # 30 \ West Creek \ 251 Creek Rd.   \ Newark    \ 5552511
  # 40 \ Blenheim   \ 1342 W.22 Ave.  \ Princeton \ 5551342
  sql.append("INSERT INTO branch values(30, 'West Creek', '251 Creek Rd.', 'Newark', 5552511)")
  sql.append("INSERT INTO branch values(40, 'Blenheim', '1342 W.22 Ave.', 'Princeton', 5551342)")

  sql.append("INSERT INTO driver values(111111111, 'Bob Smith', '111 E. 11 St.', 'Hoboken', '1975-01-01', 5551111)")
  sql.append("INSERT INTO driver values(222222222, 'John Walters', '222 E. 22 St.', 'Princeton', '1976-02-02', 5552222)")

  # TODO Task 4: insert the rest of tuples in Table Driver
  # 333333333 \ Troy Rops  \ 333 W.33 Ave \ NYC      \ 1970-03-03 \ 5553333
  # 444444444 \ Kevin Mark \ 444 E.4 Ave. \ Hoboken  \ 1974-04-04 \ 5554444
  sql.append("INSERT INTO driver values(333333333, 'Troy Rops', '333 W.33 Ave', 'NYC', '1970-03-03', 5553333)")
  sql.append("INSERT INTO driver values(444444444, 'Kevin Mark', '444 E.4 Ave.', 'Hoboken', '1974-04-04', 5554444)")

  # TODO Task 5, 6.3: insert all tuples into Table license;
  # 1 \ 11111111 \ D \ 5 \ 2022-05-24 \ 2017-05-25 \ 20
  # 2 \ 22222222 \ D \ 5 \ 2023-08-29 \ 2016-08-29 \ 40
  # 3 \ 33333333 \ L \ 5 \ 2022-12-27 \ 2017-06-27 \ 20
  # 4 \ 44444444 \ D \ 5 \ 2022-08-30 \ 2017-08-30 \ 40
  sql.append("INSERT INTO license values(1, 111111111, 'D', 5, '2022-05-24', '2017-05-25', 20)")
  sql.append("INSERT INTO license values(2, 222222222, 'D', 5, '2023-08-29', '2016-08-29', 40)")
  sql.append("INSERT INTO license values(3, 333333333, 'L', 5, '2022-12-27', '2017-06-27', 20)")
  sql.append("INSERT INTO license values(4, 444444444, 'D', 5, '2022-08-30', '2017-08-30', 40)")

  # TODO Task 6, 6.4: insert all tuples into Table exam
  # 11111111 \ 20 \ 2017-05-25 \ D \ 79
  # 11111111 \ 20 \ 2017-12-02 \ L \ 67
  # 22222222 \ 30 \ 2016-05-06 \ L \ 25
  # 22222222 \ 40 \ 2016-06-10 \ L \ 51
  # 22222222 \ 40 \ 2016-08-29 \ D \ 81
  # 33333333 \ 10 \ 2017-07-07 \ L \ 45
  # 33333333 \ 20 \ 2017-06-27 \ L \ 49
  # 33333333 \ 20 \ 2017-07-27 \ L \ 61
  # 44444444 \ 10 \ 2017-07-27 \ L \ 71
  # 44444444 \ 20 \ 2017-08-30 \ L \ 65
  # 44444444 \ 40 \ 2017-09-01 \ L \ 62
  sql.append("INSERT INTO exam values(111111111, 20, '2017-05-25', 'D', 79)")
  sql.append("INSERT INTO exam values(111111111, 20, '2017-12-02', 'L', 67)")
  sql.append("INSERT INTO exam values(222222222, 30, '2016-05-06', 'L', 25)")
  sql.append("INSERT INTO exam values(222222222, 40, '2016-06-10', 'L', 51)")
  sql.append("INSERT INTO exam values(222222222, 40, '2016-08-29', 'D', 81)")
  sql.append("INSERT INTO exam values(333333333, 10, '2017-07-07', 'L', 45)")
  sql.append("INSERT INTO exam values(333333333, 20, '2017-06-27', 'L', 49)")
  sql.append("INSERT INTO exam values(333333333, 20, '2017-07-27', 'L', 61)")
  sql.append("INSERT INTO exam values(444444444, 10, '2017-07-27', 'L', 71)")
  sql.append("INSERT INTO exam values(444444444, 20, '2017-08-30', 'L', 65)")
  sql.append("INSERT INTO exam values(444444444, 40, '2017-09-01', 'L', 62)")

  for statement in sql:
    cursor.execute(statement)
  db.commit()
  print("Records inserted succesfully...")

  cursor.execute("SELECT branch_id, branch_name, branch_addr FROM branch")
  results = cursor.fetchall()
  for result in results:
      print(f"branch id = {result[0]}, name = {result[1]}, address = {result[2]}")
  print(f"{len(results)} rows were retrieved.")

def print_result(pre, results):
  plurality = "s were" if len(results) > 1 else " was"
  for result in results:
    print(f"{pre} = {result[0]}")
  print(f"{len(results)} row{plurality} retrieved.")

def run_query(pre, sql):
  global cursor
  cursor.execute(sql)
  result = cursor.fetchall()
  print_result(pre, result)

def query_records():
  global cursor
  # TODO Task 7.1:
  # Find the name of the drivers who got the license from the branch “NYC”.
  input("Press any key to find the name of the drivers who got the license from the branch \"NYC\".")
  sql = "SELECT driver_name FROM license NATURAL JOIN driver NATURAL JOIN branch WHERE branch_city=\'NYC\'"
  run_query("driver_name", sql)

  # TODO Task 7.2:
  # Find the name of the drivers whose driver license expire by 12/31/2022.
  input("Press any key to find the name of the drivers whose driver license expire by 12/31/2022")
  sql = "SELECT driver_name FROM license NATURAL JOIN driver WHERE license_expiry <= '2022-12-31'"
  run_query("driver_name", sql)

  # TODO Task 7.3:
  # Find the name of the drivers who took at least 2 exams for the same driver license type at the same branch.
  input("Press any key to find the name of the drivers who took at least 2 exams for the same driver license type at the same branch.")
  sql = "SELECT driver_name FROM driver NATURAL JOIN exam GROUP BY driver_ssn, branch_id, exam_type HAVING COUNT(*) >= 2"
  run_query("driver_name", sql)

  # TODO Task 7.4:
  # Find the name of the drivers whose exam scores get consecutively lower when he/she took more exams.
  input("Press any key to find the name of the drivers whose exam scores get consecutively lower when he/she took more exams.")
  sql = "SELECT driver_name FROM driver WHERE driver_ssn NOT IN (SELECT E.driver_ssn FROM exam E JOIN exam E2 ON E2.exam_score > E.exam_score AND E.exam_date < E2.exam_date WHERE E.driver_ssn = E2.driver_ssn)"
  run_query("driver_name", sql)

def drop_db():
  global cursor
  cursor.execute(f"DROP DATABASE { DATABASE_NAME }")


if __name__ == "__main__":
  end_msg = "Press any key to end the script and drop the database."
  try:
    create_tables()
    insert_records()
    query_records()
    input(end_msg)
    drop_db()
    db.close()
  except Exception as e:
    print(f"ERROR {e}")
    input(end_msg)
    drop_db()
    db.close()