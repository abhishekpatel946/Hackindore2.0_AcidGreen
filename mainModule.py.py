import mysql.connector


# INSERT INTO DATASET'S
def insertData():
    mycursor = mydb.cursor()
    print('Symptom, Duration, Climate, Season, Date, Medicine, Result')

    symptom = input('Enter the Symptom : ')
    symptom = symptom.upper()
    
    duration = input('Enter the Duration : ')
    duration = duration.upper()
    
    climate = input('Enter the Climate : ')
    climate = climate.upper()
    
    season = input('Enter the Season : ')
    season = season.upper()
    
    date = input('Enter the Date <<YYYY-MM-DD>> : ')
    #date = date.upper()
    
    medicine = input('Enter the Medicine : ')
    medicine = medicine.upper()
    
    #result = input('Enter the Result')


    print('\t\n======Something Went Wrong!!!=======\n')
        
   #  sqlQuery = " INSERT INTO DATA1 (SYMPTOM, DURATION, CLIMATE, SEASON, date, MEDICINE, RESULT) VALUES(%s, %s, %s, %s, %s, %s, %s)"
   #  queryValues = (f'{symptom}, {duration}, {climate}, {season}, {date}, {medicine}')
    
    
   #  mycursor.execute(sqlQuery, queryValues)

   #  mydb.commit()

    

def displayAll():
    # for display the database
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM  DATA1')
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

    
def predictMedicine(symptom, climate):
    # predict the medicine and disease
    #print(symptom)
    #print(climate)

    sqlQuery =  f"SELECT DISTINCT MEDICINE FROM DATA1 WHERE SYMPTOM = '{symptom}' AND CLIMATE = '{climate}' "
    mycursor.execute(sqlQuery)
    myresult = mycursor.fetchall()
    for i in myresult:
        print('\n',i)

    print('\n\n\t____________Most Used Medicine in past___________\n')
    sqlQuery =  f" SELECT MEDICINE, COUNT(*) AS C FROM DATA1 GROUP BY MEDICINE ORDER BY C DESC LIMIT 5; "
    mycursor.execute(sqlQuery)
    myresult = mycursor.fetchall()
    for i in myresult:
        print('\n',i)

    
def predictDisease(climate, season):
    # predict the medicine and disease
    #print(symptom)
    #print(climate)
    
    sqlQuery =  f"SELECT SYMPTOM, MEDICINE FROM DATA1 WHERE CLIMATE = '{climate}' AND SEASON = '{season}' "
    mycursor.execute(sqlQuery)
    myresult = mycursor.fetchall()
    for i in myresult:
        print('\n',i)
    

    print('\n\n\t_________Most Probable Disease_________\n')
    sqlQuery =  f" SELECT SYMPTOM, MEDICINE, COUNT(MEDICINE) AS C FROM DATA1 GROUP BY MEDICINE ORDER BY C DESC "
    mycursor.execute(sqlQuery)
    myresult = mycursor.fetchall()
    for i in myresult:
        print('\n',i)
    






if __name__ == '__main__':
    
    mydb = mysql.connector.connect( 
    host = 'localhost',
    user = 'root',
    passwd = 'Shweta@123',
    database = 'db'
)
    
    print('\t\t-------------Future Disease Predictor------------\n')

    # print the whole dataset's
    displayAllmycursor = mydb.cursor()





    # insert data
    choise = input('___________Do you want to insert data? : ___________\n \t\t1.Yes \t 2.NO \n')
    if choise == '1':
        displayAllmycursor = mydb.cursor()
        mycursor = mydb.cursor()
        
        insertData()
    elif choise == '3':
        print('')



   
    # choises for prediction
    choise = input('_____________Do you want to predict : _____________ \n \t\t1.Medicine \t 2.Disease \t 3.Exit \n')

    
    if choise == '1':
        displayAllmycursor = mydb.cursor()
        mycursor = mydb.cursor()
        
        mycursor.execute(" SELECT DISTINCT SYMPTOM FROM DATA1 ")
        myresult = mycursor.fetchall()
        for i in myresult:
            print('\n\n',i,end='')
        symptom = input('\n\n\t Enter the Symptom : ')
        symptom = symptom.upper()
   
        mycursor.execute(" SELECT DISTINCT CLIMATE FROM DATA1 ")
        myresult = mycursor.fetchall()
        for i in myresult:
            print('\n\n',i,end=' ')
        climate = input('\n\n\t Enter the Climate : ')
        climate = climate.upper()

        
        predictMedicine(symptom, climate)



    
    elif choise == '2':
        displayAllmycursor = mydb.cursor()
        mycursor = mydb.cursor()
        
        mycursor.execute(" SELECT DISTINCT CLIMATE FROM DATA1 ")
        myresult = mycursor.fetchall()
        for i in myresult:
            print('\n\n',i,end='')
        climate = input('\n\n\t Enter the Climate : ')
        climate = climate.upper()
   
        mycursor.execute(" SELECT DISTINCT SEASON FROM DATA1 ")
        myresult = mycursor.fetchall()
        for i in myresult:
            print('\n\n',i,end=' ')
        season = input('\n\n\t Enter the Season : ')
        season = season.upper()
        
        
        predictDisease(climate, season)


        
    else:
        print('____________Thank You !!!________________')
