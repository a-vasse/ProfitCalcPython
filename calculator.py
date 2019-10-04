from decimal import *

currency_places = Decimal(10) ** -2

def calculate_net(revenue, expenses):
    try:
        revenue = Decimal(revenue)
    except:
        raise ValueError('revenue must be numeric')
    try:
        expenses = Decimal(expenses)
    except:
        raise ValueError('expenses must be numeric')

    if revenue < 0:
        raise ValueError('revenue cannot be negative')
    if expenses < 0:
        raise ValueError('expenses cannot be negative')

    with localcontext() as ctx:
        ctx.traps[Inexact] = True
        revenue = revenue.quantize(currency_places)
        expenses = expenses.quantize(currency_places)

    return {
       'revenue': revenue,
       'expenses': expenses,
       'net': revenue - expenses
    }
