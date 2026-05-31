from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preview', methods=['GET', 'POST'])
def preview():
    if request.method == 'POST':
        # Handle file upload or text input
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(filepath)
                with open(filepath, 'r') as f:
                    content = f.read()
                return render_template('preview.html', content=content)
        
        # Handle direct text input
        text_content = request.form.get('text_content', '')
        return render_template('preview.html', content=text_content)
    
    return render_template('preview.html')

if __name__ == '__main__':
    app.run(debug=True)