from flask import Flask, render_template, request, redirect, url_for
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

reminders = []
MAX_REMINDERS = 10

class Reminder:
    def __init__(self, title, date, time, repeat, sound, index):
        self.title = title
        self.date = date
        self.time = time
        self.repeat = repeat
        self.sound = sound
        self.index = index

@app.route('/')
def home():
    reminders_dict = [
        {
            'title': r.title,
            'date': r.date,
            'time': r.time,
            'repeat': r.repeat,
            'sound': r.sound,
            'index': r.index
        }
        for r in reminders
    ]
    return render_template('index.html', reminders=reminders_dict)


@app.route('/save', methods=['POST'])
def save():
    if len(reminders) >= MAX_REMINDERS:
        return "Reminder maksimal 10!", 400

    title = request.form.get('title')
    date = request.form.get('date')
    time = request.form.get('time')
    repeat = request.form.get('repeat')
    file = request.files.get('sound')

    if not all([title, date, time, repeat, file]):
        return "Semua field harus diisi.", 400

    if file and file.filename.endswith('.mp3'):
        filename = str(uuid.uuid4()) + "_" + file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
    else:
        return "Format file tidak valid (harus .mp3)", 400

    index = len(reminders)
    reminders.append(Reminder(title, date, time, repeat, "/" + filepath.replace("\\", "/"), index))
    return redirect(url_for('home'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    global reminders
    reminders = [r for r in reminders if r.index != index]
    return redirect(url_for('home'))

if __name__ == '__main__':
    os.makedirs('static/uploads', exist_ok=True)
    app.run(debug=True)
