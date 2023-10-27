from django.shortcuts import render

import crypto

def home(request):
	import requests
	import json

	#get crypto price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,BNB,XRP,USDC,SOL,DOGE,ADA,TRX,TON,LINK,MATIC,WBTC,DAI,DOT,LTC,BCH,SHIB,AVAX,LEO,TUSD,XLM,XMR,OKB,ATOM,UNI,ETC,BUSD,HBAR,FIL,LDO,APT,ICP,CRO,MKR,VET,QNT,OP,ARB,MNT,NEAR,AAVE,INJ,GRT,STX,BSV,ALGO,RNDR,IMX,RUNE,EGLD,USDD,XDC,AXS,SAND,XTZ,EOS,MANA,THETA,SNX,MINA,BGB,FTM,NEO,KAVA,XEC,FLOW,PEPE,CFX,XAUt,PAXG,CHZ,USDP,RPL,APE,IOTA,GALA,ZEC,KCS,FXS,TWT,CRV,KLAY,dYdX,GMX&tsyms=USD")
	price = json.loads(price_request.content)

	#get crypto news
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'price':  price })

  
def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote': quote, 'crypto' : crypto})

def news(request):
	import requests
	import json
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'news.html', {'api' : api}) 