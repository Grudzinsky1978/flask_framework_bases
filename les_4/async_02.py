import asyncio


async def count():
    print('Начало выполнения')
    await asyncio.sleep(1)
    print('Прошла 1 секунда')
    await asyncio.sleep(2)
    print('Прошло ещё 2 секунды')
    return 'Готово'


async def main():
    result = await asyncio.gather(count(), count(), count()) # выполнить вместе
    print(result)


asyncio.run(main())