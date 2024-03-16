import MetaTrader5 as mt5
import pandas as pd
import numpy as np 
import talib
import time








def execute_sell_order():
   
    
    support = df['support'].iloc[-1] 
    take_profit = support
    symbol ="Volatility 25 Index"
    volume = 0.5
    entry_price = df['close'].iloc[-1]
    stop_loss = df['close'].iloc[-1] + 1
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_TYPE_SELL,
        "price": entry_price,
        "sl": stop_loss,
        "tp": take_profit,
    }
    result = mt5.order_send(request)
    print(f"Sell order placed at {entry_price}, Take Profit at {take_profit}, Stop Loss at {stop_loss}")
   
                
    return result


def execute_buy_order():
    
    
    resistance = df['resistance'].iloc[-1] 
    take_profit = resistance
    symbol ="Volatility 25 Index"
    volume = 0.5
    entry_price =  df['close'].iloc[-1]
    stop_loss = df['close'].iloc[-1] - 2
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_TYPE_BUY,
        "price": entry_price,
        "sl": stop_loss,
        "tp": take_profit,
    }
    result = mt5.order_send(request)
    print(f"Buy order placed at {entry_price}, Take Profit at {take_profit}, Stop Loss at {stop_loss}")
    

   
       

    return result



count = 0
trade_count = 100

while count < trade_count:

    try:

        

        
        ohlc = mt5.copy_rates_from_pos("Volatility 25 Index", mt5.TIMEFRAME_M1, 0, 20)
        df = pd.DataFrame(ohlc)

        """print(df)"""
      
        def calculate_support(df, window=80):
            price_data = df['close']
            support = df['close'].rolling(window=window, min_periods=1).min()
            S = support.where(support < price_data)

            if S.isna().all():
                # If all values in S are NaN, increase window size
                support = df['close'].rolling(window=window + 70, min_periods=1).min()
                S = support.where(support < price_data)

            return S
  

        def calculate_resistance(df, max_window=200, step=30):
            price_data = df['close']
            resistance = df['close'].rolling(window=max_window, min_periods=1).max()
            R = resistance.where(resistance > price_data)
            

            if R.isna().all():
                return R  # All values in S are NaN, no need to increase window size

            for window_size in range(step, max_window + step, step):
                resistance = df['close'].rolling(window=window_size, min_periods=1).max()
                R = resistance.where(resistance > price_data)

                if not R.isna().all():
                    return R

            return R


        
        df['resistance'] = calculate_resistance(df)
        df['support'] = calculate_support(df)
        support = df['support'].iloc[-1]
        resistance = df['resistance'].iloc[-1]
        
        
        high = df['high'].iloc[-5:-3]
        beforeH = df['high'].iloc[-8:-5]
        afterH = df['high'].iloc[-3:-1]

        low = df['low'].iloc[-5:-3]
        beforeL = df['low'].iloc[-8:-5]
        afterL = df['low'].iloc[-3:-1]



        if max(beforeH) < max(high) > max(afterH):
            execute_sell_order()
            count += 1

        elif min(beforeL) > min(low) < min(afterL) :
            execute_buy_order()
            count += 1

        else:
            print('condition not met')

        

    

       

        
        time.sleep(60) 
    except Exception as e:
        print(f"Error condition: {e}")

       

    