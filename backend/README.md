## Create project folder, create virtual env inside that folder:
python -m venv venv   # keeps your project’s Python packages separate from other projects. and creates a dir  venv

source venv/bin/activate   # Mac/Linux

venv\Scripts\activate      # Windows first goto E: drive where project folder is

pip install flask

## Create app.py

app.run(debug=True)

    Starts the built-in Flask development server.

    debug=True enables:

        Auto-reload: the server restarts automatically when you change code (very convenient while developing).

        Interactive debugger: if an error happens, Flask shows a helpful web debugger with stack trace.

    Security note: never use debug=True in production — the interactive debugger can allow executing code on your machine if exposed publicly.

    Default host/port: the server binds to 127.0.0.1 (localhost) and port 5000. You can change them:

## app.run(host='0.0.0.0', port=8000, debug=True) ##

    host='0.0.0.0' makes the server reachable from other machines (e.g., your phone on the same Wi-Fi)



## Error ##

 return render_template(templates/'index.html')
NameError: name 'templates' is not defined
127.0.0.1 - - [06/Nov/2025 02:19:19] "GET /abc?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 -
 # Flask automatically looks for a folder named templates in the same directory as your app.py. no need for specify template path but if our template folder not in same dir 
 then use 
 ## app = Flask( __name__, template_folder=r"E:\sonia_dir\python\html_templates")  ##
