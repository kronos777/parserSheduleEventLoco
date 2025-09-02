import json


from bs4 import BeautifulSoup as bs
from selenium import webdriver


class parserDetailEventPage:

    def getDetailEventInfo(self, pageHtml, season):
        gameData = []
        seasonEvent = season
        dateTimeEvent = pageHtml.find('title').get_text().split(',')
        dateTimeEvent = dateTimeEvent[1].split('|')
        dateTimeEvent = dateTimeEvent[0].strip()
        dateTimeHoursEvent = pageHtml.find('div', {'class': ['match-detail-time']}).get_text().strip()
        dateTimeEvent = dateTimeEvent + " " + dateTimeHoursEvent
        placeEvent = pageHtml.find('div', {'class': ['match-detail-stadium']}).get_text().strip()
        typeСompetition = pageHtml.find('div', {'class': ['match-detail-tour']}).find_all('div')[0].get_text().strip()
        stageСompetition = pageHtml.find('div', {'class': ['match-detail-tour']}).find_all('div')[1].get_text().strip()
        commandOne = pageHtml.find_all('div', {'class': ['match-detail-team-title']})[0].get_text().strip()
        commandOneScore = pageHtml.find('div', {'class': ['match-detail-score']}).get_text().strip().split(':')[0]
        commandOneLogo = pageHtml.find_all('div', {'class': ['match-detail-team-logo']})[0].find('img').get('src')
        commandOneCity = pageHtml.find_all('div', {'class': ['match-detail-team-city']})[0].get_text().strip()
        commandOneEvents = []

        commandTwo = pageHtml.find_all('div', {'class': ['match-detail-team-title']})[1].get_text().strip()
        if len(pageHtml.find('div', {'class': ['match-detail-score']}).get_text().strip().split(':')) > 1:
            commandTwoScore = pageHtml.find('div', {'class': ['match-detail-score']}).get_text().strip().split(':')[1]
        else:
            commandTwoScore = ""
        commandTwoLogo = pageHtml.find_all('div', {'class': ['match-detail-team-logo']})[1].find('img').get('src')
        commandTwoCity = pageHtml.find_all('div', {'class': ['match-detail-team-city']})[1].get_text().strip()
        commandTwoEvents = []
        # timeline-event

        for element in pageHtml.find_all('div', {'class': ['event-home']}):
            if element is not None:
                eventDateTime = element.find('div', {'class': ['timeline-event-time']})
                eventDetil = element.find('div', {'class': ['timeline-event-caption']})
                commandOneEvents.append({'eventDateTime': eventDateTime, 'eventDetil': eventDetil})

        for element in pageHtml.find_all('div', {'class': ['event-away']}):
            if element is not None:
                eventDateTime = element.find('div', {'class': ['timeline-event-time']})
                eventDetil = element.find('div', {'class': ['timeline-event-caption']})
                commandTwoEvents.append({'eventDateTime': eventDateTime, 'eventDetil': eventDetil})

        gameData.append({
            'seasonEvent': seasonEvent,
            'dateTimeEvent': dateTimeEvent,
            'placeEvent': placeEvent,
            'typeСompetition': typeСompetition,
            'stageСompetition': stageСompetition,
            'commandOne': commandOne,
            'commandOneScore': commandOneScore,
            'commandOneLogo': commandOneLogo,
            'commandOneCity': commandOneCity,
            'commandOneEvents': str(commandOneEvents),
            'commandTwo': commandTwo,
            'commandTwoScore': commandTwoScore,
            'commandTwoLogo': commandTwoLogo,
            'commandTwoCity': commandTwoCity,
            'commandTwoEvents': str(commandTwoEvents)
        })

        return gameData

    def dump_json(self, result, name):
       file_name = name + '.json'
       with open(file_name, 'w+', encoding = 'utf-8') as file:
            try:
                jsonfile = json.dump(result,file, ensure_ascii=False, indent=15)
                print('Данные сохранены в файле {}'.format(file_name))
            except:
                print('Не удалось сохранить данные!')

    def prepareGameForWriteFile(self, gameData):
        file = open('allFootballEventDetail.json', encoding="utf8")
        dataAllGame = json.load(file)
        dataAllGame.insert(len(dataAllGame), gameData)
        return dataAllGame
