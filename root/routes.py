from root import app
from flask import render_template,redirect,url_for,flash,request,session
from root.model import blogdb
from root import db
from root.forms import loginform,blogform







with app.app_context():
    db.create_all()
    

@app.route('/')
def home():

    post = blogdb.query.all()
    form = blogform()
    
    return render_template('index.html',post=post,form=form)




@app.route('/login',methods=['GET','POST'])
def login():
    form = loginform()
    if form.validate_on_submit():
        
        username = form.username.data
        password =  form.password.data
        
        
        if username == "user" and password == "blog":
            return redirect( url_for('home') )

    
    return render_template('login.html', form=form)

@app.route('/post',methods=['GET','POST'])
def post():
    form = blogform()
     
    if request.method == 'POST':
        title = form.title.data
        blog = form.blogpost.data
        owner = "user"

        post = blogdb(owner=owner,title=title,blogdata=blog)

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('home'))


