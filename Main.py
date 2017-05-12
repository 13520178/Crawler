import ND_Crawler
import threading

nguyenkim = ND_Crawler.ND_Carawler("nguyenkim.html")
g_data = nguyenkim.Re_Find_All("a","nk-fgp-in-items" )


t1 = threading.Thread(target=nguyenkim.Re_Contents(g_data, 9, "span","nk-price-txt",0 ))
t2 = threading.Thread(target=nguyenkim.Re_Contents(g_data, 9, "span","nk-price-txt",0 ))

t1.start()
t2.start()

t1.join()
t2.join()