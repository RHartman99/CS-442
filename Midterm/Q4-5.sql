-- Question 4
CREATE TABLE Statement (
  issuedDate DATE,
  sID INTEGER,
  accNum INTEGER,
  PRIMARY KEY (sID, accNum),
  FOREIGN KEY (accNum) REFERENCES Account
);

-- Question 5
CREATE TABLE Own (
  accNum INTEGER,
  ssn CHAR(9),
  PRIMARY KEY (accNum),
  FOREIGN KEY (accNum) REFERENCES Account,
  FOREIGN KEY (ssn) REFERENCES Customer
);