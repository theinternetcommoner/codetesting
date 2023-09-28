from flask import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
	# initialize value (this will show on the html file)
	x=0
	if request.method == 'POST':
		# get value from html form
		x = int(request.form['hidden'])
		# increment value by 1
		x+=1
		# print(x)	# for checking purposed
		return render_template('index.html', x = x)
	else:
		return render_template('index.html', x = x)

@app.route('/live')
def live():
	index()
	return render_template('live.html', x = x)

if __name__ == '__main__':
	app.run(debug = True, port = 5555)