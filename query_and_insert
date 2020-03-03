import db_connect

mydb = db_connect.connect_dbs()
mycursor = mydb.cursor()
id0= str(input("What is the id? "))
id ='('+id0+')'

sql = "SELECT * FROM database.table WHERE id LIKE %s"
#In %-style you usually use %s for the string representation (string formatting syntax).
args = ['%'+id0+'%']
mycursor.execute(sql,args)

temp_result = mycursor.fetchall()

if not temp_result:
    print('This is not in database.')
    ask_hardcode = str(input("Want to hardcode this id? ") or 'Yes')
    if ask_hardcode == "Yes":
        price = int(input("What is the price? "))
        discounted_price = int(input("What is the discounted price? "))
        currency = str(input('What is the currency? ') or 'HKD')

        sql1 = "INSERT INTO database.table (type, target_id, price, discounted_price, currency) VALUES (%s, %s, %s, %s, %s)"
        args = ('1', id0, price, discounted_price, currency)
        mycursor.execute(sql1, args)
        mydb.commit()
        # Don't forget to commit!! If forgot, the query will not be executed.
        print('inserted into the database table!')

        sql2 = f"insert into es_updates (type, type_id) select 'product_priority', id from database.table where id IN {id}"
        #F-string
        mycursor.execute(sql2)
        mydb.commit()
        print('inserted into es update!')
    else:
        exit
else:
    print('This is hardcoded!')

