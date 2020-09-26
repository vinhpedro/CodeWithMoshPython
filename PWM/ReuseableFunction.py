
def sentance(message):
    words=message.split(' ')

    dictionary={
        ':)':'😊',
        ':(':'😢'

        }
    out=''
    for item in words:
        out+=dictionary.get(item,item)+' '
    return out


mess=input('>')

print(sentance(mess))