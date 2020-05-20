from flask import Flask, g,render_template,request #import flask to run python code using flask framework.
import sqlite3 #import sqlite3 for running code that includes tables and database.
app = Flask(__name__)#its like a main function. name is initialised as main
    
@app.route("/")#As soon as we start the application it returns signup.html page
def main():
    return render_template('signup.html')

@app.before_request#this function runs before each request.
def before_request():
    g.db = sqlite3.connect("cloud.db") #it connects to cloud.db file.
    
@app.route("/yourdetails", methods=["post"])
def yourdetails():
    c=g.db.cursor()#it iterates through the whole table
    username=request.form['UserName']#it gets the username from the form
    password=request.form['inputPassword']#it gets the inputpassword from the form
    c.execute("select username from tbl_user where username=(?)",[username])#query to find the row with the username is executed
    if c.fetchone() is not None :#fetchone returns rows if there are no rows then it will return none
       r_data=g.db.execute("select firstname,lastname,email from tbl_user where username=(?)",[username])#if username is found data is fetched
       return render_template('display.html',data=r_data)#Then it goes to display.html
    else:
       return render_template('details.html')#if data not found it goes to registration page which is details.html
    
    
@app.route("/Regestration", methods=["post"])#this is to store the details during registration
def Regestration():
   c=g.db.cursor()
   username= request.form['UserName']#it gets username, firstname and all the details from the form.
   firstname= request.form['FName']
   lastname= request.form['LName']
   email= request.form['Email']
   password = request.form['inputPassword']
   g.db.execute("INSERT INTO tbl_user(username,password,firstname,lastname,email) VALUES (?,?,?,?,?)", [username,password,firstname,lastname,email])#the values are stored in the table in sqlite3
   g.db.commit()#changes are committed
   mydata=c.execute("SELECT firstname,lastname,email from tbl_user where username=(?)",[username])#after data is fetched it is sent to display.html.
   return render_template('display.html',data=mydata)
         
         
if __name__=="__main__":
    app.run()
