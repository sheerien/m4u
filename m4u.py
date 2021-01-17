from requests_html import HTML, HTMLSession
import urllib.request
from tqdm import tqdm
from time import sleep
import re
import os


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Bold Text Colors
    bd_dark_Gray = '\033[1;30;40m'
    bd_bright_Red = '\033[1;31;40m'
    bd_bright_Green = '\033[1;32;40m'
    bd_yellow = '\033[1;33;40m'
    bd_bright_Blue = '\033[1;34;40m'
    bd_bright_Magenta = '\033[1;35;40m'
    bd_bright_Cyan = '\033[1;36;40m'
    bd_white = '\033[1;37;40m'

    # Text Color Grey Background
    txt_black = '\033[0;30;47m'
    txt_red = '\033[0;31;47m'
    txt_green = '\033[0;32;47m'
    txt_brown = '\033[0;33;47m'
    txt_blue = '\033[0;34;47m'
    txt_magenta = '\033[0;35;47m'
    txt_cyan = '\033[0;36;47m'
    txt_light_Grey = '\033[0;37;40m'

    # Colored Background
    bg_black = '\033[0;37;48m'
    bg_red = '\033[0;37;41m'
    bg_green = '\033[0;37;42m'
    bg_yellow = '\033[0;37;43m'
    bg_blue = '\033[0;37;44m'
    bg_magenta = '\033[0;37;45m'
    bg_cyan = '\033[0;37;46m'
    bg_white = '\033[0;37;47m'


class vod(Color):
    session = HTMLSession()

    def __init__(self, path):
        # self.show()
        self.path = path

    def base_url(self):
        all_paths = []
        r = self.session.get(self.path)
        art_id = r.html.find('#player-option-1')
        for a_id in art_id:
            all_paths.append(a_id.attrs['data-url'])
        return all_paths

    def img_film(self):
        r = self.session.get(self.path)
        poster = r.html.find('.poster', first=True)
        img = poster.find('img', first=True).attrs['src']
        return img

    def film_name(self):
        r = self.session.get(self.path)
        title = r.html.find('.data', first=True)
        name = title.find('h1', first=True).text
        return name

    def desc_film(self):
        r = self.session.get(self.path)
        desc = r.html.find('.wp-content', first=True)
        desc_end = desc.find('p', first=True).text
        return desc_end

    def inside_link(self, items=[]):
        all_data = []
        for a in items:
            r = self.session.get(a)
            art_data = r.html.find('iframe')
            for a_data in art_data:
                all_data.append(a_data.attrs['src'])
        return all_data

    def mp_links(self, linkes=[]):
        all_mps = []
        for l in linkes:
            r = self.session.get(l)
            art_mp4 = r.html.find('source')
            for a_mp4 in art_mp4:
                all_mps.append(a_mp4.attrs['src'])
        return all_mps

    def all_mp4(self, mpfours=[]):
        for m in mpfours:
            print(m)

    def down_load(self, url_mp4):
        open_url = urllib.request.urlopen(url_mp4)
        print(open_url.info())
        file_name = url_mp4.split("/")[-1]
        print(file_name)
        open_file = open(file_name, 'wb')
        block_size = 1024
        file_size = int(open_url.headers["Content-Length"])
        for i in tqdm(range(file_size)):
            buffer = open_url.read(block_size)
            i = i + block_size
            open_file.write(buffer)

        open_file.close()
        print("Download Complet ..... !!!")


def show():
    print("")
    c = Color()
    os.system("color 0a")
    os.system("mode 80,25")
    os.system('title  Movies 4U [ V 1.0.0 ]')
    os.system("cls")
    print(f"{c.bd_bright_Cyan}")
    sh = '''
                        ***********************
                        *****             *****
                        * Welcome Everybody:] *
                        *****             *****
                        ***********************
            
        #     # ####### #     # ### #######  #####  #       #     # 
        ##   ## #     # #     #  #  #       #     # #    #  #     # 
        # # # # #     # #     #  #  #       #       #    #  #     # 
        #  #  # #     # #     #  #  #####    #####  #    #  #     # 
        #     # #     #  #   #   #  #             # ####### #     # 
        #     # #     #   # #    #  #       #     #      #  #     # 
        #     # #######    #    ### #######  #####       #   #####  
        
           *****************************************************
           ****            Movies4U Tool @v1.0.0            ****
           ****        Developed by : Sherien Bassem        ****
           ****               Ghana-Est Company             ****
           *****************************************************
    '''
    print(sh)
    input("Press Enter To Continue ....... ")


def film(url):
    print("")
    v = vod(url)
    # img = v.img_film()
    # name = v.film_name()
    # desc = v.desc_film()
    vr = v.base_url()
    vra = v.inside_link(vr)
    mp4 = v.mp_links(vra)
    # print("=================================")
    # print("")
    # print(f"image : {img}")
    # print("")
    # print("=================================")
    # print("")
    # print(f"film name : {name}")
    # print("")
    # print("=================================")
    # print("")
    # print(f"description film : {desc}")
    # print("")
    # print("=================================")
    print("")
    v.all_mp4(mp4)
    print("")
    print("========================================================================")
    print("")


def run():
    print("")
    show()
    print("")
    os.system("cls")
    print("")
    website = '''
           *****************************************************
           ****               Go To Web-Site                ****
           ****           [ https://www.movs4u.ws/ ]        ****
           ****  And you choose any Movie to fetch mp4 url  ****
           *****************************************************
    '''
    print(website)
    print("")
    print("======================= Enter Your Movie Url ==========================")
    vod_path = input("Enter your movie url : ")
    is_url = re.search(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", vod_path)
    if is_url:
        film(vod_path)
    else:
        print("")
        print("Please Enter A Valid URL ...")
        sleep(5)
        os.system("cls")


run()
while True:
    try:
        user_choice = input("Do you want to continue [y/n]: ").lower().strip()
        if user_choice == 'y':
            run()
        elif user_choice == "n":
            print('The tool has been finished ...')
            sleep(3)
            exit()
        else:
            err_1 = '''
                    *******************************************
                    ***   Please Choose  [ y ] or [ n ]     ***
                    *******************************************
                    '''
            print(err_1)
            sleep(3)
    except ValueError:
        err_2 = '''
            *****************************************
            ***  Please Enter A Valid Choice !!!  ***
            *****************************************
        '''
        print(err_2)
        sleep(3)
