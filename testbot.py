import wolframalpha 

client = wolframalpha.Client('APPID')


while True:
    query = str(input('Enter query: '))
    res = client.query(query)
    output = next(res.results).text
    print(output)


