from fastapi import FastAPI, BackgroundTasks


app = FastAPI()


@app.get("/")
async def root():
    return "SUCCESS"


def save_to_file(name: str, city=""):
    with open("text_db.txt", mode="w") as text_db:
        row = f"{name}, {city}"
        text_db.write(row)


@app.post("/users")
async def run_async(body: dict, background_tasks: BackgroundTasks):
    background_tasks.add_task(save_to_file, body["name"], body["city"])
    return "SUCCESS"
