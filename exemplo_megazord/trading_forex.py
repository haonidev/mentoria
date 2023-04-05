from envs_trade.indicators.log_buy_sell import LogReturnBuySell 

import numpy as np 
from decimal import Decimal 
class TradingForex: 
    def __init__(self,initial_investment,profit_target): 

        # OPERATION
        self.initial_invest = Decimal(initial_investment) 
        
        # INDICATORS
        self.log_return_buy  = LogReturnBuySell(2) 
        self.log_return_sell = LogReturnBuySell(2) 

        self.log_return_buy_cl  = LogReturnBuySell(2) 
        self.log_return_sell_cl = LogReturnBuySell(2) 

        self.log_return_buy  = LogReturnBuySell(2) 
        self.log_return_sell = LogReturnBuySell(2) 
        
        self.profit_target = profit_target + initial_investment
                
    # 0-0
    def reset_trading(self,total_steps,balance_acumulated,equity_acumulated,mode):
        self.log_return_buy .reset_log()
        self.log_return_sell.reset_log()
        self.log_return_buy_cl.reset_log()
        self.log_return_sell_cl.reset_log()
        self.log_return_buy .reset_log() 
        self.log_return_sell.reset_log() 
        self.mode        = mode
        self.total_steps = total_steps 
        self.cur_step    = -1
        self.done        = False 
        
        self.rewards = Decimal(0)
                
        self.hold = 0
        
        self.max_equity = 0
        self.min_equity = 9999999999
                
        self.reset_buy()
        self.reset_sell()  

        self.balance = self.initial_invest 
        self.equity  = self.initial_invest
        
        self.balance_acumulated = balance_acumulated
        self.equity_acumulated  = equity_acumulated
        
    def reset_buy(self):    
        self.buy_prices = []
        self.buy_pl = 0
        
        self.buy_open   = 0 
        self.buy_close  = 0
        self.buy_right  = 0
        self.buy_wrong  = 0
        
        self.log_ask    = 0
        self.max_pl_buy = 0
        self.min_pl_buy = 9999999999
        self.rw_buy     = 0
    def reset_sell(self):    
        self.sell_prices = []
        self.sell_pl = 0
        
        self.sell_open   = 0
        self.sell_close  = 0
        self.sell_right  = 0
        self.sell_wrong  = 0
        
        self.log_bid     = 0
        self.max_pl_sell = 0
        self.min_pl_sell = 9999999999
        self.rw_sell     = 0

    # 1-0 update market after action
    def update_market(self,candle):
        # CANDLE
        self.datetime         = candle[0] 
        self.bid_current      = round(Decimal(candle[1] * 1000),2)
        self.ask_current      = round(Decimal(candle[2] * 1000),2)

        # REAL VALUES
        self.ask_close_sell_price = self.ask_current  
        self.bid_open_sell_price  = self.bid_current  
        self.bid_close_buy_price  = self.bid_current 
        self.ask_open_buy_price	  = self.ask_current 
                
        self.log_ask = self.log_return_buy.log_ask(self.ask_current )
        self.log_bid = self.log_return_sell.log_bid(self.bid_current)

        self.log_buy  = self.log_return_buy.log_buy(self.ask_current,self.bid_current)
        self.log_sell = self.log_return_sell.log_sell(self.ask_current,self.bid_current)
        
        self.update_operation_buy()
        self.update_operation_sell()
        self.update_equity()
        self.update_min_max()
        self.control_steps()
        
        return
   
    # 1 - 1
    def update_operation_buy(self):
        self.current_buy_right = 0
        self.current_buy_wrong = 0
        self.buy_pl            = 0
        # BUY
        if len(self.buy_prices) > 0:
            for i in range(len(self.buy_prices)):
                real_profit_loss = self.bid_close_buy_price - self.buy_prices[i] 
                self.buy_pl     += real_profit_loss  
                if real_profit_loss > 0:
                    self.current_buy_right += 1
                if real_profit_loss < 0:
                    self.current_buy_wrong += 1      
    def update_operation_sell(self):
        self.current_sell_right = 0
        self.current_sell_wrong = 0
        self.sell_pl            = 0
        # SELL
        if len(self.sell_prices) > 0:
            for i in range(len(self.sell_prices)):
                real_profit_loss = self.sell_prices[i] - self.ask_close_sell_price 
                self.sell_pl    += real_profit_loss  
                if real_profit_loss > 0:
                    self.current_sell_right += 1
                if real_profit_loss < 0:
                    self.current_sell_wrong += 1

    # 1 - 2
    def update_equity(self):    
        self.equity  = self.balance
        self.equity += self.buy_pl
        self.equity += self.sell_pl
        
        self.equity_acumulated  = self.balance_acumulated
        self.equity_acumulated += self.buy_pl
        self.equity_acumulated += self.sell_pl
        return 

    # 1 - 4 STEPS
    def control_steps(self):     
        self.cur_step+=1
        #self.done     = self.cur_step == self.total_steps-1

    def verify_done(self):
        coust_operation_buy  = abs(self.bid_close_buy_price  - self.ask_open_buy_price)
        coust_operation_sell = abs(self.ask_close_sell_price - self.bid_open_sell_price)
        # CLOSE OPERATIONS
        if self.equity < coust_operation_buy or self.equity < coust_operation_sell or self.equity >= self.profit_target or self.cur_step == (self.total_steps-1):
            if len(self.buy_prices) > 0 and len(self.sell_prices) > 0:
                _ = self.close_all()
            if len(self.buy_prices) > 0 :
                _ = self.buy_close_all()
            if len(self.sell_prices) > 0 :
                _ = self.sell_close_all()    
            self.done = True    
        return self.done
        
    # 1 - 5 send state
    def state_neural_network(self,state_size):
        # STATES
        self.state = np.zeros(state_size) 

        # SCORE
        self.state[0] = self.rewards 
        # INDICATOR
        self.state[1] = self.log_ask 
        self.state[2] = self.log_bid

        # OPERATION 
        self.state[3] = len(self.sell_prices)
        self.state[4] = len(self.buy_prices)
        
        self.state[5] = self.sell_pl
        self.state[6] = self.buy_pl

        self.state[7] = self.equity
        
        self.state[8] = self.log_buy
        self.state[9] = self.log_sell
        
        # self.state[10] = self.rw_buy
        # self.state[11] = self.rw_sell
        
        self.state[10] = self.balance

        return self.state

    # 2 
    def status_market(self):  
        buy_opened  = len(self.buy_prices)
        sell_opened = len(self.sell_prices)

        self.update_equity()
        
        return self.cur_step,self.rewards,self.equity,self.balance,self.hold,\
            self.sell_open,self.sell_close,self.sell_right,self.sell_wrong,sell_opened,\
                self.buy_open,self.buy_close,self.buy_right,self.buy_wrong,buy_opened,\
                    self.min_equity, self.max_equity, self.max_pl_sell, self.min_pl_sell,\
                        self.max_pl_buy, self.min_pl_buy, self.balance_acumulated, self.equity_acumulated       



    # OPEN OPERATION
    def buy(self):   
        self.buy_open += 1
        real_coust_operation  = abs(self.bid_close_buy_price  - self.ask_open_buy_price)
        self.buy_prices.append(self.ask_open_buy_price) 
        self.update_balance(real_coust_operation,"open")
        self.rewards -= abs(self.log_buy)
        if self.sell_open == 0:
            self.rewards -= abs(self.log_buy)
        return "buy", 1 
    def sell(self):
        self.sell_open += 1
        real_coust_operation = abs(self.bid_open_sell_price - self.ask_close_sell_price)
        self.sell_prices.append(self.bid_open_sell_price) 
        self.update_balance(real_coust_operation,"open")
        self.rewards -= abs(self.log_sell)
        if self.buy_open == 0:
            self.rewards -= abs(self.log_sell)
        return "sell",1


    def sell_close_all(self): 
        self.update_operation_sell()
        volum_close      = len(self.sell_prices)
        self.sell_close += volum_close
        self.sell_right += self.current_sell_right
        self.sell_wrong += self.current_sell_wrong 
        self.update_balance(self.sell_pl,"close")
        if self.sell_pl > 0 : 
            self.rewards += abs(self.log_sell) #abs(self.log_sell)
        if self.sell_pl < 0 : 
            self.rewards -= abs(self.log_sell)
        # REMOVE
        self.sell_pl = 0
        self.sell_prices  = []
        self.rw_sell = 0
        return "close_sell",volum_close 
    def buy_close_all(self): 
        self.update_operation_buy()  
        volum_close     = len(self.buy_prices)
        self.buy_close += volum_close
        self.buy_right += self.current_buy_right
        self.buy_wrong += self.current_buy_wrong 
        self.update_balance(self.buy_pl,"close")
        if self.buy_pl > 0 : 
            self.rewards += abs(self.log_buy)#abs(self.log_buy)
        if self.buy_pl < 0 : 
            self.rewards -= abs(self.log_buy)
        # REMOVE
        self.buy_pl = 0
        self.buy_prices  = []
        return "close_buy",volum_close 
    def close_all(self): 
        self.update_operation_buy()    
        self.update_operation_sell() 
        volum_close = len(self.sell_prices) + len(self.buy_prices)
        self.sell_close += len(self.sell_prices)
        self.buy_close  += len(self.buy_prices)
        self.sell_right += self.current_sell_right
        self.buy_right  += self.current_buy_right
        self.sell_wrong += self.current_sell_wrong 
        self.buy_wrong  += self.current_buy_wrong 
        self.update_balance(self.buy_pl,"close")
        if self.buy_pl > 0 : 
            self.rewards += abs(self.log_buy)
        if self.buy_pl < 0 : 
            self.rewards -= abs(self.log_buy)
        self.update_balance(self.sell_pl,"close")
        if self.sell_pl > 0 : 
            self.rewards += abs(self.log_sell)
        if self.sell_pl < 0 : 
            self.rewards -= abs(self.log_sell)
        

        
        self.buy_pl  = 0
        self.sell_pl = 0
        self.buy_prices  = []
        self.sell_prices = []
        self.rw_buy  = 0
        self.rw_sell = 0
        return "close_all",volum_close 



  
    def update_balance(self,real_coust_operation,action):
        if action == "open":
            self.balance -= real_coust_operation
            #self.rewards -= real_coust_operation
            
            self.balance_acumulated -= real_coust_operation
            
        if action == "close":
            self.balance += real_coust_operation
            #self.rewards += real_coust_operation
            
            self.balance_acumulated += real_coust_operation
            
        self.equity = self.balance
        self.equity_acumulated = self.balance_acumulated
        return

    def penalty_buy(self): # cai aqui se não tiver nenhuma posiça de buy aberta 
        self.hold += 1        
        self.rewards -= abs(self.log_buy) * self.hold
        return "type_ope", 0

    def penalty_sell(self): # cai aqui se não tiver nenhuma posiça de Sell aberta 
        self.hold += 1
        self.rewards -= abs(self.log_sell) * self.hold
        return "type_ope", 0

    def update_min_max(self):
        # PL BUY
        if self.buy_pl > self.max_pl_buy:
            self.max_pl_buy = self.buy_pl  
        if self.buy_pl < self.min_pl_buy:
            self.min_pl_buy = self.buy_pl
        # PL SELL
        if self.sell_pl > self.max_pl_sell:
            self.max_pl_sell = self.sell_pl   
        if self.sell_pl < self.min_pl_sell:
            self.min_pl_sell = self.sell_pl
        # EQUITY MAX
        if self.equity > self.max_equity : 
            self.max_equity = self.equity
        if self.equity < self.min_equity :
            self.min_equity = self.equity
        return
    