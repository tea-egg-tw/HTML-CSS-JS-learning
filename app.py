from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/about')
def about_page():

    admin = {
        'name':'Mark'
        
    }
        

    return render_template('about.html', admin=admin)

if __name__ == '__main__':
    app.run(debug=True)