# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
import base64
import hashlib
import math
import json
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import NotSupported
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import InvalidNonce


class bitfinex (Exchange):

    def describe(self):
        return self.deep_extend(super(bitfinex, self).describe(), {
            'id': 'bitfinex',
            'name': 'Bitfinex',
            'countries': 'VG',
            'version': 'v1',
            'rateLimit': 1500,
            # new metainfo interface
            'has': {
                'CORS': False,
                'createDepositAddress': True,
                'deposit': True,
                'fetchClosedOrders': True,
                'fetchDepositAddress': True,
                'fetchFees': True,
                'fetchFundingFees': True,
                'fetchMyTrades': True,
                'fetchOHLCV': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchTickers': True,
                'fetchTradingFees': True,
                'withdraw': True,
            },
            'timeframes': {
                '1m': '1m',
                '5m': '5m',
                '15m': '15m',
                '30m': '30m',
                '1h': '1h',
                '3h': '3h',
                '6h': '6h',
                '12h': '12h',
                '1d': '1D',
                '1w': '7D',
                '2w': '14D',
                '1M': '1M',
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/27766244-e328a50c-5ed2-11e7-947b-041416579bb3.jpg',
                'api': 'https://api.bitfinex.com',
                'www': 'https://www.bitfinex.com',
                'doc': [
                    'https://bitfinex.readme.io/v1/docs',
                    'https://github.com/bitfinexcom/bitfinex-api-node',
                ],
            },
            'api': {
                'v2': {
                    'get': [
                        'candles/trade:{timeframe}:{symbol}/{section}',
                        'candles/trade:{timeframe}:{symbol}/last',
                        'candles/trade:{timeframe}:{symbol}/hist',
                    ],
                },
                'public': {
                    'get': [
                        'book/{symbol}',
                        # 'candles/{symbol}',
                        'lendbook/{currency}',
                        'lends/{currency}',
                        'pubticker/{symbol}',
                        'stats/{symbol}',
                        'symbols',
                        'symbols_details',
                        'tickers',
                        'today',
                        'trades/{symbol}',
                    ],
                },
                'private': {
                    'post': [
                        'account_fees',
                        'account_infos',
                        'balances',
                        'basket_manage',
                        'credits',
                        'deposit/new',
                        'funding/close',
                        'history',
                        'history/movements',
                        'key_info',
                        'margin_infos',
                        'mytrades',
                        'mytrades_funding',
                        'offer/cancel',
                        'offer/new',
                        'offer/status',
                        'offers',
                        'offers/hist',
                        'order/cancel',
                        'order/cancel/all',
                        'order/cancel/multi',
                        'order/cancel/replace',
                        'order/new',
                        'order/new/multi',
                        'order/status',
                        'orders',
                        'orders/hist',
                        'position/claim',
                        'positions',
                        'summary',
                        'taken_funds',
                        'total_taken_funds',
                        'transfer',
                        'unused_taken_funds',
                        'withdraw',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': True,
                    'percentage': True,
                    'maker': 0.1 / 100,
                    'taker': 0.2 / 100,
                    'tiers': {
                        'taker': [
                            [0, 0.2 / 100],
                            [500000, 0.2 / 100],
                            [1000000, 0.2 / 100],
                            [2500000, 0.2 / 100],
                            [5000000, 0.2 / 100],
                            [7500000, 0.2 / 100],
                            [10000000, 0.18 / 100],
                            [15000000, 0.16 / 100],
                            [20000000, 0.14 / 100],
                            [25000000, 0.12 / 100],
                            [30000000, 0.1 / 100],
                        ],
                        'maker': [
                            [0, 0.1 / 100],
                            [500000, 0.08 / 100],
                            [1000000, 0.06 / 100],
                            [2500000, 0.04 / 100],
                            [5000000, 0.02 / 100],
                            [7500000, 0],
                            [10000000, 0],
                            [15000000, 0],
                            [20000000, 0],
                            [25000000, 0],
                            [30000000, 0],
                        ],
                    },
                },
                'funding': {
                    'tierBased': False,  # True for tier-based/progressive
                    'percentage': False,  # fixed commission
                    'deposit': {
                        'BTC': 0.0005,
                        'IOTA': 0.5,
                        'ETH': 0.01,
                        'BCH': 0.01,
                        'LTC': 0.1,
                        'EOS': 0.1,
                        'XMR': 0.04,
                        'SAN': 0.1,
                        'DASH': 0.01,
                        'ETC': 0.01,
                        'XRP': 0.02,
                        'YYW': 0.1,
                        'NEO': 0,
                        'ZEC': 0.1,
                        'BTG': 0,
                        'OMG': 0.1,
                        'DATA': 1,
                        'QASH': 1,
                        'ETP': 0.01,
                        'QTUM': 0.01,
                        'EDO': 0.5,
                        'AVT': 0.5,
                        'USDT': 0,
                    },
                    'withdraw': {
                        'BTC': 0.0008,
                        'IOTA': 0.5,
                        'ETH': 0.01,
                        'ETC': 0.01,
                        'BCH': 0.0001,
                        'LTC': 0.001,
                        'EOS': 0.8609,
                        'XMR': 0.04,
                        'SAN': 3.2779,
                        'DASH': 0.01,
                        'XRP': 0.02,
                        'YYW': 40.543,
                        'NEO': 0,
                        'ZEC': 0.001,
                        'BTG': 0,
                        'OMG': 0.5897,
                        'DATA': 52.405,
                        'FUN': 90.402,
                        'GNT': 15.435,
                        'MNA': 76.821,
                        'BAT': 17.223,
                        'SPK': 24.708,
                        'QASH': 6.1629,
                        'ETP': 0.01,
                        'QTUM': 0.01,
                        'EDO': 2.5238,
                        'AVT': 3.2495,
                        'USDT': 20.0,
                        'ZRX': 5.6442,
                        'TNB': 87.511,
                        'SNT': 32.736,
                    },
                },
            },
            'exceptions': {
                'exact': {
                    'Order could not be cancelled.': OrderNotFound,  # non-existent order
                    'No such order found.': OrderNotFound,  # ?
                    'Order price must be positive.': InvalidOrder,  # on price <= 0
                    'Could not find a key matching the given X-BFX-APIKEY.': AuthenticationError,
                    'This API key does not have permission for self action': AuthenticationError,  # authenticated but not authorized
                    'Key price should be a decimal number, e.g. "123.456"': InvalidOrder,  # on isNaN(price)
                    'Key amount should be a decimal number, e.g. "123.456"': InvalidOrder,  # on isNaN(amount)
                    'ERR_RATE_LIMIT': DDoSProtection,
                    'Nonce is too small.': InvalidNonce,
                },
                'broad': {
                    'Invalid order: not enough exchange balance for ': InsufficientFunds,  # when buying cost is greater than the available quote currency
                    'Invalid order: minimum size for ': InvalidOrder,  # when amount below limits.amount.min
                    'Invalid order': InvalidOrder,  # ?
                },
            },
        })

    def common_currency_code(self, currency):
        currencies = {
            'DSH': 'DASH',  # Bitfinex names Dash as DSH, instead of DASH
            'QTM': 'QTUM',
            'BCC': 'CST_BCC',
            'BCU': 'CST_BCU',
            'IOT': 'IOTA',
            'DAT': 'DATA',
        }
        return currencies[currency] if (currency in list(currencies.keys())) else currency

    def fetch_funding_fees(self, params={}):
        self.load_markets()
        response = self.privatePostAccountFees(params)
        fees = response['withdraw']
        withdraw = {}
        ids = list(fees.keys())
        for i in range(0, len(ids)):
            id = ids[i]
            code = id
            if id in self.currencies_by_id:
                currency = self.currencies_by_id[id]
                code = currency['code']
            withdraw[code] = self.safe_float(fees, id)
        return {
            'info': response,
            'withdraw': withdraw,
            'deposit': withdraw,  # only for deposits of less than $1000
        }

    def fetch_trading_fees(self, params={}):
        self.load_markets()
        response = self.privatePostSummary(params)
        return {
            'info': response,
            'maker': self.safe_float(response, 'maker_fee'),
            'taker': self.safe_float(response, 'taker_fee'),
        }

    def load_fees(self):
        #  # PHP does flat copying for arrays
        #  # setting fees on the exchange instance isn't portable, unfortunately...
        #  # self should probably go into the base class as well
        # funding = self.fees['funding']
        # fees = self.fetch_funding_fees()
        # funding = self.deep_extend(funding, fees)
        # return funding
        raise NotSupported(self.id + ' loadFees() not implemented yet')

    def fetch_fees(self):
        fundingFees = self.fetch_funding_fees()
        tradingFees = self.fetch_trading_fees()
        return self.deep_extend(fundingFees, tradingFees)

    def fetch_markets(self):
        markets = self.publicGetSymbolsDetails()
        result = []
        for p in range(0, len(markets)):
            market = markets[p]
            id = market['pair'].upper()
            baseId = id[0:3]
            quoteId = id[3:6]
            base = self.common_currency_code(baseId)
            quote = self.common_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'price': market['price_precision'],
                'amount': market['price_precision'],
            }
            limits = {
                'amount': {
                    'min': float(market['minimum_order_size']),
                    'max': float(market['maximum_order_size']),
                },
                'price': {
                    'min': math.pow(10, -precision['price']),
                    'max': math.pow(10, precision['price']),
                },
            }
            limits['cost'] = {
                'min': limits['amount']['min'] * limits['price']['min'],
                'max': None,
            }
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'active': True,
                'precision': precision,
                'limits': limits,
                'lot': math.pow(10, -precision['amount']),
                'info': market,
            })
        return result

    def fetch_balance(self, params={}):
        self.load_markets()
        balanceType = self.safe_string(params, 'type', 'exchange')
        balances = self.privatePostBalances()
        result = {'info': balances}
        for i in range(0, len(balances)):
            balance = balances[i]
            if balance['type'] == balanceType:
                currency = balance['currency']
                uppercase = currency.upper()
                uppercase = self.common_currency_code(uppercase)
                account = self.account()
                account['free'] = float(balance['available'])
                account['total'] = float(balance['amount'])
                account['used'] = account['total'] - account['free']
                result[uppercase] = account
        return self.parse_balance(result)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        orderbook = self.publicGetBookSymbol(self.extend({
            'symbol': self.market_id(symbol),
        }, params))
        return self.parse_order_book(orderbook, None, 'bids', 'asks', 'price', 'amount')

    def fetch_tickers(self, symbols=None, params={}):
        self.load_markets()
        tickers = self.publicGetTickers(params)
        result = {}
        for i in range(0, len(tickers)):
            ticker = tickers[i]
            if 'pair' in ticker:
                id = ticker['pair']
                if id in self.markets_by_id:
                    market = self.markets_by_id[id]
                    symbol = market['symbol']
                    result[symbol] = self.parse_ticker(ticker, market)
                else:
                    raise ExchangeError(self.id + ' fetchTickers() failed to recognize symbol ' + id + ' ' + self.json(ticker))
            else:
                raise ExchangeError(self.id + ' fetchTickers() response not recognized ' + self.json(tickers))
        return result

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        ticker = self.publicGetPubtickerSymbol(self.extend({
            'symbol': market['id'],
        }, params))
        return self.parse_ticker(ticker, market)

    def parse_ticker(self, ticker, market=None):
        timestamp = float(ticker['timestamp']) * 1000
        symbol = None
        if market:
            symbol = market['symbol']
        elif 'pair' in ticker:
            id = ticker['pair']
            if id in self.markets_by_id:
                market = self.markets_by_id[id]
                symbol = market['symbol']
            else:
                raise ExchangeError(self.id + ' unrecognized ticker symbol ' + id + ' ' + self.json(ticker))
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': float(ticker['high']),
            'low': float(ticker['low']),
            'bid': float(ticker['bid']),
            'ask': float(ticker['ask']),
            'vwap': None,
            'open': None,
            'close': None,
            'first': None,
            'last': float(ticker['last_price']),
            'change': None,
            'percentage': None,
            'average': float(ticker['mid']),
            'baseVolume': float(ticker['volume']),
            'quoteVolume': None,
            'info': ticker,
        }

    def parse_trade(self, trade, market):
        timestamp = int(float(trade['timestamp'])) * 1000
        side = trade['type'].lower()
        orderId = self.safe_string(trade, 'order_id')
        price = float(trade['price'])
        amount = float(trade['amount'])
        cost = price * amount
        fee = None
        if 'fee_amount' in trade:
            feeCost = self.safe_float(trade, 'fee_amount')
            feeCurrency = self.safe_string(trade, 'fee_currency')
            if feeCurrency in self.currencies_by_id:
                feeCurrency = self.currencies_by_id[feeCurrency]['code']
            fee = {
                'cost': feeCost,
                'currency': feeCurrency,
            }
        return {
            'id': str(trade['tid']),
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': market['symbol'],
            'type': None,
            'order': orderId,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    def fetch_trades(self, symbol, since=None, limit=50, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
            'limit_trades': limit,
        }
        if since is not None:
            request['timestamp'] = int(since / 1000)
        response = self.publicGetTradesSymbol(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {'symbol': market['id']}
        if limit is not None:
            request['limit_trades'] = limit
        if since is not None:
            request['timestamp'] = int(since / 1000)
        response = self.privatePostMytrades(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        orderType = type
        if (type == 'limit') or (type == 'market'):
            orderType = 'exchange ' + type
        # amount = self.amount_to_precision(symbol, amount)
        order = {
            'symbol': self.market_id(symbol),
            'amount': str(amount),
            'side': side,
            'type': orderType,
            'ocoorder': False,
            'buy_price_oco': 0,
            'sell_price_oco': 0,
        }
        if type == 'market':
            order['price'] = str(self.nonce())
        else:
            # price = self.price_to_precision(symbol, price)
            order['price'] = str(price)
        result = self.privatePostOrderNew(self.extend(order, params))
        return self.parse_order(result)

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        return self.privatePostOrderCancel({'order_id': int(id)})

    def parse_order(self, order, market=None):
        side = order['side']
        open = order['is_live']
        canceled = order['is_cancelled']
        status = None
        if open:
            status = 'open'
        elif canceled:
            status = 'canceled'
        else:
            status = 'closed'
        symbol = None
        if not market:
            exchange = order['symbol'].upper()
            if exchange in self.markets_by_id:
                market = self.markets_by_id[exchange]
        if market:
            symbol = market['symbol']
        orderType = order['type']
        exchange = orderType.find('exchange ') >= 0
        if exchange:
            parts = order['type'].split(' ')
            orderType = parts[1]
        timestamp = int(float(order['timestamp']) * 1000)
        result = {
            'info': order,
            'id': str(order['id']),
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': orderType,
            'side': side,
            'price': self.safe_float(order, 'price'),
            'average': float(order['avg_execution_price']),
            'amount': float(order['original_amount']),
            'remaining': float(order['remaining_amount']),
            'filled': float(order['executed_amount']),
            'status': status,
            'fee': None,
        }
        return result

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        response = self.privatePostOrders(params)
        orders = self.parse_orders(response, None, since, limit)
        if symbol:
            orders = self.filter_by(orders, 'symbol', symbol)
        return orders

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {}
        if limit is not None:
            request['limit'] = limit
        response = self.privatePostOrdersHist(self.extend(request, params))
        orders = self.parse_orders(response, None, since, limit)
        if symbol is not None:
            orders = self.filter_by(orders, 'symbol', symbol)
        orders = self.filter_by(orders, 'status', 'closed')
        return orders

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        response = self.privatePostOrderStatus(self.extend({
            'order_id': int(id),
        }, params))
        return self.parse_order(response)

    def parse_ohlcv(self, ohlcv, market=None, timeframe='1m', since=None, limit=None):
        return [
            ohlcv[0],
            ohlcv[1],
            ohlcv[3],
            ohlcv[4],
            ohlcv[2],
            ohlcv[5],
        ]

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=100, params={}):
        self.load_markets()
        market = self.market(symbol)
        v2id = 't' + market['id']
        request = {
            'symbol': v2id,
            'timeframe': self.timeframes[timeframe],
            'sort': 1,
            'limit': limit,
        }
        if since is not None:
            request['start'] = since
        request = self.extend(request, params)
        response = self.v2GetCandlesTradeTimeframeSymbolHist(request)
        return self.parse_ohlcvs(response, market, timeframe, since, limit)

    def get_currency_name(self, currency):
        names = {
            'BTC': 'bitcoin',
            'LTC': 'litecoin',
            'ETH': 'ethereum',
            'ETC': 'ethereumc',
            'OMNI': 'mastercoin',
            'ZEC': 'zcash',
            'XMR': 'monero',
            'USD': 'wire',
            'DASH': 'dash',
            'XRP': 'ripple',
            'EOS': 'eos',
            'BCH': 'bcash',  # undocumented
            'USDT': 'tetheruso',  # undocumented
            'NEO': 'neo',  # #1811
            'AVT': 'aventus',  # #1811
            'QTUM': 'qtum',  # #1811
            'EDO': 'eidoo',  # #1811
        }
        if currency in names:
            return names[currency]
        raise NotSupported(self.id + ' ' + currency + ' not supported for withdrawal')

    def create_deposit_address(self, currency, params={}):
        response = self.fetch_deposit_address(currency, self.extend({
            'renew': 1,
        }, params))
        return {
            'currency': currency,
            'address': response['address'],
            'status': 'ok',
            'info': response['info'],
        }

    def fetch_deposit_address(self, currency, params={}):
        name = self.get_currency_name(currency)
        request = {
            'method': name,
            'wallet_name': 'exchange',
            'renew': 0,  # a value of 1 will generate a new address
        }
        response = self.privatePostDepositNew(self.extend(request, params))
        address = response['address']
        tag = None
        if 'address_pool' in response:
            tag = address
            address = response['address_pool']
        return {
            'currency': currency,
            'address': address,
            'tag': tag,
            'status': 'ok',
            'info': response,
        }

    def withdraw(self, currency, amount, address, tag=None, params={}):
        name = self.get_currency_name(currency)
        request = {
            'withdraw_type': name,
            'walletselected': 'exchange',
            'amount': str(amount),
            'address': address,
        }
        if tag:
            request['payment_id'] = tag
        responses = self.privatePostWithdraw(self.extend(request, params))
        response = responses[0]
        return {
            'info': response,
            'id': response['withdrawal_id'],
        }

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        request = '/' + self.implode_params(path, params)
        if api == 'v2':
            request = '/' + api + request
        else:
            request = '/' + self.version + request
        query = self.omit(params, self.extract_params(path))
        url = self.urls['api'] + request
        if (api == 'public') or (path.find('/hist') >= 0):
            if query:
                suffix = '?' + self.urlencode(query)
                url += suffix
                request += suffix
        if api == 'private':
            self.check_required_credentials()
            nonce = self.nonce()
            query = self.extend({
                'nonce': str(nonce),
                'request': request,
            }, query)
            query = self.json(query)
            query = self.encode(query)
            payload = base64.b64encode(query)
            secret = self.encode(self.secret)
            signature = self.hmac(payload, secret, hashlib.sha384)
            headers = {
                'X-BFX-APIKEY': self.apiKey,
                'X-BFX-PAYLOAD': self.decode(payload),
                'X-BFX-SIGNATURE': signature,
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def find_broadly_matched_key(self, map, broadString):
        partialKeys = list(map.keys())
        for i in range(0, len(partialKeys)):
            partialKey = partialKeys[i]
            if broadString.find(partialKey) >= 0:
                return partialKey
        return None

    def handle_errors(self, code, reason, url, method, headers, body):
        if len(body) < 2:
            return
        if code >= 400:
            if body[0] == '{':
                response = json.loads(body)
                feedback = self.id + ' ' + self.json(response)
                message = None
                if 'message' in response:
                    message = response['message']
                elif 'error' in response:
                    message = response['error']
                else:
                    raise ExchangeError(feedback)  # malformed(to our knowledge) response
                exact = self.exceptions['exact']
                if message in exact:
                    raise exact[message](feedback)
                broad = self.exceptions['broad']
                broadKey = self.find_broadly_matched_key(broad, message)
                if broadKey is not None:
                    raise broad[broadKey](feedback)
                raise ExchangeError(feedback)  # unknown message
