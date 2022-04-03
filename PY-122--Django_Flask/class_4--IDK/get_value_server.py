from flask import Flask

app = Flask(__name__)

@app.route('/<note>')
def idk_yet(note):
    lyrics = {'do': 'Doe, a deer a female deer',
         're': 'Ray, A drop of golden sun',
         'me': 'Me, a name I call myself',
         'fa': 'Far, a long long way to run',
         'so': 'Sew, a needle pulling thread',
         'la': 'La, a note to follow so',
         'ti': 'Tea, a drink with jam and bread'}
    if note in lyrics:
        return lyrics[note]
    else: return 'Note not found'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)