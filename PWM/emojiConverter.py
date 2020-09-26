enter =input('>')
sentance= enter.split(' ')

emojies={
    ':)': '😊',
    ':(':'😢'
}
output=''
for  item in sentance:
    output+=emojies.get(item,item) + ' '
print(output)