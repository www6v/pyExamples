# 大佬
# https://www.bilibili.com/video/BV1oa411b7c9/
import asyncio
import time

# eventloop event 
# task 所有权

async def say_after(delay, what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"

async def main():

    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print("started at", time.strftime("%X"))
     
    ret1 = await task1
    ret2 =await task2
    print(ret1)
    print(ret2)


    print("finished at", time.strftime("%X"))


    print("started at", time.strftime("%X"))
    await asyncio.gather(
        say_after(1, 'hello'),
        say_after(2, 'world'),
    )
    print("finished at", time.strftime("%X"))    

asyncio.run(main())