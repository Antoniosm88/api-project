from src.app import app

@app.route ("/")
def Welcome():
    return "Hola¡¡ Esta es mi primera API"