# Copy and paste this code into VS code and name it test_flask.py
from flask import Flask

app = Flask(__name__)


def factors(x):
	numbers = []
	for i in range(1, x + 1):
		if x % i == 0:
			numbers.append(i)
	return f"The factors of {x} are: {numbers}"

def prime_factors(self, start=0):
		if start == 0: start == self.start
		return [num for num in range(1,start+1) if start % num == 0 and self.check_prime(num) == True]

def check_prime(start):
	x = ""
	if start < 4: x = ""
	if start % 2 == 0: x = "not"
	i = 3
	while i < 20:
		if start % i == 0: x = "not"
		i+=2
	return f"{start} is {x} prime."


@app.route('/factors/<number>')
def ops1(number):
    return factors(int(number))

@app.route('/prime_factors/<number>')
def ops2(number):
    return prime_factors(int(number))

@app.route('/is_prime/<number>')
def ops3(number):
    return str(check_prime(int(number)))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=5500)

