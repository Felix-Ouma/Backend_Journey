from flask import *
import pymysql


# create an app
myapp = Flask(__name__)

# DEFINE THE ROUTE/ LINK TO API 
@myapp.route("/api/get_notes", methods = ["GET"])

# function to perform data  extration from the data 
def get_notes():

    # connect to the database
    connection = pymysql.connect(host="localhost", user="root", password="", database='simple_notes')
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute('SELECT * FROM notes;')

    # stores the results in variable
    short_notes = cursor.fetchall()


    # close the connection
    connection.commit()


    # return the results
    return jsonify(short_notes)



# run the app
if __name__ == "__main__":
    myapp.run(debug=True)