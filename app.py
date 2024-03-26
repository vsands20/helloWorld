from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Victoria Sands! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():
    return render_template('about-css.html')

@app.route('/favorite-course', methods=['GET','POST'])
def favoritecourse():

    print('Subject Entered: ' + request.args.get('subject_name'))
    print('Course Entered: ' + request.args.get('course_number'))
    print ('You entered your favorite course as:' + request.form.get('subject_name''  ''course_number'))


    return render_template('favorite-course.html')

if __name__ == '__main__':
    app.run()