from flask import Flask , jsonify , render_template , redirect , url_for, session , request ,json
from flask_mysqldb import MySQL


application = Flask(__name__)

application.secret_key = 'r1fq1'
application.config['MYSQL_HOST'] = 'localhost'
application.config['MYSQL_USER'] = 'root'
application.config['MYSQL_PASSWORD'] = ''
application.config['MYSQL_DB'] = 'koperasi'
 
mysql = MySQL(application)

@application.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@application.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@application.route('/login_action', methods=['POST'])
def login_action():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password'] 
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return redirect(url_for('dashboard'))
        else:
            msg = 'error'
            return redirect(url_for('login', msg = msg))


@application.route('/dashboard', methods=['GET'])
def dashboard():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM user''')
    rv = cur.fetchall()
    # return jsonify(rv)
    return render_template("dashboard.html",value=rv)

@application.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@application.route('/add', methods=['GET'])
def add():
    return render_template('add.html')

@application.route('/action_add', methods=['POST'])
def action_add():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        status = request.form['status'] 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user (username,password,status) VALUES (%s, %s, %s)", (username, password, status))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('dashboard'))


@application.route("/delete/<int:id>",methods=['GET'])
def delete(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE from user WHERE id_user = %s " , (str(id)))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('dashboard')) 

# UPDATE `access_users`   
#    SET `contact_first_name` = :firstname,
#        `contact_surname` = :surname,
#        `contact_email` = :email,
#        `telephone` = :telephone 
#  WHERE `user_id` = :user_id --

if __name__ == '__main__':
    application.run(debug=True)

    