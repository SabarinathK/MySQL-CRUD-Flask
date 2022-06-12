from flask import Flask, render_template,request, url_for,redirect
from flask_mysqldb import MySQL
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='flask_mysql'
mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        mydb=mysql.connection
        c=mydb.cursor()
        query="insert into primary_table (name,email,subject) value(%s,%s,%s)"
        c.execute(query,(name,email,subject))
        mydb.commit()
        return redirect(url_for('read'))
    return render_template('home.html')

@app.route('/read')
def read():
    mydb=mysql.connection
    c=mydb.cursor()
    query="select * from primary_table"
    c.execute(query)
    user=c.fetchall()
    return render_template ('read.html',datas=user)

@app.route('/edituser/<string:id>',methods=['GET' , "POST"])
def edit(id):
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        subject=request.form['subject']
        mydb=mysql.connection
        c=mydb.cursor()
        query="update primary_table set name=%s,email=%s,subject=%s where id =%s"
        c.execute(query,(name,email,subject,id))
        mydb.commit()
        c.close()
        return redirect(url_for('read'))
    
    mydb=mysql.connection
    c=mydb.cursor()
    query="select * from primary_table where id=%s"
    c.execute(query,id)
    user=c.fetchone()
    return render_template ('edit.html',datas=user)



@app.route('/deleteuser/<string:id>',methods=['GET' , "POST"])
def delete(id):
    mydb=mysql.connection
    c=mydb.cursor()
    query="delete from primary_table where id =%s"
    c.execute(query,id)
    mydb.commit()
    c.close()
    return redirect(url_for('read'))
    
if __name__=='__main__':
    app.run(debug=True)