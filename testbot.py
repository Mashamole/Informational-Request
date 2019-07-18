import wolframalpha 

client = wolframalpha.Client('TQEPQQ-G68H4RU9U3')


while True:
    query = str(input('Enter query: '))
    res = client.query(query)
    output = next(res.results).text
    print(output)


