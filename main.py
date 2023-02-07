from fastapi import FastAPI, BackgroundTasks
import asyncio
import logging


app = FastAPI(debug=True)
logger = logging.getLogger("uvicorn.error")
# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/issues/19


@app.get("/")
async def root():
    return "SUCCESS"


async def log_to_a_file(name: str, city=""):
    logger.info("log_to_a_file function called...")
    with open("users_log.txt", mode="a") as log_file:
        row = f"{name}, {city}\n"
        log_file.write(row)


@app.post("/users")
async def run_async(body: dict, background_tasks: BackgroundTasks):
    logger.info("api called!")
    logger.info("adding task to background tasks...")
    background_tasks.add_task(log_to_a_file, body["name"], body["city"])
    logger.info("returning response...")
    return "SUCCESS"


@app.post("/asyncio-ensure-future")
async def asyncio_ensure_future(body: dict):
    logger.info("api called!")
    logger.info("adding task to background tasks...")
    asyncio.ensure_future(log_to_a_file(body["name"], body["city"]))
    logger.info("returning response...")
    return "SUCCESS"
