import asyncio
from pathlib import Path


async def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        contents = f.read()
        # do some processing with the file contents
        print(f'{f.name} содержит <<<{contents[:13]}...>>>') # имя файла и первый 13 символов содержания


async def main():
    # dir_path = Path('/path/to/directory')
    dir_path = Path('.') # путь к текущему каталогу
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()] # итерируемся по всем объектам (файлам, каталогам, ссылкам),
                                                                                        # и если это файл, то его название помещается в список file_path
    tasks = [asyncio.create_task(process_file(file_path)) for file_path in file_paths] # запускается столько корутин, сколько найдено файлов
    await asyncio.gather(*tasks) # одновременный запуск корутин из списка tasks



if __name__ == '__main__':
    asyncio.run(main()) # корутина


# Асинхронный код выполняется внутри одного потока