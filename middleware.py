from fastapi import Request
from logger import logger
import time
from datetime import datetime



async def log_middleware(request:Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    log_dict = {
        "headers": request.headers,
        "method": request.method,
        "process_time": process_time,
        "time_of_request": datetime.now()
    }

    logger.info(log_dict, extra=log_dict)

    return response