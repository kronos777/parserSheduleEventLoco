import json


from bs4 import BeautifulSoup as bs
from selenium import webdriver


class parserListEventPage:

    def cycleListLink(self, html, season):
        allSectionEvents = html.find_all('div', {'class': ['schedule-section']})
        allLink = []
        allLink.append(season)
        for idx, itemSection in enumerate(allSectionEvents):
            for ids, itemRow in enumerate(itemSection.find_all('div', {'class': ['schedule-row']})):
                link = itemRow.find('a', {'class': ['btn']})
                if link is not None:
                    allLink.append(link.get('href'))
                    print(link.get('href'))
        newData = self.prepareGameForWriteFile(allLink)
        self.dump_json('allFootballEvent', newData)

    def prepareGameForWriteFile(self, gameData):
        file = open('allFootballEvent.json', encoding="utf8")
        dataAllGame = json.load(file)
        dataAllGame.insert(len(dataAllGame), gameData)
        return dataAllGame


    def dump_json(self, fileName, data):
        file_name = fileName + '.json'
        with open(file_name, 'w+', encoding='utf-8') as file:
            try:
                jsonfile = json.dump(data, file, ensure_ascii=False)
                print('Данные сохранены в файле {}'.format(file_name))
            except:
                print('Не удалось сохранить данные!')