from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # Récupérer les données du formulaire
    site_name = request.form.get('site_name')
    site_description = request.form.get('site_description')
    site_color = request.form.get('site_color')
    
    # Créer un dossier pour le site
    site_folder = os.path.join('generated_sites', site_name)
    os.makedirs(site_folder, exist_ok=True)
    
    # Générer le fichier HTML
    html_content = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_name}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: {site_color};
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: {site_color};
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{site_name}</h1>
        <p>{site_description}</p>
    </div>
</body>
</html>
"""
    
    with open(os.path.join(site_folder, 'index.html'), 'w') as f:
        f.write(html_content)
    
    return redirect(url_for('preview', site_name=site_name))

@app.route('/preview/<site_name>')
def preview(site_name):
    return render_template('preview.html', site_name=site_name)

if __name__ == '__main__':
    app.run(debug=True)