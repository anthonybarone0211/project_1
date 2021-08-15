import questionary
ARK_ETF = ["TSLA", "ROKU", "TDOC", "MSTR", "SQ", "SHOP", "TTWO", "TWLO", "SPOT", "NTLA", "CRSP", "EXAS", "Z", "TWTR", "TER","DOCU","CGEN"]
competitors_list = ["NIO", "NFLX", "PFE", "MSFT", "V", "PYPL", "CRM", "ATVI", "VG", "TTD", "IONS", "NVAX", "AMGN", "RDFN", "SNAP"]
alt_stock_1_q = questionary.select(
    "Which is the first stock from the ARK ETF you want to replace?",
    ARK_ETF
).ask()
#print(alt_stock_1_q)

# alt_stock_1_q_list = [alt_stock_1_q]
# print(alt_stock_1_q_list)
print(alt_stock_1_q)
#delete alt_stock_1 value from ARK_ETF list, save as new list, use .loc?
#trying to build ARK_ETF_MINUS_1_STOCK list with the stock that the user selects deleted from ARK_ETF, running into either list of choices error or object not iterable error
ARK_ETF_MINUS_1_STOCK = ARK_ETF
ARK_ETF_MINUS_1_STOCK.remove(alt_stock_1_q)

alt_stock_2_q = questionary.select(
    "Which is the second stock from the ARK ETF you want to replace?",
    ARK_ETF_MINUS_1_STOCK
).ask()

print(alt_stock_2_q)

alt_stock_1_a = questionary.select(
    f"What would you like to replace {alt_stock_1_q} with?",
    competitors_list
).ask()

print(alt_stock_1_a)

competitors_list_minus_1_stock = competitors_list
competitors_list_minus_1_stock.remove(alt_stock_1_a)

alt_stock_2_a = questionary.select(
    f"What would you like to replace {alt_stock_2_q} with?",
    competitors_list_minus_1_stock
).ask()

print(alt_stock_2_a)
