import os
import sys
import subprocess
import threading
from flask import Flask, render_template, request, jsonify
import instaloader

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

app = Flask(__name__, 
            template_folder=resource_path('templates'),
            static_folder=resource_path('static'))
current_process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    use_browser = data.get('use_browser') # boolean

    if not username:
        return jsonify({"status": "error", "message": "El usuario es obligatorio."}), 400

    # Clean username if user pasted a full URL
    if "instagram.com" in username:
        username = username.strip('/').split('/')[-1]

    try:
        if use_browser:
            # Import cookies from Chrome using CLI
            cmd_cookies = [sys.executable, "-m", "instaloader", "--load-cookies", "chrome"]
            result = subprocess.run(
                cmd_cookies, 
                capture_output=True, text=True
            )
            if result.returncode != 0 and "error" in result.stderr.lower():
                return jsonify({"status": "error", "message": f"Error: {result.stderr.strip()}"}), 500
            return jsonify({"status": "success", "message": "Sesión importada de Chrome correctamente."})
        else:
            if not password:
                return jsonify({"status": "error", "message": "La contraseña es obligatoria."}), 400
            
            # Using CLI to login
            cmd_login = [sys.executable, "-m", "instaloader", "--login", username]
            result = subprocess.run(
                cmd_login, 
                input=password + "\n", 
                capture_output=True, text=True
            )
            if "Session saved" in result.stdout or "Logged in" in result.stdout or result.returncode == 0:
                return jsonify({"status": "success", "message": f"Sesión iniciada para {username}."})
            else:
                return jsonify({"status": "error", "message": "Error al iniciar sesión. Revisa la contraseña."}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": f"Error al iniciar sesión: {str(e)}"}), 500

@app.route('/api/download', methods=['POST'])
def download():
    global current_process
    
    if current_process and current_process.poll() is None:
        return jsonify({"status": "error", "message": "Ya hay una descarga en curso. Detenla primero."}), 400
        
    data = request.json
    target_type = data.get('type')
    target = data.get('target')
    username = data.get('username')
    
    # Clean username if user pasted a full URL
    if username and "instagram.com" in username:
        username = username.strip('/').split('/')[-1]
    
    if not target or not target_type:
        return jsonify({"status": "error", "message": "Faltan datos de descarga"}), 400
        
    cmd = [
        sys.executable, "-m", "instaloader",
        "-q", # Quiet mode to fail instead of asking for password
        "--dirname-pattern", "downloads/{target}",
        "--no-video-thumbnails",
        "--no-captions",
        "--no-metadata-json"
    ]
    
    # If a username is provided, use the saved session
    if username:
        cmd.extend(["--login", username])
        
    if target_type == 'profile':
        cmd.append(target)
    elif target_type == 'post':
        cmd.extend(["--", f"-{target}"])
        
    # Start download in background using subprocess
    current_process = subprocess.Popen(cmd)
    
    return jsonify({
        "status": "success", 
        "message": f"Descarga iniciada para {target}. Revisa la carpeta 'downloads'."
    })

@app.route('/api/stop', methods=['POST'])
def stop():
    global current_process
    if current_process and current_process.poll() is None:
        current_process.terminate()
        current_process.wait()
        current_process = None
        return jsonify({"status": "success", "message": "Descarga detenida forzosamente."})
        
    return jsonify({"status": "error", "message": "No hay descargas activas en este momento."})

import webbrowser

if __name__ == '__main__':
    # Abrir el navegador automáticamente después de un pequeño retraso
    threading.Timer(1.25, lambda: webbrowser.open("http://127.0.0.1:3017")).start()
    app.run(port=3017, debug=False)
