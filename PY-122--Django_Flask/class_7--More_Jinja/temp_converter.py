"""
Converting celsius to farenheight and vice versa
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/celsius/<temperature>') # route that takes in variable via url
def to_celcius(temperature): # function runs once url is requested
    # Dictionary will be passed as argument to render_template()
    kwargs={
        'converter':convert_to_celsius, # converter is the function that will run within the template
        'temperature':int(temperature),
        'unit':'C'
    }
    # kwargs is sent as an arument to render_template() but first is unpacked into its many values
    return render_template('temp_conversions.html', **kwargs)


@app.route('/fahrenheit/<temperature>')
def to_farenheit(temperature):
    kwargs={
        'converter':convert_to_fahrenheit,
        'temperature':int(temperature),
        'unit':'F'
    }
    return render_template('temp_conversions.html', **kwargs)


def convert_to_celsius(temp):
    return round((temp * 9/5) + 32, 2)

def convert_to_fahrenheit(temp):
    return round((temp - 32) * 5/9, 2)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)