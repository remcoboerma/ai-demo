from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)

def get_images():
    img_dir = Path('static/images')
    return sorted(p.name for p in img_dir.glob('*') if p.suffix.lower() in {'.jpg', '.jpeg', '.png', '.gif', '.webp'})

@app.route('/')
def gallery():
    return render_template('gallery.html', images=get_images())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
