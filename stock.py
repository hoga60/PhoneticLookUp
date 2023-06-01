import twstock
import matplotlib.pyplot as plt
import time
from datetime import datetime

def read( code ):
    time.sleep(5)

    stock = twstock.Stock( code )

    x = stock.date
    y = stock.price
    z = stock.capacity

    # 將日期轉成字串
    x = [datetime.strftime(e, '%Y-%m-%d') for e in x]
    xlabel = x[::10]

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    ax1.plot( x, y, color="orange" )
    ax2.bar( x, z )

    plt.xticks( xlabel )
    plt.savefig( code + '.png')
    return code+'.png'
