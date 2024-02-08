import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kushi@3641",
    database="pylog"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS form_responses (id INT AUTO_INCREMENT PRIMARY KEY, \
                  question1 VARCHAR(255), \
                  question2 VARCHAR(255), \
                  question3 VARCHAR(255), \
                  question4 VARCHAR(255), \
                  question5 VARCHAR(255))")

def fill_form():
    responses = []
    print("Please fill out the form:")
    for i in range(1, 6):
        response = input(f"Question {i}: ")
        responses.append(response)
    return responses

def insert_responses(responses):
    sql = "INSERT INTO form_responses (question1, question2, question3, question4, question5) VALUES (%s, %s, %s, %s, %s)"
    mycursor.execute(sql, tuple(responses))
    mydb.commit()
    print("Responses successfully stored in the database!")

if __name__ == "__main__":
    responses = fill_form()
    insert_responses(responses)

    mydb.close()
