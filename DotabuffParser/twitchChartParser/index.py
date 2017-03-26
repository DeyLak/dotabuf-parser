import codecs
import json
import datetime


def createCSV(json, name):
    result = ''
    prevDate = ''
    currentValue = 0
    currentCount = 0
    for timestampDate, value in json:
        date = datetime.datetime.fromtimestamp(timestampDate / 1000).strftime('%Y-%m-%d')
        if prevDate == '':
            prevDate = date

        if prevDate != date:
            prevDate = date
            currentValue /= currentCount
            currentCount = 0
            result += date + ';' + str(currentValue).replace('.', ',') + '\n'
        else:
            currentCount += 1
            currentValue += value

    with open(name, "w") as f:
        f.write(result)


with codecs.open("../../etc/twitchChartData.json", "r", "utf-8") as f:
    fileText = f.read()
    jsonChart = json.loads(fileText)
    createCSV(jsonChart[0]['data'], 'viewers.csv')
    createCSV(jsonChart[1]['data'], 'streams.csv')


