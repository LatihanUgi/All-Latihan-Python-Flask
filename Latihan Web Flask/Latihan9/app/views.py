from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from .forms import SignUp


@app.route('/')						   
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
						   
@app.route('/')						   
@app.route('/daftar', methods=['GET', 'POST'])
def daftar():
    form = SignUp()
    if form.validate_on_submit():
        flash('Username="%s", Email = "%s" , Password = "%s", Status = "%s"' %(form.username.data, form.email.data, form.password.data, form.accept_tos.data))
        return redirect('/daftar')
    return render_template('daftar.html', 
                           title='Sign Up',
                           form=form)
						   

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Muhammad Hudya Ramadhana'}  # fake user
	posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Mutia Ayu Dianita'}, 
            'body': 'Kid, masih jaman jomblo? taken sana~ HAHAHA' 
        },
        { 
            'author': {'nickname': 'Buce Immanuel'}, 
            'body': 'Gimana kid? doi udah peka belom?' 
        },
		{ 
            'author': {'nickname': 'Chacha Barizana'}, 
            'body': 'Dhan, jomblonya jangan ketauan banget dong hehehe >,<' 
        },
		{ 
            'author': {'nickname': 'Yudi Setiawan'}, 
            'body': 'Semangat ya mas nyari pacarnya!' 
        },
		{ 
            'author': {'nickname': 'Reza Ramadhan'}, 
            'body': 'Kid buruan dong taken!' 
        },
		{ 
            'author': {'nickname': 'Insan Hamzah'}, 
            'body': 'ayo mas buruan lepasin status jomblonya oi oi oi!' 
        },
		{ 
            'author': {'nickname': 'Azuura Salsabila'}, 
            'body': 'Semangat ya my brother ! jangan jomblo mulu <3 laffyu' 
        },
		{ 
            'author': {'nickname': 'Nabilah Maulida'}, 
            'body': 'Kak! gausah takut dibilang jomblo! inget Allah aja kak selalu bersama kamu hehehe' 
        },
		{ 
            'author': {'nickname': 'David Beckham'}, 
            'body': 'Keep smile bro! Single is a reason to choose among the best!' 
        },
		{ 
            'author': {'nickname': 'Dimas Faza'}, 
            'body': 'Santai aja dong broh kalo jomblo hehehehe' 
        },
		{ 
            'author': {'nickname': 'Akashi Seijuro'}, 
            'body': 'If a girl reject you, tell me and i will kill her.' 
        }
		
    ]
	return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)