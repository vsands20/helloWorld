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

@app.route('/favorite-course')
def favoritecourse():

    print('Subject Entered: ' + request.args.get('subject'))
    print('Course Entered: ' + request.args.get('course_number'))


    return render_template('favorite-course.html')

@app.route('/contact',methods = ['GET','POST'])
def contact():
    if request.method =='POST':
        print('Thank you for filling out our contact form. Below is the information you entered:')
        print('First Name: ' + request.form.get('firstname'))
        print('Last Name: ' + request.form.get('lastname'))
        print('Email: ' + request.form.get('emailaddress'))
        print('Phone Number: ' + request.form.get('phonenumber'))


    return render_template('contact.html')

if __name__ == '__main__':
    app.run()