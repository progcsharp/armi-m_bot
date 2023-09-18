import asyncio


async def event_loop(loop, delay):
    # код для запроса

    when_to_call = loop.time() + delay
    loop.call_at(when_to_call, my_func)


def my_func():
    loop = asyncio.get_event_loop()
    delay = 60.0
    asyncio.ensure_future(event_loop(loop, delay))



