from flask import Flask, render_template, request
import json
app = Flask(__name__)

@app.route('/')
def home():
    # return "Hello, World!"
    return render_template('index.html')

@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    room = request.form['room']
    start = request.form['start']
    end = request.form['end']
    print(room, start, end)
    print(type(room), type(start), type(end))
    # open database.json file
    with open('database.json', 'r') as file:
        data = json.load(file)
    # add reservation to database
    # tell if the room is already reserved
    for reservation in data["Reservations"]:
        print(type(reservation["end"]))
        if reservation["room"] == room:
            if start < reservation["end"] and end > reservation["start"]:
                return "Room already reserved!"
    data["Reservations"].append({
        "room": room,
        "start": start,
        "end": end
    })
    # write to database.json file
    with open('database.json', 'w') as file:
        json.dump(data, file)
    return "Reservation submitted!"

if __name__ == '__main__':
    app.run(debug=True)
