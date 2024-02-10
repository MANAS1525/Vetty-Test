from flask import Flask, render_template, request
import os

app = Flask(__name__)

def read_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

@app.route('/', defaults={'file_name': 'file1.txt'})
@app.route('/<file_name>')
def display_file(file_name):
    try:
        start_line = request.args.get('start_line', type=int)
        end_line = request.args.get('end_line', type=int)
        content = read_file(file_name)
        if start_line is not None and end_line is not None:
            lines = content.split('\n')[start_line - 1:end_line]
            content = '\n'.join(lines)
        return render_template('file.html', content=content)
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
