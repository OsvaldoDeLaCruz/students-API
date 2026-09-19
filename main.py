app = FastAPI (title= "student-api", vesrion = APP)


@app.get ("/students")
def list_students ():
    return [{"id":1, "name": "Ana"}, {"id":2,"name":"luis"}]
    