from fastapi import FastAPI, BackgroundTasks


app = FastAPI(debug=True)


@app.get("/")
async def root():
    return "SUCCESS"


def log_to_a_file(name: str, city=""):
    print("log_to_a_file function called...")
    with open("users_log.txt", mode="a") as log_file:
        row = f"{name}, {city}\n"
        log_file.write(row)


@app.post("/users")
async def run_async(body: dict, background_tasks: BackgroundTasks):
    print("api called!")
    print("adding task to background tasks...")
    background_tasks.add_task(log_to_a_file, body["name"], body["city"])
    print("returning response...")
    return "SUCCESS"
