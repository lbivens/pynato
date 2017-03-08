class Pynato:
    abc = { "A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", 
                      "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel", 
                      "I":"India", "J":"Juliet", "K":"Kilo", "L":"Lima", 
                      "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", 
                      "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango", 
                      "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"Xray", 
                      "Y":"Yankee", "Z":"Zulu", "0":"Zero", "1":"One", 
                      "2":"Two", "3":"Three", "4":"Four", "5":"Five",
                      "6":"Six", "7":"Seven", "8":"Eight", "9":"Niner"} 

    def __init__(self, message): 
        self.message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    def get_nato(self):
        return map(lambda x: self.abc.get(x.upper(),' '), self.message)

    def print_nato(self):
        print(' '.join([x for x in self.get_nato()]))
