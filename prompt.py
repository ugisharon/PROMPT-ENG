import openai
import json
import requests

openai.api_key = #enter api key

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": userPrompt}]
    )
    return completion.choices[0].message.content

def GetBitcoinPrices():

    #define the API endpoint and query parameters
    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"
    querystring = {
        "referenceCurrencyUuid":"yhjMzLPhuIDl",
        "timePeriod":"7d"
        }
    #define the request headers with API key and host

    headers = {
	"X-RapidAPI-Key": "e94c6d58e2msh8a0912490ecce35p1a1750jsn7e304b764e46",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }
    #send a GET response to the API endpoint with query parameters and headers

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    #Parse the response data as a JSON object
    JSONResult =json.loads(response.text)
    history = JSONResult["data"]["history"]
    #Extract the "price" field from each element in the "history" array and add to a list
    prices = []
    for change in history:
        prices.append(change["price"])
    #join the list of prices into a comma-seperate string
    pricesList = ','.join(prices)
    #return the comma-seperated string of prices
    return pricesList

bitcoinPrices = GetBitcoinPrices()
chatGPTPrompt = """You are an expert crypto trader with more than 10 years of experience,
I will provie you with a list of bitcoin prices for the last 7 days
can you provide me with a technical analysis
of Bitcoin base on these prices, here is what I want:
Price overview,
Moving Averages
Relative Strength Index (RSI)
Moving Average Convergence Divergence (MACD)
Advice and Suggestion
Do I buy or sell?
Please be as detailed as you can and explain in a way any beginner can understand.
Here is the price list: {bitcoinPrices}"""

analysis = BasicGeneration(chatGPTPrompt)

print(analysis)