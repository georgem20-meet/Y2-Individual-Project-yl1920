from flask import Flask, render_template, request, redirect
from databases import *

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['uname']
        password = request.form['psw']

        if username == 'admin' and password == 'admin':
        	info = query_all()

        	return render_template('bend.html', info = info)

        else:
        	return render_template('index.html', error= 'Username or password incorrect')

@app.route('/')
def homepage():	
	info = query_all()

	return render_template('index.html',info= info)

@app.route('/add' methods=["POST"])
def add():	
	info = query_all()

	header = request.form["header"]
	body= request.form["body"]
	images= request.form["images"]
	link = request.form["link"]

	add_News(header, body, images, link)

	return render_template('index.html',info= info)


@app.route('/edit', methods=['POST'])
def editpage():



	header = request.form["header"]
	body= request.form["body"]
	images= request.form["images"]
	link = request.form["link"]

	edit_image(header, image
)
	# left.position = request.form['left.position']
	# middle.position = request.form['midde.position']
	# right.position = request.form['right.position']
	# left.header = request.form['left.header']
	# middle.header = request.form['middle.header']
	# right.header = request.form['right.header']
	# left.body = request.form['left.body']
	# middle.body = request.form['middle.body']
	# right.body = request.form['right.body']
	# left.images = request.form['left.images']
	# middle.images = request.form['middle.images']
	# right.images = request.form['right.images']
	# left.link = request.form['left.link']
	# middle.link = request.form['middle.link']
	# right.link = request.form['right.link']

	
	return redirect('/')

@app.route('/delete', methods=['POST'])
def deletepage():

	choose= request.form["choose"]

	delete_News(choose)
	return redirect("/")
	
if __name__ == '__main__':
    app.run(debug = True, threaded=False, port=5000)
