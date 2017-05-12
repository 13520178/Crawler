import Crawler_Roof
import time

from bs4 import BeautifulSoup

class ND_Carawler(Crawler_Roof.Renew_Crawler):
    def __init__(self, h_p):
        self.html_page = h_p



    def Re_Find_All(self, g_data_tag, class_name = None):
        if class_name == None:
            soup = BeautifulSoup(open(self.html_page), "html.parser")
            g_data = soup.find_all(g_data_tag, href=True)
        else:
            soup = BeautifulSoup(open(self.html_page), "html.parser")
            g_data = soup.find_all(g_data_tag, {"class": class_name})

        return g_data

    #OK
    def Re_Contents(self, g_da, num_contents, f_a_n = None,class_name = None,num_find_all =None):
        if f_a_n == None and class_name == None and num_find_all== None:
            for item in g_da:
                result = item.contents[num_contents].text
        else:
            for item in g_da:

                result = item.contents[num_contents].find_all(f_a_n,{"class":class_name})[num_find_all].text
                #time.sleep(0.1)
                print(result)


    def Re_Item(self,g_da, loc_f_a, f_a_num):
       for item in g_da:
           result = item.find_all(loc_f_a)[f_a_num].text
       return result


    