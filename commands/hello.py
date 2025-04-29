async def main(data):
    await data.Channel.send(f"Hello, {data.Message.author}")