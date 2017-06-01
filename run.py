import asyncio.subprocess
import sys

@asyncio.coroutine
def run_code(code):

    create = asyncio.create_subprocess_exec(sys.executable, '-c', code,
                                                stdout=asyncio.subprocess.PIPE)

    proc = yield from create

    # Read one line of output
    data = yield from proc.stdout.read()
    line = data.decode('utf-8').rstrip()

    # Wait for the subprocess exit
    yield from proc.wait()
    return line

if sys.platform == "win32":
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
else:
    loop = asyncio.get_event_loop()

code = """import sys
print(sys.version)
print("한글")"""
date = loop.run_until_complete(run_code(code))
print("Current date: %s" % date)
loop.close()