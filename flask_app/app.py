from flask import Flask, render_template, redirect, url_for
import subprocess
import os
import sys

app = Flask(__name__)

SCRIPTS_PATH = r"C:\Users\Mehjabin\Desktop\Selenium-Testing\test-project"

# Output files for each script
OUTPUT_FILES = {
    'login': os.path.join(SCRIPTS_PATH, 'Main Super Admin Output.txt'),
    'brand_settings': os.path.join(SCRIPTS_PATH, 'Brand Settings Output.txt'),
    'system_settings': os.path.join(SCRIPTS_PATH, 'System Settings Output.txt'),
    'company_settings': os.path.join(SCRIPTS_PATH, 'Company Settings Output.txt'),
    'bank_settings': os.path.join(SCRIPTS_PATH, 'Bank Settings Output.txt'),
    'settings_user': os.path.join(SCRIPTS_PATH, 'Settings User Output.txt')
}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/run_script/<script_name>')
def run_script(script_name):
    try:
        if script_name == 'login':
            script_path = os.path.join(SCRIPTS_PATH, 'Main_Super_Admin.py')
            output_file = OUTPUT_FILES['login']

        elif script_name == 'brand_settings':
            script_path = os.path.join(SCRIPTS_PATH, 'brand_settings.py')
            output_file = OUTPUT_FILES['brand_settings']

        elif script_name == 'system_settings':
            script_path = os.path.join(SCRIPTS_PATH, 'system_settings.py')
            output_file = OUTPUT_FILES['system_settings']


        elif script_name == 'company_settings':
            script_path = os.path.join(SCRIPTS_PATH, 'company_settings.py')
            output_file = OUTPUT_FILES['company_settings']

        elif script_name == 'bank_settings':
            script_path = os.path.join(SCRIPTS_PATH, 'bank_settings.py')
            output_file = OUTPUT_FILES['bank_settings']

        elif script_name == 'settings_user':
            script_path = os.path.join(SCRIPTS_PATH, 'settings_user.py')
            output_file = OUTPUT_FILES.get('settings_user', os.path.join(SCRIPTS_PATH, 'Settings User Output.txt'))


        else:
            return "Invalid script name!"


        process = subprocess.Popen([sys.executable, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if process.returncode == 0:
            return redirect(url_for('show_output', script_name=script_name, _external=True, _scheme='http'))
        else:
            return f"Error executing script {script_name}:<br><pre>{error.decode('utf-8')}</pre>"
    except Exception as e:
        return f"Exception occurred: {str(e)}"


# OUTPUT Showing

@app.route('/show_output/<script_name>')
def show_output(script_name):
    try:
        output_file = OUTPUT_FILES.get(script_name)
        if not output_file or not os.path.exists(output_file):
            return "Output file not found."

        with open(output_file, 'r') as file:
            output_content = file.read()

        # Replace newline characters with <br> for HTML rendering
        output_content = output_content.replace('\n', '<br>')

        return render_template('output.html', output_content=output_content)
    except FileNotFoundError:
        return "Output file not found."




if __name__ == '__main__':
    app.run(debug=True)