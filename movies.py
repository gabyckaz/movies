from app import app
from flask import jsonify
from flask import flash, request
import sqlite3,json
import os
import logging
from logging.handlers import RotatingFileHandler

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# # log console
# console = logging.StreamHandler()
# console.setFormatter(formatter)
# handler = RotatingFileHandler(os.path.join(os.getenv("HOME"), 'log_movies.log'), maxBytes=10*1000000, backupCount=5)
# handler.setFormatter(formatter)
# logger.addHandler(console)
# logger.addHandler(handler)

#TODOS
@app.route('/')
def movies_list():
	try:
		conn = sqlite3.connect("movies.db")
		cursor = conn.cursor()
		cursor.execute("select * from movies where availability=0")
		movie=[]
		desc=[]
		for record in cursor.fetchall():
			movie.append({'title': str(record[1]), 'desc': str(record[2]), 'img':str(record[3])})

		return jsonify(data=movie,status="success"), 200
	except Exception as e:
		print(e)
		return jsonify(status="error")
	finally:
		cursor.close()
		conn.close()
		
# @app.route('/movie/<str:key>/')
# def search_namesl(str):
	# try:
		# conn = sqlite3.connect("movies.db")
		# cursor = conn.cursor()
		# cursor.execute("select * from movies where title like %"+str(key)+"%")
		# movie=[]
		# desc=[]
		# for record in cursor.fetchall():
			# movie.append({'title': str(record[1]), 'desc': str(record[2]), 'img':str(record[3])})

		# return jsonify(status="success",data=movie), 200
	# except Exception as e:
		# print(e)
		# return jsonify(data="error")
	# finally:
		# cursor.close()
		# conn.close()		

#USER
@app.route('/movie/add/rent', methods=['POST'])
def rent_movie():
	if request.method == 'POST':
		try:
			id_user = str(request.form['id_user'])
			id_movie=str(request.form['id_movie'])
			return_date=str(request.form['return_date'])
			price_penalty=3.50
			conn = sqlite3.connect("movies.db")
			conn.execute("INSERT INTO rents(id_user,id_movie,return_date,price_penalty) VALUES (?,?,?,?)",(id_user,id_movie,return_date,price_penalty));
			conn.commit()
			#logger.info("El usuario "+str(id_user)+" ha realizado una renta de la pelicula "+str(id_movie))
			return jsonify(status="success"), 201
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
				#logger.info("El usuario "+str(id_user)+" compro la pelicula "+str(id_movie))
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
			#logger.info("Movie "+str(key)+" has been liked")
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
			#logger.info(str(title)+" has been updated, rental price"+str(rent_price)+", sale price "+str(rent_price))
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


if __name__=="__main__":
	app.run(debug=True)
