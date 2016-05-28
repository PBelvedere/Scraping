from lxml import html
import requests
#from bs4 import BeautifulSoup
import bs4
test = open('test.txt', 'w')

url = 'http://game.thronemaster.net/?game=63100&show=log'

#Get the webpage
page = requests.get('http://game.thronemaster.net/?game=63100&show=log')

soup = bs4.BeautifulSoup(page.text, 'lxml')

#Acquire the content for the entire page
tree = html.fromstring(page.content)

print ('scraping')
#create a list of players
players = []

for plyr in soup.find_all('nobr'):
    players.append(plyr.get_text())
#Create a list of moves
moves = []

for mvs in soup.find_all(id = True):
    moves.append(mvs.get_text())

phase = []

#Find all phases, used a different syntax due to multiple valigns and multiple small tags
phase = tree.xpath('//th[@valign = "top"]/small/text()')

settings = []
i = 0
setting_set = []

sett = soup.find(style = "padding-left:35px")
for stt in sett.find_all('td'):
    if i%2 == 0:
        settings.append(stt.get_text())
        i+=1
    else:
        setting_set.append(stt.get_text())
        i+=1

print ('done scraping')

settings_table = soup.find('td', valign = 'top', style = 'padding-left:35px')

for stt, stting in zip(settings, setting_set):
    test.write(stt + ' ' + stting + '\n')

for player, move, phse in zip(players, moves, phase):
    line = ("" + player + ": " + phse + " MOVE: " + move  + '\n ')
    test.write(line)

player = [players[0], players[1], players[2]]
win = [0, 0, 0]


for x in range(0, 3):
    if (players[x] + ' wins this game of thrones!') == moves[len(moves)-1]:
        win[x] = 1

print (win, player)