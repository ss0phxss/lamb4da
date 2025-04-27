import os
import time
import functools

initial_files = set(os.listdir('/tmp'))
initial_env = dict(os.environ)

def seccheck():
    current_files = set(os.listdir('/tmp'))
    new_files = current_files - initial_files
    if new_files:
        print(f"Suspicious files detected in /tmp: {new_files}")

    for key, value in os.environ.items():
        if key not in initial_env:
            print(f"Warning: New environment variable detected: {key}")
        elif initial_env[key] != value:
            print(f"Environment variable {key} value changed")

def safe_lmbd(func):
    @functools.wraps(func)
    def wrapper(event, context):
        start_time = time.time()
        
        seccheck()
        
        # original handler
        result = func(event, context)
        
        duration = time.time() - start_time
        if duration > 5:  # as example
            print(f"Lambda execution time suspiciously long: {duration:.2f}s")
        
        return result
    return wrapper

@safe_lmbd
def handler(event, context):
    # Lambda function ....
    return {"statusCode": 200}
