from flask import Flask, render_template, url_for, request, flash, get_flashed_messages
from re import search

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your secret key'

pattern = '^[a-z 0-9]+[\_.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'

@app.route('/', methods = ['POST', 'GET'])
def index():
   if request.method == "POST":
      email = request.form["email"]
      password = request.form["password"]
      confirm = request.form["confirm"]
      if not search(pattern, email):
         flash('Invalid email adress․', category = "email")
      if len(password) < 6:
         flash('The number of password characters is at least 6.', category = "password")
      if confirm != password:
         flash('Password not confirmed.', category="confirm")
      if (search(pattern, email) and len(password) >= 6 and confirm == password):
         flash('Sucesfull registered!', category="sucess")
   return render_template('index.html', title="FlaskApp - register")

if __name__ == '__main__':
   app.run()