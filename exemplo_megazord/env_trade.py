
from envs_trade.trading_forex import TradingForex

class EnvTrade: 
    def __init__(self): 
        self.action_space = 5
        self.state_dim    = 11
        self.limit_ope    = 30000000000000000000
        
    
    def get_state(self, candle):
        self.trading.update_market(candle)
        state_nn = self.trading.state_neural_network(self.state_dim)
        return state_nn
    
    def execute(self, action):
        previous_value  = self.rewards
        operation,volum = self.execute_strategy(action)
        rewards_step    = self.rewards - previous_value

        if self.mode == "scaler":
            return self.done
  
        if self.mode == "train" or self.mode == "test" : 
            return self.done, rewards_step, self.rewards,self.cur_step, self.balance,\
                self.equity, self.buy_right,self.sell_right,self.buy_wrong,self.sell_wrong,self.min_equity
        
        if self.mode == "relatory":
            return  self.done, self.rewards, self.cur_step, self.hold, self.buy_open, self.buy_close, self.buy_right, self.buy_wrong,\
                self.sell_open, self.sell_close, self.sell_right, self.sell_wrong, self.balance, self.equity,\
                     self.min_equity, self.max_equity, self.max_pl_sell, self.min_pl_sell, self.max_pl_buy, self.min_pl_buy
                    
        if self.mode == "real_time":
            return operation,volum,self.done

        if self.mode == "backtest":
            return operation, volum, self.balance, self.balance_acumulated, self.equity_acumulated, self.equity, self.done

    def get_status_market(self):
        self.cur_step,self.rewards,self.equity,self.balance,self.hold,\
            self.sell_open,self.sell_close,self.sell_right,self.sell_wrong,self.sell_opened,\
                self.buy_open,self.buy_close,self.buy_right,self.buy_wrong,self.buy_opened,\
                    self.min_equity, self.max_equity, self.max_pl_sell, self.min_pl_sell,\
                        self.max_pl_buy, self.min_pl_buy, self.balance_acumulated, self.equity_acumulated = self.trading.status_market() 
                             
    def execute_strategy(self, action):  
        self.done = self.trading.verify_done()
        if self.done == True:
            if self.buy_opened > 0 and self.sell_opened > 0 :
                type_ope, volum = self.trading.close_all()
                return "close_all", volum
            
            if self.sell_opened > 0 :
                type_ope, volum = self.trading.sell_close_all()
                return type_ope, volum
                
            if self.buy_opened > 0:
                type_ope, volum = self.trading.buy_close_all()
                return type_ope, volum  
        
            #if self.buy_opened < 10 : 
            type_ope, volum = self.trading.buy()
            return type_ope, volum

            #if self.sell_opened < 10 :
            type_ope, volum = self.trading.sell()
            return type_ope, volum

            if self.buy_opened == 0 :
                self.trading.penalty_buy()
                return "hold", 0
            if self.buy_opened > 0 :
                type_ope, volum = self.trading.buy_close_all()
                return type_ope, volum

            if self.sell_opened == 0 :
                self.trading.penalty_sell()
                return "hold", 0
            if self.sell_opened > 0 :
                type_ope, volum = self.trading.sell_close_all()
                return type_ope, volum

            if self.sell_opened > 0 and self.buy_opened > 0:
                type_ope, volum = self.trading.close_all()
                return "close_all", volum        
            self.trading.penalty_sell()
            self.trading.penalty_buy()
            return "hold", 0

    def execute_print(self,worker_name):
        self.space = "--------------------------------------------------"
        print(f"------------- Env-TRADE WEEK : {self.week_now} Worker Name : {worker_name} ")
        print(f"REWARDS -----: {self.rewards}") 
        print(f"STEPS -------: {self.cur_step}")
        print(f"HOLD --------: {self.hold}")   
        print(self.space)
        print(f"BUY OPEN -------: {self.buy_open} | SELL OPEN -------: {self.sell_open} ")
        print(f"BUY CLOSE ALL --: {self.buy_close} | SELL CLOSE ALL --: {self.sell_close}")
        print(f"BUY CLOSE RIGHT : {self.buy_right} | SELL CLOSE RIGHT : {self.sell_right}")
        print(f"BUY CLOSE WRONG : {self.buy_wrong} | SELL CLOSE WRONG : {self.sell_wrong}")
        print(self.space)
        print(f"BALANCE ---- : {self.balance} ")
        print(f"EQUITY  ---- : {self.equity} ")
        print(f"MIN EQUITY-- : {self.min_equity} ")
        print(self.space)
        print(" ")
        
        return self.hold, self.buy_open, self.buy_close, self.buy_right, self.buy_wrong,\
            self.sell_open, self.sell_close, self.sell_right, self.sell_wrong, self.min_equity

    def reset_env(self,initial_investment,balance_acumulated,equity_acumulated,profit_target,total_steps,week_now,mod, trading: TradingForex):
        # self.trading     = TradingForex(initial_investment,profit_target)
        self.trading     = trading
        self.mode        = mode
        self.total_steps = total_steps
        self.week_now    = week_now
        self.trading.reset_trading(total_steps,balance_acumulated,equity_acumulated,mode)
        self.profit_target = profit_target + initial_investment
        return


if __name__ == "__main__":

    trade_enviroment = EnvTrade()

    initial_investment = 1
    balance_acumulated = 1
    equity_acumulated = 1
    profit_target = 1
    total_steps = 1
    week_now = 1
    mod = "train"

    trading = TradingForex(initial_investment,profit_target)
    trade_enviroment.reset_env(initial_investment, balance_acumulated, equity_acumulated, profit_target, total_steps, week_now, mod, trading)

    trading2 = TradingForex2(initial_investment,profit_target, 1, 1, 3)
    trade_enviroment.reset_env(initial_investment, balance_acumulated, equity_acumulated, profit_target, total_steps, week_now, mod, trading2)