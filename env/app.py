def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        nom = request.form['name']
        prenom = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        recover= Account.query.filter_by(email=e)
        account = recover
        if account:
            message = 'Ce compte existe déjà'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message = 'Adresse invalide!'
        
        elif  not nom or not prenom or not  password or not email:
            message = 'tous les champs ne sont pas remplis remplissez les!'  
           # return render_template('correction.html', mesage = mesage)
        elif password != confirm_password:
            message = 'mot de passe incorrect resaisisssez le '
          #  return render_template('correction.html', mesage = mesage)
        elif not re.match(r'[A-Za-z]+', nom):
            message = 'le nom ne doit etre composé que de caractères!'
        elif not re.match(r'[A-Za-z]+',prenom):
            message = 'le champ prénom ne doit etre composé que de caractères!'

        else:
            user = Account(nom=name,prenom=surname,email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
        message = 'Vous avez été enregistrer avec succès!'
    elif request.method == 'POST':
        message = 'Please fill out the form !'
        return redirect(url_for("login"))
    return render_template('register.html', message = message)
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        user = Account.query.filter_by(email=email,password=password)
        if user:
            session['loggedin'] = True   
            session['email'] = user['email']
            session['password']=user['password']
            message = 'Connexion réussie !'
            return render_template('user.html', message = message)
        else:
            message = 'mot de passe/ email incorrect !'
    return render_template('login.html', message = message)
@app.route('/user')
def user():
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
       user = Account.query.filter_by('email = %s',(session['email'],))
        
        # Show the profile page with account info
       return render_template('user.html', session=session)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

