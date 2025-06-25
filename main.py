from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # debug = true: mean that the website vil update in real time if changes are made in the code