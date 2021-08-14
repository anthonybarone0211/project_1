import questionary
ARK_ETF = ["TSLA", "ROKU", "TDOC", "MSTR", "SQ", "SHOP", "TTWO", "TWLO", "SPOT", "NTLA", "CRSP", "EXAS", "Z", "TWTR", "TER","DOCU","CGEN"]
alt_stock_1_q = questionary.select(
    "Which is the first stock from the ARK ETF you want to replace?",
    ARK_ETF
).ask()
#print(alt_stock_1_q)

alt_stock_1_q_list = [alt_stock_1_q]
print(alt_stock_1_q_list)

#delete alt_stock_1 value from ARK_ETF list, save as new list, use .loc?
#trying to build ARK_ETF_MINUS_1_STOCK list with the stock that the user selects deleted from ARK_ETF, running into either list of choices error or object not iterable error
ARK_ETF_MINUS_1_STOCK = ARK_ETF.remove(f"{[alt_stock_1_q_list]}")

# ARK_ETF_MINUS_1_STOCK = []
# for ark_stocks in ARK_ETF:
#     user_stock = (str.replace(alt_stock_1_q,""))
#     ARK_ETF_MINUS_1_STOCK.append()


alt_stock_2_q = questionary.select(
    "Which is the second stock from the ARK ETF you want to replace?",
    ARK_ETF_MINUS_1_STOCK
).ask()

alt_stock_2_q_list = list(alt_stock_2_q)
print(alt_stock_2_q)