async def init(data):
    print("Initialized hello.py")

async def run(data):
    await data.Channel.send(f"Hello, {data.Message.author}")

async def help(data):
    pass