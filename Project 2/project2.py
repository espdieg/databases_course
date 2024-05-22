import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='project2',
        user='root',
        password='password'
    )
   
    if connection.is_connected():
        cursor = connection.cursor()
	
	# defining publishers table 
        create_publishers_table = """
        CREATE TABLE IF NOT EXISTS publishers (
          pubID INT(3) NOT NULL,
          pname VARCHAR(30) NULL,
          email VARCHAR(50) NULL,
          phone VARCHAR(30) NULL,
          PRIMARY KEY (pubID),
          UNIQUE INDEX email_UNIQUE (email ASC) VISIBLE
        )
        """
       
	# defining subjects table
        create_subjects_table = """
        CREATE TABLE IF NOT EXISTS subjects (
          subID VARCHAR(5) NOT NULL,
          sName VARCHAR(30) NULL,
          PRIMARY KEY (subID)
        )
        """
       
	# defining authors table
        create_authors_table = """
        CREATE TABLE IF NOT EXISTS authors (
          auID INT(5) NOT NULL,
          aName VARCHAR(30) NULL,
          email VARCHAR(50) NULL,
          phone VARCHAR(30) NULL,
          PRIMARY KEY (auID),
          UNIQUE INDEX email_UNIQUE (email ASC) VISIBLE
        )
        """

	# defining titles table       
        create_titles_table = """
        CREATE TABLE IF NOT EXISTS titles (
          titleID INT(5) NOT NULL,
          title VARCHAR(30) NULL,
          pubID INT(3) NULL,
          subID VARCHAR(5) NULL,
          pubDate DATE NULL,
          cover VARCHAR(10) NULL,
          price INT(4) NULL,
          PRIMARY KEY (titleID),
          INDEX pubid_idx (pubID ASC) VISIBLE,
          INDEX subid_idx (subID ASC) VISIBLE,
          CONSTRAINT pubid
             FOREIGN KEY (pubID)
             REFERENCES publishers (pubID)
             ON DELETE NO ACTION
             ON UPDATE NO ACTION,
          CONSTRAINT subid
             FOREIGN KEY (subID)
             REFERENCES subjects (subID)
             ON DELETE NO ACTION
             ON UPDATE NO ACTION
        )
        """

	# defining titleauthors table       
        create_titleauthors_table = """
        CREATE TABLE IF NOT EXISTS titleauthors (
          titleID INT(5) NOT NULL,
          auID INT(5) NOT NULL,
          importance INT(2) NULL,
          PRIMARY KEY (titleID, auID),
          INDEX auID_idx (auID ASC) VISIBLE,
          CONSTRAINT titleid
             FOREIGN KEY (titleID)
             REFERENCES titles (titleID)
             ON DELETE NO ACTION
             ON UPDATE NO ACTION,
          CONSTRAINT auID
             FOREIGN KEY (auID)
             REFERENCES authors (auID)
             ON DELETE NO ACTION
             ON UPDATE NO ACTION
        )
        """

	# creating tables       
        cursor.execute(create_publishers_table)
        cursor.execute(create_subjects_table)
        cursor.execute(create_authors_table)
        cursor.execute(create_titles_table)
        cursor.execute(create_titleauthors_table)

	# inserting values into subjects table       
        subject_query = "INSERT INTO subjects (subID, sName) VALUES (%s, %s)"
        subject_values = [
            ('ORA', 'ORACLE DATABASE'),
            ('JAVA', 'JAVA LANGUAGE'),
            ('JEE', 'JAVA ENTERPRISE EDITION'),
            ('VB', 'VISUAL BASIC.NET'),
            ('ASP', 'ASP.NET')
        ]
        cursor.executemany(subject_query, subject_values)

	# inserting values into publishers table         
        publisher_query = "INSERT INTO publishers (pubID, pname, email, phone) VALUES (%s, %s, %s, %s)"
        publisher_values = [
            (1,'WILLEY','WDT@VSNL.NET','9112326087'),
            (2,'WROX','INFO@WROX.COM',None),
            (3,'TATA MCGRAW-HILL','FEEDBACK@TATAMCGRAWHILL.COM','9133333322'),
            (4,'TECHMEDIA','BOOKS@TECHMEDIA.COM','9133257660')
        ]
        cursor.executemany(publisher_query, publisher_values)

	# inserting values into authors table         
        author_query = "INSERT INTO authors (auID, aName, email, phone) VALUES (%s, %s, %s, %s)"
        author_values = [
            (101, 'HERBERT SCHILD','HERBERT@YAHOO.COM', '2137823450'),
            (102, 'JAMES GOODWILL','GOODWILL@HOTMAIL.COM', '9095871243'),
            (103, 'DAVAID HUNTER','HUNTER@HOTMAIL.COM', '9094235581'),
            (104, 'STEPHEN WALTHER','WALTHER@GMAIL.COM', '2138773902'),
            (105, 'KEVIN LONEY','LONEY@ORACLE.COM', '9493423410'),
            (106, 'ED. ROMANS', 'ROMANS@THESERVERSIDE.COM', '9495012201')
        ]
        cursor.executemany(author_query, author_values)

	# inserting values into titles table         
        title_query = "INSERT INTO titles (titleID, title, pubID, subID, pubDate, cover, price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        title_values = [
            (1001,'ASP.NET UNLEASHED',4,'ASP','2002-04-02','HARD COVER',540),
            (1002,'ORACLE10G COMP. REF.',3,'ORA','2005-05-01','PAPER BACK',575),
            (1003,'MASTERING EJB',1,'JEE','2005-02-03','PAPER BACK',475),
            (1004,'JAVA COMP. REF',3,'JAVA','2005-04-03','PAPER BACK',499),
            (1005,'PRO. VB.NET',2,'VB','2005-06-15','HARD COVER',450),
            (1006,'INTRO. VB.NET',2,'VB','2002-12-02','PAPER BACK',425)
        ]
        cursor.executemany(title_query, title_values)

	# inserting values into titleauthors table         
        titleauthors_query = "INSERT IGNORE INTO titleauthors (titleID, auID, importance) VALUES (%s, %s, %s)"
        titleauthors_values = [
            (1001,104,1),
            (1002,105,1),
            (1003,106,1),
            (1004,103,1),
            (1005,103,1),
            (1005,102,2)
        ]
        cursor.executemany(titleauthors_query, titleauthors_values)
  
	# Query 1      
        print("Query 1 output:")
        cursor.execute("SELECT * FROM titles")
        for row in cursor:
            print(row)

	# Query 2
        print("\nQuery 2 output:")
        create_customer_table = """
        CREATE TABLE IF NOT EXISTS customer (
          custID INT AUTO_INCREMENT PRIMARY KEY,
          custName VARCHAR(30) NULL,
          zip INT(5) NULL,
          city VARCHAR(30) NULL,
          state VARCHAR(30) NULL
        )
        """
        cursor.execute(create_customer_table)
        print("Table 'customer' created. Since there is nothing inside the table yet, I will just print column names below to verify.")
        cursor.execute("DESCRIBE customer")
        columns = cursor.fetchall()
        for column in columns:
            print(column[0])
        print("\n")

	# Query 3        
        print("Query 3 output:")
        customer_query = "INSERT IGNORE INTO customer (custName) VALUES (%s)"
        customer_values = [
            ('ABRAHAM SILBERSCHATZ',),
            ('HENRY KORTH',),
            ('CALVIN HARRIS',),
            ('MARTIN GARRIX',),
            ('JAMES GOODWILL',)
        ]
        cursor.executemany(customer_query, customer_values)
        print("Customers have been added to 'customer' table. This table is shown below:")
        cursor.execute("SELECT * FROM customer")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("\n")

	# Query 4        
        print("Query 4 output:")
        cursor.execute("SELECT pubID, COUNT(*) AS title_count FROM titles GROUP BY pubID ORDER BY title_count DESC")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

	# Query 5        
        print("\nQuery 5 output: ")
        cursor.execute("""
            SELECT authors.auID, authors.aName, SUM(titles.price) AS total_price
            FROM authors
            JOIN titleauthors ON authors.auID = titleauthors.auID
            JOIN titles ON titleauthors.titleID = titles.titleID
            GROUP BY authors.auID, authors.aName
            ORDER BY total_price DESC
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)       

	# Query 6        
        print("\nQuery 6 output: ")
        cursor.execute("""
            SELECT titles.title
            FROM titles
            JOIN (
                  SELECT titleID
                  FROM titleauthors
                  GROUP BY titleID
                  HAVING COUNT(*) > 1
            ) AS multiple_authors ON titles.titleID = multiple_authors.titleID
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(row) 

	# Query 7            
        print("\nQuery 7 output: ")
        cursor.execute("""
            SELECT publishers.pname
            FROM publishers
            JOIN titles ON publishers.pubID = titles.pubID
            WHERE titles.cover = 'Paper Back' AND titles.price < 500
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

	# Query 8            
        print("\nQuery 8 output: ")
        cursor.execute("""
            SELECT authors.aName
            FROM authors
            JOIN titleauthors ON authors.auID = titleauthors.auID 
            JOIN titles ON titleauthors.titleID = titles.titleID 
            JOIN subjects ON titles.subID = subjects.subID
            WHERE subjects.sName LIKE '%JAVA%'
            AND authors.auID NOT IN (
                SELECT DISTINCT titleauthors.auID
                FROM titleauthors 
                JOIN titles ON titleauthors.titleID = titles.titleID
                JOIN subjects ON titles.subID = subjects.subID
                WHERE subjects.sName = 'VISUAL BASIC.NET'
            )                       
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

	# Query 9        
        print("\nQuery 9 output: ")
        cursor.execute("""
            SELECT pname
            FROM publishers
            WHERE email LIKE '%.com' 
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

	# Query 10            
        print("\nQuery 10 output: ")
        cursor.execute("""
             UPDATE titles
             SET price = price * 0.95
             WHERE YEAR(pubDate) < 2003
        """)
        cursor.execute("""
             UPDATE titles
             SET price = price * 1.15
             WHERE YEAR(pubDate) > 2004           
        """)
        print("Prices have been updated. Below is the new table values: ")
        cursor.execute("""SELECT * FROM titles""")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

	# commit all changes to DB
        connection.commit()
       
except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("\nMySQL connection is closed")