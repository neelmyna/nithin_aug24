import pymysql

def connectDb():
    conn = pymysql.Connect(
        host='localhost', port=3306,
        user='root', password='Root123',
        db='nithin_db', charset='utf8')
    return conn   

def readTrainerDetails():
    name = input('Enter trainer name: ')
    location = input('Enter trainer location: ')
    technology = input('Enter trainer technology: ')
    phone_number = input('Enter trainer phone_number: ')
    per_day_commercial = input('Enter trainer per_day_commercial: ')
    return (name, location, technology, phone_number, per_day_commercial)

def insertRow():
    trainer_obj = readTrainerDetails()
    connection = connectDb()
    
    db_cursor = connection.cursor()
    insert_query = """insert into trainers
    (name, location, technology, phone_number,
    per_day_commercial) values(%s, %s, %s, %s, %s)"""

    db_cursor.execute(insert_query, trainer_obj) 
    connection.commit()
    db_cursor.close()
    connection.close()

def updateRow():
    id = int(input('Enter ID of the trainer to update details: '))
    technology = input('Enter the technology to be updated: ')
    phone_number = int(input('Enter the new phone_number: '))
    query = 'update trainers set technology = %s, phone_number = %s where id = %s'
    connection = connectDb()
    db_cursor = connection.cursor()
    result = db_cursor.execute(query, (technology, phone_number, id))
    if result == None:
        print(f'Trainer with id {id} not found')
    else:
        print('Row updated successfully')
    connection.commit()
    db_cursor.close()
    connection.close()

def deleteRow():
    id = int(input('Enter ID of the trainer to delete row: '))
    query = 'delete from trainers where id = %s'
    connection = connectDb()
    db_cursor = connection.cursor()
    result = db_cursor.execute(query, id)
    if result == None:
        print(f'Trainer with id {id} not found')
    else:
        print('Row deletion successfull')
    connection.commit()
    db_cursor.close()
    connection.close()
    
def searchRow():
    id = int(input('Enter ID of the trainer to search row: '))
    query = 'select * from trainers where id = %s'
    connection = connectDb()
    db_cursor = connection.cursor()
    result = db_cursor.fetchone(query, id)
    if result == None:
        print(f'Trainer with id {id} not found')
    else:
        print(str(result))
    connection.commit()
    db_cursor.close()
    connection.close()
    
def listAllRows():
    query = 'select * from trainers'
    connection = connectDb()
    db_cursor = connection.cursor()
    all_rows = db_cursor.fetchall(query)
    if all_rows == None:
        print('No rows found in the table')
    for each_row in all_rows:
        print(str(each_row))
    connection.commit()
    db_cursor.close()
    connection.close()

def exitProgram():
    exit('End of Program')

def invalid_choice():
    print('Invalid choice entered')

menu = {
    1 : insertRow,
    2 : updateRow,
    3 : deleteRow,
    4 : serachRow,
    5 : listAllRows,
    6 : exitProgram
}

while True:
    print('1:Insert 2:Update 3:Delete 4:Search 5:ListAll 6:Exit')
    choice = int(input('Your choice please: '))
    menu.get(choice, invalid_choice)()
    