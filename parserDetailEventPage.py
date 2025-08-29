import json


from bs4 import BeautifulSoup as bs
from selenium import webdriver


class parserDetailEventPage:

"""
    def dump_json(result, name):
       file_name = name + '.json'
       with open(file_name, 'w+', encoding = 'utf-8') as file:
       #with open(file_name, 'a', encoding = 'utf-8') as file:
            try:
                jsonfile = json.dump(result,file, ensure_ascii=False, indent=14)
                print('Данные сохранены в файле {}'.format(file_name))
            except:
                print('Не удалось сохранить данные!')

    def prepareGameForWriteFile(self, gameData):
        file = open('dataJsonFinalAllEvent.json', encoding="utf8")
        dataAllGame = json.load(file)
        dataAllGame.insert(len(dataAllGame), gameData)
        return dataAllGame

    #linkForSave = []
    def parsePositionInFieldPlayer(self, htmlPlayer):
        player = []
        amplua = htmlPlayer.get('class')[1]
        position = htmlPlayer.get('class')[2]
        zapasnoyNaPosicii = ''
        if htmlPlayer.find('span', {'class': ['tooltipstered']}) is not None:
            zapasnoyNaPosicii = htmlPlayer.find('span', {'class': ['tooltipstered']}).get_text()

        numberInSostav = htmlPlayer.find('div', {'class': ['shirtnumber']}).get_text()
        namePlayer = htmlPlayer.find('div', {'class': ['playername']}).get_text()
        player.append({'amplua': amplua, 'position': position, 'zapasnoyNaPosicii': zapasnoyNaPosicii, 'numberInSostav': numberInSostav, 'namePlayer': namePlayer})

        return player


    def parsePositionInField(self, htmlField):
        posInField = []
        commandOne = []
        commandTwo = []
        for idx, item in enumerate(htmlField):
            if 'home' in item.get('class') and len(item.get('class')) >= 3:
                commandOne.append(self.parsePositionInFieldPlayer(item))
            elif len(item.get('class')) >= 3:
                commandTwo.append(self.parsePositionInFieldPlayer(item))

        posInField.append({'commandOne': commandOne, 'commandTwo': commandTwo})
        return posInField

    def parseCommandComposition(self, commandComposition):
        players = []
        compositNumberPlayer = ""
        for element in commandComposition.find_all('tr'):
            if element  is not None:
                if element.find('span', {'class': ['сomposit_num']}) is not None:
                    compositNumberPlayer = element.find('span', {'class': ['сomposit_num']}).get_text()
                if element.find('a') is not None:
                    idPlayer = element.find('a').get('href')
                    fioPlayer = element.find('a').get_text()
                    players.append(
                        {'compositNumberPlayer': compositNumberPlayer, 'idPlayer': idPlayer, 'fioPlayer': fioPlayer})
                else:
                    fioPlayer = element.get_text().strip('\n')
                    players.append(
                        {'compositNumberPlayer': compositNumberPlayer, 'fioPlayer': fioPlayer})


        return players

    def parseHtmlOrbitri(self, orbitriHtml):
        arrOrbitri = []

        for idx, item in enumerate(orbitriHtml.find_all('a')):
            arrOrbitri.append({'name': item.get_text(), 'id': item.get('href')})


        return arrOrbitri

    def parseTrainers(self, trainersHtml):
        trainer = []
        if trainersHtml.find('a') is not None:
            idTrainer = trainersHtml.find('a').get('href')
            fioTrainer = trainersHtml.find('a').get_text()
            trainer.append({'idTrainer': idTrainer, 'fioTrainer': fioTrainer})
        else:
            fioTrainer = trainersHtml.get_text().strip('\n')
            trainer.append({'fioTrainer': fioTrainer})
        return trainer

    def parseInfoAboutEvent(self, eventHtml):
        infoAbout = []
        stadion = []
        viewer = ''
        orbitri = []

        for idx, item in enumerate(eventHtml):
            if idx == 0:
                stadion.append(self.parseHtmlStadion(item))
            elif idx == 1:
                item.find('span', {'class': ['preview_param']}).clear()
                viewer = item.get_text()
            elif idx == 2:
                orbitri.append(self.parseHtmlOrbitri(item))

        infoAbout.append({'stadion': stadion, 'viewer': viewer, 'orbitri': orbitri})

        return infoAbout

    def parseHtmlStadion(self, stadionHtml):
        stHtml = []
        stadionName = ''
        stadionHref = ''
        place = ''
        temperatura = ''
        osadki = ''
        for idx, item in enumerate(stadionHtml):
            if idx == 1:
                continue
            elif idx == 3:
                stadionName = item.find('a').get_text()
                stadionHref = item.find('a').get('href')
            elif idx == 4:
                place = item.get_text()
            elif idx == 6:
                temperatura = item.get_text()
            elif idx == 7:
                osadki = item.get_text()

        stHtml.append({'stadionName': stadionName,
                        'stadionHref': stadionHref,
                        'place': place,
                        'temperatura': temperatura,
                        'osadki': osadki})
        return stHtml


    def parseStatistickMatch(self, statHtml):
        stat = []
        a = ""
        b = ""
        for idx, item in enumerate(statHtml.find_all('div', {'class': ['stats_inf']})):
            if idx == 0:
                a = item.get_text()
                #stat.append({'commandOneScore', item.get_text()})
            elif idx == 1:
                b = item.get_text()
                #stat.append({'commandTwoScore', item.get_text()})

        stat.append({'statTitle': statHtml.find('div', {'class': ['stats_title']}).get_text(), 'commandOneScore': a, 'commandTwoScore': b})

        return stat

    def getDataPageEvent(self, soup):
        responseEvent = []
        commandOne = []
        commandTwo = []
        title = soup.find('div', {'class': ['block_header']}).get_text().strip('\n')

        commandOneInfo = soup.find('div', {'class': ['live_game left']})
        commandOneName = commandOneInfo.find('div', {'class': ['live_game_ht']}).get_text().strip('\n')
        commandOneHref = commandOneInfo.find('a').get('href')
        commandOneScore = commandOneInfo.find('div', {'class': ['live_game_goal']}).get_text().strip('\n')

        commandTwoInfo = soup.find('div', {'class': ['live_game right']})
        commandTwoName = commandTwoInfo.find('div', {'class': ['live_game_at']}).get_text().strip('\n')
        commandTwoHref = commandTwoInfo.find('a').get('href')
        commandTwoScore = commandTwoInfo.find('div', {'class': ['live_game_goal']}).get_text().strip('\n')

        statusEvent = ""
        if soup.find('div', {'class': ['live_game_status']}) is not None:
            statusEvent = soup.find('div', {'class': ['live_game_status']}).get_text().strip('\n')

        commandOne.append({'title': commandOneName, 'href': commandOneHref, 'score': commandOneScore})
        commandTwo.append({'title': commandTwoName, 'href': commandTwoHref, 'score': commandTwoScore})


       # hronologyMathAllDiv = soup.find('div', {'class': ['block_body_nopadding padv15']})
        if soup.find('div', {'class': ['live_game_status']}) is not None:
            hronologyMathAllDivParent = soup.find('div', {'class': ['live_game_status']})
            hronologyMathAllDiv = str(hronologyMathAllDivParent.find_next_siblings()) #html for hronology
            responseEvent.append({'hronologyMathAllDiv': hronologyMathAllDiv})
        #print(hronologyMathAllDiv)1
        #for idx, x in enumerate(hronologyMathAllDiv):
        #   print(idx, x)

        if soup.find('div', {'id': ['tm-lineup']}) is not None:
            teamCompositionParent = soup.find('div', {'id': ['tm-lineup']})
            teamComposition = teamCompositionParent.find_all('div', {'class': ['сomposit_block']})
            for idx, players in enumerate(teamComposition):
                if players is not None:
                    if idx == 0:
                       commandOne.append({'osnovnoyTeam': self.parseCommandComposition(players)})
                    elif idx == 1:
                      commandTwo.append({'osnovnoyTeam': self.parseCommandComposition(players)})
                    elif idx == 2:
                        commandOne.append({'mainCoach': self.parseTrainers(players)})
                    elif idx == 3:
                        commandTwo.append({'mainCoach': self.parseTrainers(players)})


        if soup.find('div', {'id': ['tm-subst']}) is not None:
            teamCompositionZapasParent = soup.find('div', {'id': ['tm-subst']})
            teamCompositionZapas = teamCompositionZapasParent.find_all('div', {'class': ['сomposit_block']})
            for idx, players in enumerate(teamCompositionZapas):
                if idx == 0:
                  commandOne.append({'zapasTeam': self.parseCommandComposition(players)})
                elif idx == 1:
                  commandTwo.append({'zapasTeam': self.parseCommandComposition(players)})

        #print(commandTwo)
        statMatch = []

        if soup.find('div', {'id': ['stat-tp0']}) is not None:
            statMatchParent = soup.find('div', {'id': ['stat-tp0']})
            statItemBlocks = statMatchParent.find_all('div', {'class': ['stats_item']})
            for idx, itemStat in enumerate(statItemBlocks):
                statMatch.append(self.parseStatistickMatch(itemStat))
            responseEvent.append({'statisticksEvent': statMatch})

        #responseEvent.append({'commandOne': commandOne, 'commandTwo': commandTwo})
        if soup.find('div', {'id': ['preview']}) is not None:
            infoAboutEventParent = soup.find('div', {'id': ['preview']})
            infoAboutEvent = infoAboutEventParent.find_all('div', {'class': ['preview_item']})
            infoAboutEventData = self.parseInfoAboutEvent(infoAboutEvent)
            responseEvent.append({'infoAboutEvent': infoAboutEventData})

        #positionInField = []
        if soup.find('div', {'id': ['tm-players-position-view']}) is not None:
            positionInFieldParent = soup.find('div', {'id': ['tm-players-position-view']})
            positionInField = positionInFieldParent.find_all('div', {'class': ['player_position']})
            positionInFieldData = self.parsePositionInField(positionInField)
            responseEvent.append({'positionInFieldData': positionInFieldData})
        #hronologyMathAllDivArr = [{'hronologyMathAllDiv': hronologyMathAllDiv}]
        #print(hronologyMathAllDivArr)
        responseEvent.append(
            {'title': title, 'statusEvent': statusEvent,
             'commandOne': commandOne, 'commandTwo': commandTwo})


        return responseEvent
"""




"""
lnk = "https://soccer365.ru/games/11497254/"
lnk = "https://soccer365.ru/games/14777881/"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(lnk)
htmlPage = driver.page_source
soup = bs(htmlPage)
dataEvent = ParserEventPage().getDataPageEvent(soup)
dataJson = json.dumps(dataEvent)
ParserEventPage.dump_json(dataEvent, 'firstFile')
time.sleep(1)
driver.close()
"""