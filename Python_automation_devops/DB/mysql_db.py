import mysql.connector

db = mysql.connector.connect(
    host="190.92.174.189",  # Example: "db4free.net" or some IP
    user="tatotech_mock_user",  # Your DB username
    password="Mock@user",  # Your DB password
    database="tatotech_mock_db"  # Database name you created
)

cursor = db.cursor()

def test_check_db_connection():

    # Replace these with your actual database detail

# Check if connection was successful
    if db.is_connected():
        print("Connection successful!")
    else:
        print("Connection failed!")

def test_create_table():
    create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT,
            email VARCHAR(100) UNIQUE
        )
        """

    cursor.execute(create_table_query)
    print("Table 'users' created (or already exists).")

def test_insert_data_into_table():
    insert_query="INSERT into users (name,age,email,phone_number) values (%s,%s,%s,%s)"
    user_data=[
        ("Alice1", 28, "alice1@example.com",1234567891),
        ("Bob1", 35, "bob1@example.com",1234567898),
        ("Charlie1", 22, "charlie1@example.com",1234567899)
    ]

    cursor.executemany(insert_query,user_data)
    db.commit()
    print(f"{cursor.rowcount} users inserted successfully.")

def test_alter_table():
    query="alter table users change phone_number  mobile varchar(10) unique"
    print('phone number is added to table')
    cursor.execute(query)

def test_drop_table():
    query='drop table users'
    cursor.execute(query)

def test_upload_files():
    query="""create table if not exists files (
           id int auto_increment primary key,
           filename varchar(50),
           filedata longblob
           
           )"""
    cursor.execute(query)
    # with open('C:/Users/veera/Downloads/Python_Variables_and_Operators_CheatSheet.pdf', 'rb') as file:
    #     binary_data = file.read()

    insert_query = "INSERT INTO files (filename, filedata) VALUES (%s, %s)"
    cursor.execute(insert_query, ("example.pdf", "C:/Users/veera/Downloads/Python_Variables_and_Operators_CheatSheet.pdf"))
    db.commit()
    cursor.close()
    db.close()
