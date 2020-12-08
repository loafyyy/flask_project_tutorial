from flask import Flask, render_template, request
from forms import MathForm
from lib.calculation import Exponentiator

def create_app():
    app = Flask(__name__)

    # home page -- renders when URL is base URL + "/"
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    # rendering HTML and passing in variables
    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        # this renders the HTML in hello.html
        # passing in the name variable
        return render_template('hello.html', name=name) 

    # an example of a route displaying a form and handling form submissions
    @app.route('/math', methods=['GET', 'POST'])
    def math():
        form = MathForm(request.form)
        # if submitting the form
        if request.method == 'POST' and form.validate():
            int_input = form.int_input.data
            print("int_input =", int_input)
            squarer = Exponentiator(power=2)
            answer = squarer.exponentiate(int_input)
            return render_template('results.html', answer=answer, input=int_input)
        # if viewing the form
        return render_template('math.html', form=form)

    return app

# start the application if running as main
if __name__ == '__main__':
    app = create_app()
    # localhost port 5000 by default
    # set host='0.0.0.0' to make the server publically accessible
    app.run(host='127.0.0.1', port=5000, debug=True) 