from flask import Flask, render_template , request , redirect, url_for

app = Flask(__name__)               #__name__: tells Flask where the application code lives so it can find static files and templates relative flask module

print(app)
@app.route('/')       #Decorator that tells Flask: “Run the following function index() when someone visits the path /
def index():        
    return "hello sonia"    #Returning a plain string makes Flask return an HTTP 200 response with content-type text/html by default. return render_template('index.html') would return the contents of templates/index.html.

@app.route('/abc')
def abc():
    return render_template('index.html')

if __name__ == '__main__':    
    app.run(debug=True)



