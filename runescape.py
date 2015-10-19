import urllib.request
import json

#total level class
class totallevel:
    def gettotallevelrank(name):
        
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[0][0]
    
    def gettotallevellevel(name):
    
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[0][1]
    
    def gettotallevelxp(name):

        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[0][2]

#attack level class
class attacklevel:
    def getattacklevelrank(name):
            
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[1][0]

    def getattacklevellevel(name):
            
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[1][1]

    def getattacklevelxp(name):
            
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[1][2]

#defence level class    
class defencelevel:
    def getdefencelevelrank(name):
            
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[2][0]

    def getdefencelevellevel(name):
            
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[2][1]

    def getdefencelevelxp(name):
            
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[2][2]

#strength level class
class strengthlevel:
    def getstrengthlevelrank(name):
            
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[3][0]

    def getstrengthlevellevel(name):
            
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[3][1]

    def getstrengthlevelxp(name):
            
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[3][2]

#hitpoint level class    
class hitpointlevel:
    def gethitpointlevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[4][0]

    def gethitpointlevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[4][1]

    def gethitpointlevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[4][2]

#ranged level class
class rangedlevel:
    def getrangedlevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[5][0]

    def getrangedlevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[5][1]

    def getrangedlevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[5][2]

#prayer level class
class prayerlevel:
    def getprayerlevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[6][0]

    def getprayerlevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[6][1]

    def getprayerlevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[6][2]

#magic level class
class magiclevel:
    def getmagiclevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[7][0]

    def getmagiclevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[7][1]

    def getmagiclevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[7][2]

#cooking level class
class cookinglevel:
    def getcookinglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[8][0]

    def getcookinglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[8][1]

    def getcookinglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[8][2]


#woodcutting level class
class woodcuttinglevel:
    def getwoodcuttinglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[9][0]

    def getwoodcuttinglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[9][1]

    def getwoodcuttinglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[9][2]

#fletching level class
class fletchinglevel:
    def getfletchinglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[10][0]

    def getfletchinglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[10][1]

    def getfletchinglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[10][2]

#fishing level class
class fishinglevel:
    def getfishinglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[11][0]

    def getfishinglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[11][1]

    def getfishinglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[11][2]

#firemaking level class
class firemakinglevel:
    def getfiremakinglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[12][0]

    def getfiremakinglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[12][1]

    def getfiremakinglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[12][2]

#crafting level class
class craftinglevel:
    def getcraftinglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[13][0]

    def getcraftinglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[13][1]

    def getcraftinglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[13][2]

#smithing level class
class smithinglevel:
    def getsmithinglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[14][0]

    def getsmithinglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[14][1]

    def getsmithinglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[14][2]

#mining level class
class mininglevel:
    def getmininglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[15][0]

    def getmininglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[15][1]

    def getmininglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[15][2]

#heblore level class
class heblorelevel:
    def getheblorelevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[16][0]

    def getheblorelevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[16][1]

    def getheblorelevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[16][2]

#agility level class
class agilitylevel:
    def getagilitylevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[17][0]
    
    def getagilitylevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[17][1]

    def getagilitylevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[17][2]

#thieving level class
class thievinglevel:
    def getthievinglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[18][0]

    def getthievinglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[18][1]

    def getthievinglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[18][2]

#slayer level class
class slayerlevel:
    def getslayerlevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[19][0]

    def getslayerlevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[19][1]

    def getslayerlevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[19][2]

#farming level class
class farminglevel:
    def getfarminglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[20][0]

    def getfarminglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[20][1]

    def getfarminglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[20][2]


#runecrafting level class
class runecraftinglevel:
    def getrunecraftinglevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[21][0]

    def getrunecraftinglevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[21][1]

    def getrunecraftinglevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[21][2]

#hunter level class
class hunterlevel:
    def gethunterlevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[22][0]

    def gethunterlevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[22][1]

    def gethunterlevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[22][2]

#construction level class
class constructionlevel:
    def getconstructionlevelrank(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[23][0]

    def getconstructionlevellevel(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[23][1]

    def getconstructionlevelxp(name):
        url = 'http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={0}'.format(name)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()
        format_to_string = str(read_url)

        data_list = [data_line.split(',') for data_line in format_to_string.split()]
        return data_list[23][2]


#grand exchange class

class grand_exchange:
    #gets the global information for a certain item ID.
    def getjson(item_id):
        url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={0}'.format(item_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return json_data
    
    #returns the integer of the current price for a certain item ID.
    def getprice(item_id):
        url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={0}'.format(item_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return int(json_data['item']['current']['price'])
    
    #returns the string of the name for a certain item ID.
    def getname(item_id):
        url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={0}'.format(item_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return str(json_data['item']['name'])

    #returns the boolean wether the item is member or not (True = member, False = non-member)
    def ismember(item_id):
        url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={0}'.format(item_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return bool(json_data['item']['members'])

    #returns the string of the description for a certain item ID.
    def getdescription(item_id):
        url = 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={0}'.format(item_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return str(json_data['item']['description'])



#bestiary class
    
class bestiary:
    #gets the global information for a certain NPC ID.
    def getjson(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return json_data

    #returns the int hitpoint level for a certain NPC ID.
    def gethitpointlevel(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return int(json_data['lifepoints'])

    #returns the int attack level for a certain NPC ID.
    def getattacklevel(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return int(json_data['attack'])

    #returns the int defence level for a certain NPC ID.
    def getdefencelevel(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return int(json_data['defence'])

    #returns the int strength level for a certain NPC ID.
    def getstrengthlevel(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return int(json_data['strength'])

    #returns the int ranged level for a certain NPC ID.
    def getrangedlevel(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return int(json_data['ranged'])

    #returns the int combat level for a certain NPC ID.
    def getcombatlevel(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return int(json_data['level'])

    #returns the string of the description for a certain NPC ID.
    def getdescription(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return str(json_data['description'])

    #returns the string name for a certain NPC ID.
    def getname(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return str(json_data['name'])

    #returns the boolean wether a NPC is aggresive or not
    #[True = agressive, False = not-aggresive]
    def isaggressive(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return bool(json_data['aggressive'])
        
    #returns the boolean wether a player can attack a NPC or not
    #[True = attackable, False= not-attackable]
    def isattackable(npc_id):
        url = 'http://services.runescape.com/m=itemdb_rs/bestiary/beastData.json?beastid={0}'.format(npc_id)
        open_url = urllib.request.urlopen(url)
        read_url = open_url.read().decode()

        json_data = json.loads(read_url)
        return bool(json_data['attackable'])
    

#extra formatings

class extra:
    def getcombatskills(name):
        attack_level = attacklevel.getattacklevellevel(name)
        defence_level = defencelevel.getdefencelevellevel(name)
        strength_level = strengthlevel.getstrengthlevellevel(name)
        hitpoint_level = hitpointlevel.gethitpointlevellevel(name)
        ranged_level = rangedlevel.getrangedlevellevel(name)
        prayer_level = prayerlevel.getprayerlevellevel(name)
        magic_level = magiclevel.getmagiclevellevel(name)
        
        table = str('''
---------------------------
┆ Skill     ┆  Level      
---------------------------
┆ Attack    ┆  {0}        
┆ Strength  ┆  {1}        
┆ Defence   ┆  {2}        
┆ Hitpoint  ┆  {3}        
┆ Ranged    ┆  {4}        
┆ Prayer    ┆  {5}        
┆ Magic     ┆  {6}        
---------------------------
        ''').format(attack_level,
                    strength_level,
                    defence_level,
                    hitpoint_level, 
                    ranged_level,
                    prayer_level,
                    magic_level)  

        return table 
        
