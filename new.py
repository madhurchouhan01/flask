from flask import Flask, render_template, request, session, url_for, redirect,flash,abort
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key="Don't say anyone"
# conn=sqlite3.connect("bookings.db")
# cur=conn.cursor()
# cur.execute("CREATE TABLE persons(username TEXT, password TEXT)")
# conn.commit()
# conn.close()
# conn=sqlite3.connect("hey.db")
# cur=conn.cursor()
# cur.execute("CREATE TABLE heyall(username TEXT, password TEXT, age TEXT,nationality TEXT, state TEXT, berth TEXT, phone INTEGER, email TEXT)")
# conn.commit()
# conn.close()

@app.route('/')
def action():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/panchvalley')
def panchavalley():
    
    return render_template('panchvalley.html')
@app.route('/chandigarh')
def chandigarh():
    
    return render_template('chandigarh.html')
@app.route('/ranthambore')
def ranthambore():
    
    return render_template('ranthambore.html')
@app.route('/malwa')
def malwa():
    
    return render_template('malwa.html')
@app.route('/shipra')
def shipra():
    
    return render_template('shipra.html')
@app.route('/about')
def about():
    
    return render_template('about.html')
@app.route('/FAQs')
def FAQs():
    
    return render_template('FAQs.html')
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='POST':
        if(request.form["email"]!="" and request.form["password"]!=""):
            username=request.form["email"]
            password=request.form["password"]

            conn=sqlite3.connect("signup.db")
            cur=conn.cursor()
            cur.execute("INSERT INTO person VALUES('"+username+"','"+password+"')")
            conn.commit()
            conn.close()
            return redirect(url_for("home"))
        else:
            flash("You have entered wrong credentials")
            return redirect(url_for('signup.html'))
    return render_template('signup.html')

@app.route('/book', methods=['GET','POST'])
def book():
    if request.method=='POST':
        if(request.form["nm"]!="" and request.form["pd"]!="" and request.form["age"]!="" and request.form["nat"]!="" and request.form["st"]!="" and request.form["bp"]!="" and request.form["num"]!="" and request.form["email"]!=""):
            username=request.form["nm"]
            password=request.form["pd"]
            age=request.form["age"]
            nationality=request.form["nat"]
            state=request.form["st"]
            berth=request.form["bp"]
            phone=request.form["num"]
            email=request.form["email"]

            conn=sqlite3.connect("hey.db")
            cur=conn.cursor()
            cur.execute("INSERT INTO heyall VALUES('"+username+"','"+password+"','"+age+"','"+nationality+"','"+state+"','"+berth+"','"+phone+"','"+email+"')")
            conn.commit()
            conn.close()
            return redirect(url_for("home"))
        else:
            return
    return render_template('book.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if(request.method=="POST"):
        username=request.form.get("username")
        password=request.form.get("password")
        conn=sqlite3.connect("signup.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM person WHERE username= '"+username+"' and password ='"+password+"'")
        r=cur.fetchall()
        for i in r:
            if (username==i[0] and password== i[1]):
                return redirect(url_for("home"))
            else:
                flash("You have entered wrong credentials, Enter valid username")
                return redirect(url_for('login.html'))

    return render_template('login.html')
    
if __name__ == "__main__":
        app.run(debug=True) 