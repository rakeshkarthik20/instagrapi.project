from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('project.html')

@app.route('/handle_data', methods = ['POST', 'GET'])
def handle_data():
    userQuestion = request.form['user_id']
    print(userQuestion)
    return render_template('project.html', userQuestion = userQuestion)

if __name__ == '__main__':
   app.run()