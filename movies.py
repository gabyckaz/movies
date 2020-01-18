#from app import app
from flask import Flask
from flask import jsonify
from flask import flash, request
import sqlite3,json
import logging
from logging.handlers import RotatingFileHandler
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = ['/movie/list','/api/example','/movie/add/rent']
app.config['JWT_SECRET_KEY'] = 'movie-test' 
app.config['JWT_CSRF_CHECK_FORM '] = True

jwt = JWTManager(app)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# log console
console = logging.StreamHandler()
console.setFormatter(formatter)
handler = RotatingFileHandler('log_movies.log', maxBytes=10*1000000, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(console)
logger.addHandler(handler)

# @app.route('/token/auth', methods=['POST'])
# def logintest():
    # username = str(request.form['user'])
    # password = str(request.form['pass'])
    # if username != 'test' or password != 'test':
        # return jsonify({'login': False}), 401

    # # Create the tokens we will be sending back to the user
    # access_token = create_access_token(identity=username)

    # # Set the JWT cookies in the response
    # resp = jsonify({'login': True})
    # set_access_cookies(resp, access_token)

    # return resp, 200
	
# @app.route('/api/example', methods=['GET'])
# @jwt_required
# def protected():
	# username = get_jwt_identity()
	# return jsonify({'hello': 'from {}'.format(username)}), 200
	
	
#TODOS
#Welcome page, lists basic movie info
@app.route('/')
def movies_list():
	try:
		conn = sqlite3.connect("movies.db")
		cursor = conn.cursor()
		cursor.execute("select * from movies where availability=0")
		movie=[]
		for record in cursor.fetchall():
			movie.append({'title': str(record[1]), 'desc': str(record[2]), 'img':str(record[3])})
		cursor.close()
		conn.close()
		return jsonify(data=movie,status="success"), 200
	except Exception as e:
		print(e)
		return jsonify(status="error")



#ADMIN
#See all info of all the movies
@app.route('/movie/list', methods=['GET'])
@jwt_required
def movies_list_admin():
	current_user_name = get_jwt_identity()
	if current_user_name:
		role=check_role(current_user_name)
		if 'admin' in role:
			try:
				conn = sqlite3.connect("movies.db")
				cursor = conn.cursor()
				cursor.execute("select * from movies")
				movie=[]
				for record in cursor.fetchall():
					movie.append({'title': str(record[1]), 'desc': str(record[2]), 'img':str(record[3]),'stock':int(record[4]),
					'rent':float(record[5]),'sale':float(record[6]),'availability':int(record[7]),'popularity':int(record[8])})
				cursor.close()
				conn.close()	
				return jsonify(data=movie,status="success",current_user=current_user_name,rol=role), 200	
			except Exception as e:
				print(e)
				return jsonify(status="error")
		else:
			return jsonify(status="error, you're not allowed",current_user=current_user_name,rol=role), 200			


#TODOS		
@app.route('/movie/<string:key>')
def search_names(key):
	try:
		movie=[]
		conn = sqlite3.connect("movies.db")
		cursor = conn.cursor()
		cursor.execute("select title,description,image from movies where title like '%"+str(key)+"%'")
		for record in cursor.fetchall():
			movie.append({'title': str(record[0]), 'desc': str(record[1]), 'img':str(record[2])})

		return jsonify(status="success",data=movie), 200
	except Exception as e:
		print(e)
		return jsonify(data="error")
	finally:
		cursor.close()
		conn.close()

#USER
@app.route('/movie/add/rent', methods=['POST'])
@jwt_required
def rent_movie():
	if request.method == 'POST':
		current_user_name = get_jwt_identity()
		if current_user_name:
			role=check_role(current_user_name)
			if 'user' in role:
				try:
					id_user = str(request.form['id_user'])
					id_movie=str(request.form['id_movie'])
					return_date=str(request.form['return_date'])
					price_penalty=3.50
					conn = sqlite3.connect("movies.db")
					conn.execute("INSERT INTO rents(id_user,id_movie,return_date,price_penalty) VALUES (?,?,?,?)",(id_user,id_movie,return_date,price_penalty));
					conn.commit()
					logger.info("The user "+str(id_user)+" has rented the movie "+str(id_movie))
					return jsonify(status="success",current_user=current_user_name,rol=role), 201
				except Exception as e:
					print(e)
					return jsonify(data="error"),
				conn.close()


#USER
@app.route('/movie/add/buy', methods=['POST'])
def buy_movie():
	if request.method == 'POST':
		try:
			id_user = str(request.form['id_user'])
			id_movie=str(request.form['id_movie'])
			stock=0
			conn = sqlite3.connect("movies.db")
			cursor = conn.cursor()
			cursor.execute("select stock from movies where id_movie="+str(id_movie))
			for record in cursor.fetchall():
				stock=record[0]
			if stock is 0:
				return jsonify(status="error, no stock"), 200
			else:
				#update stock
				stock-=1
				cursor = conn.cursor()
				cursor.execute("UPDATE movies SET stock=? WHERE id_movie=?",(stock,str(id_movie)))
				conn.execute("INSERT INTO sales(id_user,id_movie) VALUES (?,?)",(id_user,id_movie));
				conn.commit()
				logger.info("The user "+str(id_user)+" has bought the movie "+str(id_movie))
				return jsonify(status="success"), 201
		except Exception as e:
			print(e)
			return jsonify(data="error"),
		conn.close()
	
#USER	
@app.route('/movie/<int:key>/like', methods=['PUT'])
def like_movie(key):
	if request.method == 'PUT':
		try:
			#select value
			num_likes=[]
			conn = sqlite3.connect("movies.db")
			cursor = conn.cursor()
			cursor.execute("select popularity from movies where id_movie="+str(key))
			for record in cursor.fetchall():
				num_likes=record[0]
			num_likes+=1
			#insert new value
			cursor = conn.cursor()
			cursor.execute("UPDATE movies SET popularity=? WHERE id_movie=?",(num_likes,str(key)))
			conn.commit()
			logger.info("Movie "+str(key)+" has been liked")
			return jsonify(status="success",data=num_likes), 200
		except Exception as e:
			print(e)
			return jsonify(status="error"),
		conn.close()
		
		
#SOLO ADMIN		
@app.route('/movie/add', methods=['POST'])
def movies_add():
	if request.method == 'POST':
		try:
			title = str(request.form['title'])
			desc=str(request.form['desc'])
			stock=str(request.form['stock'])
			image=str(request.form['image'])
			rent_price=float(request.form['rent_price'])
			sale_price=float(request.form['sale_price'])
			availability=int(request.form['availability'])
			popularity=int(request.form['popularity'])
			conn = sqlite3.connect("movies.db")
			conn.execute("INSERT INTO movies(title,description,image,stock,rent_price,sale_price,availability,popularity) VALUES (?,?,?,?,?,?,?,?)",(title,desc,image,stock,rent_price,sale_price,availability,popularity));
			conn.commit()
			return jsonify(status="success"), 201
		except Exception as e:
			print(e)
			return jsonify(data="error"),
		conn.close()		
		
		
@app.route('/movie/<int:key>/', methods=['GET','PUT', 'DELETE'],)
def movies_detail(key):
	#TODOS
	if request.method == 'GET':
		try:
			movie=[]
			conn = sqlite3.connect("movies.db")
			cursor = conn.cursor()
			cursor.execute("select * from movies where id_movie="+str(key))
			for record in cursor.fetchall():
				movie.append({'title': str(record[1]), 'desc': str(record[2]), 'img':str(record[3])})

			return jsonify(status="success",data=movie), 201
		except Exception as e:
			print(e)
			return jsonify(status="error"),
		cursor.close()
		conn.close()
	
	#ADMIN
	if request.method == 'PUT':
		try:
			title = str(request.form['title'])
			desc=str(request.form['desc'])
			stock=str(request.form['stock'])
			desc=str(request.form['desc'])
			image=str(request.form['image'])
			rent_price=float(request.form['rent_price'])
			sale_price=float(request.form['sale_price'])
			availability=int(request.form['availability'])
			popularity=int(request.form['popularity'])
			#insert de nuevos valores
			conn = sqlite3.connect("movies.db")
			cursor = conn.cursor()
			cursor.execute("UPDATE movies SET title=?, description=?,image=?,stock=?, rent_price=?,sale_price=?, availability=?, popularity=? WHERE id_movie=?",(title,desc,image,stock,rent_price,sale_price,availability,popularity,str(key)))
			conn.commit()
			logger.info(str(title)+" has been updated, rental price: $"+str(rent_price)+", sale price: $"+str(rent_price))
			return jsonify(status="success"), 200
		except Exception as e:
			print(e)
			return jsonify(status="error"),
		conn.close()
		
	#ADMIN
	if request.method == 'DELETE':
		try:
			movie=[]
			conn = sqlite3.connect("movies.db")
			conn.execute("DELETE FROM movies WHERE id_movie="+str(key))
			conn.commit()
			conn.close()

			return jsonify(status="success"), 201
		except Exception as e:
			print(e)
			return jsonify(data="error"),
		cursor.close()
		conn.close()


@app.route('/login', methods=['POST'])
def login():
	hash_pass=""
	username= str(request.form['user'])
	password = str(request.form['pass'])
	
	conn = sqlite3.connect("movies.db")
	cursor = conn.cursor()
	cursor.execute("select pass from users where name='"+str(username)+"'")
	for record in cursor.fetchall():
		hash_pass=str(record[0])
	check=check_password_hash(hash_pass, password)
	if check is False:
		return jsonify(status="error",data="wrong credentials"), 200
	else:	
		# Create the tokens we will be sending back to the user
		access_token = create_access_token(identity=username)
		# Set the JWT cookies in the response
		resp = jsonify({'login': True})
		set_access_cookies(resp, access_token)
		return resp, 200


@app.route('/logout', methods=['POST'])
def logout():
    resp = jsonify({'status': True})
    unset_jwt_cookies(resp)
    return resp, 200
    
    
# Protect a view with jwt_required, which requires a valid access token
# in the request to access.
# @app.route('/protected', methods=['GET'])
# @jwt_required
# def protected():
    # # Access the identity of the current user with get_jwt_identity
    # current_user = get_jwt_identity()
    # if current_user:
        # return jsonify(logged_in_as=current_user), 200
    # else:
        # return jsonify(logged_in_as='anonymous user'), 200
    # return jsonify(logged_in_as=current_user), 200
    
def check_role(user_name):
	conn = sqlite3.connect("movies.db")
	cursor = conn.cursor()
	cursor.execute("select role from users WHERE name='"+str(user_name)+"'")
	for record in cursor.fetchall():
		user_role=str(record[0])
	return user_role	


if __name__=="__main__":
	app.run(debug=True)
