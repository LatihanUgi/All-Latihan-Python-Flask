from flask import render_template
from app import app

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/authorize')
def facebook_authorize():
	if not current_user.is_anonymous: # if user logged in
		return redirect(url_for('index'))
	oauth = FacebookSignIn() # if user anonymous, begin the authorization phase
	return oauth.authorize()
	
class FacebookSignIn(object):

	def __init__(self):
		credentials = current_app.config['OAUTH_CREDENTIALS']['facebook'] #takes the app credentials obtained in Facebook  
		self.consumer_id = credentials['id']
		self.consumer_secret = credentials['secret']
		self.service = OAuth2Service(
			name='facebook',
			client_id=self.consumer_id,
			client_secret=self.consumer_secret,
			authorize_url='https://www.facebook.com/dialog/oauth',
			access_token_url='https://graph.facebook.com/oauth/access_token',
			base_url='https://graph.facebook.com/'
		) # initialize the OAuth2 service object with the app credentials and URLs required by the OAuth2 machinery
		
def authorize(self):
	return redirect(self.service.get_authorize_url(
		scope='public_profile,email',
		response_type='code',
		redirect_uri=self.get_callback_url()
	))
	
@app.route('/callback')
def show_preloader_start_authentication():
	if not current_user.is_anonymous:
		return redirect(url_for('index'))
 
    # store in the session id of the asynchronous operation
	status_pending = AsyncOperationStatus.query.filter_by(code='pending').first()
	async_operation = AsyncOperation(async_operation_status_id=status_pending.id)
	db.session.add(async_operation)
	db.session.commit()
    # store in a session the id of asynchronous operation
	session['async_operation_id'] = str(async_operation.id)
    # run external_auth in the separate thread
	taskman.add_task(external_auth) 
	return redirect(url_for('preloader'))
	
@app.route('/get-status')
def get_status():
	if 'async_operation_id' in session:
		async_operation_id = session['async_operation_id']
        # retrieve from database the status of the stored in session async operation
		async_operation = AsyncOperation.query.filter_by(id=async_operation_id).join(AsyncOperationStatus).first()
		status = str(async_operation.status.code)
		print async_operation.status.code
	else:
		print "async operation not in session"
		return redirect(url_for(error))
		
	return status
	
def external_auth():
	oauth = FacebookSignIn()
	facebook_id, email, first_name, last_name = oauth.callback()
	if facebook_id is None:
		flash('Authentication failed')
       # change the status of async operation for 'error'
		status_error = AsyncOperationStatus.query.filter_by(code='error').first()
#        print "external auth" + session['async_operation_id']
		async_operation = AsyncOperation.query.filter_by(id=session['async_operation_id']).first()
		print async_operation.id
		async_operation.async_operation_status_id = status_error.id
		db.session.add(async_operation)
		db.session.commit()
		return redirect(url_for('error'))
 
   # retrieve the user data from the database
	user = UserProfile.query.filter_by(facebook_id=facebook_id).first()
 
   # if the user is new, we store their credentials in user_profile table
	if not user:
		user = UserProfile(facebook_id=facebook_id, email=email, first_name=first_name, last_name=last_name)
		db.session.add(user)
		db.session.commit()
 
   # change the status of the async operation for 'ok' and insert the value of the user id
   # to the async_operation table
	status_ok = AsyncOperationStatus.query.filter_by(code='ok').first()
	async_operation = AsyncOperation.query.filter_by(id=session['async_operation_id']).first()
	async_operation.async_operation_status_id = status_ok.id
	async_operation.user_profile_id = user.id
	db.session.add(async_operation)
	db.session.commit()
	
def callback(self):
	if 'code' not in request.args:
		return None, None, None, None
		oauth_session = self.service.get_auth_session(
			data={'code': request.args['code'],
					'redirect_uri': self.get_callback_url()
				}
		)
		user_data = oauth_session.get('me?fields=id,email,first_name,last_name').json()
		return (
			user_data=['id'],
			user_data.get('email'),
			user_data.get('first_name'),
			user_data.get('last_name')
		)