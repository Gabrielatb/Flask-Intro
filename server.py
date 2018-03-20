"""Greeting Flask app."""

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISS = ['stinky', 'lame-sauce', 'derp']


@app.route('/')
def start_here():
    """Home page."""

    return """
          <!doctype html>
          <html>
            <head>
            </head>
            <body>
              Hi! This is the home page.<br>
              <a href="/hello">Hello Form</a>
            </body>
          </html>
          """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    comp_options = ""
    for compliment in AWESOMENESS:
        option = "<option value='{}'>{}</option>".format(compliment, compliment)
        comp_options = comp_options + option

    diss_options = ""
    for diss in DISS:
        option = "<option value='{}'>{}</option>".format(diss, diss)
        diss_options = diss_options + option

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          <br>
          Pick a Compliment:
          <select name="compliment">
            {compliment}
          </select><br>
          <br>
          <input type="submit" value="Get Compliment">

        </form><br>
        <form action="/diss">
          What's your name? <input type="text" name="person"><br>
          <br>
          Pick a "Compliment":
          <select name="diss">
            {diss}
          </select><br>
          <br>
          <input type="submit" name="diss_button" value='Get "Compliment"'>

        </form>
      </body>
    </html>
    """.format(compliment=comp_options, diss=diss_options)


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """.format(player=player, diss=diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
