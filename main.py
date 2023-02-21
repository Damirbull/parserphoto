from icrawler.builtin import GoogleImageCrawler

parser_photo = GoogleImageCrawler(storage={'root_dir': 'C:/Users/ACER/Desktop/bbc'})

print('Сколько нужно скачать фото?')

photo = int(input())

print("Введите данные фото")
name = str(input())

parser_photo.crawl(keyword=name, max_num=photo)