
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from time import sleep
from random import choice as ch

#Enter username of instagram
username = " "

#Enter password
password = " "

# This bot post a comment on a post that is post with a hashtag
# enter hashtag  for Ex. "dog", "cat"
tag= " "


# Enter a comment 
# Ex. "nice" , "nice pic" etc.
com= " "

# This function post a comment
def comment(username,password):
    firefoxprofile=FirefoxProfile()
    firefoxprofile.set_preference('permissions.default.image',2)
    firefoxprofile.set_preference('media.autoplay.default', 2)
    firefoxprofile.set_preference('media.autoplay.allow-muted', False)

    options = Options()
    
    # This option make bot handless or you can't see graphic interface
    # use false to see graphic interface
    options.headless = True
    
    # Before using this bot Please download geckodriver (Webdriver of firefox)
    # Enter the path of geckodriver
    exe_path = "E:\\selenium\\geckodriver.exe"
    
    driver=webdriver.Firefox(firefox_profile=firefoxprofile,options=options, executable_path= exe_path)
    
    # total comment
    tocom=0
    yot=0

    driver.get("https://www.instagram.com/accounts/login/")
    sleep(2)

    print("===>login into...----> "+username)

    usr=driver.find_element(by=By.XPATH, value="//input[@name='username']")
    usr.send_keys(username)
    pase=driver.find_element(by=By.CSS_SELECTOR, value="div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
    pase.send_keys(password)

    try:
        logn=driver.find_element(by=By.XPATH, value="//form[@id='loginForm']/div/div[3]/button/div")
        logn.click()
    except:
        print("================> Fail to login...") 
        driver.close()   
        return 

    sleep(5)
   
    for i in range(1,5):

        print("finding tag....")
        driver.get("https://www.instagram.com/explore/tags/"+tag+"/")

        sleep(5)
        print("Finding First Post...",i)
        print("\n")

        try:
            driver.find_element(by=By.CSS_SELECTOR, value=".\_ac7v:nth-child(3) > .\_aabd:nth-child(3) .\_aagw").click()
            sleep(3)
            driver.find_element(by=By.CSS_SELECTOR, value=".\_aaqg .\_ab6-").click()

        except:
            print("=============> Fail to find first post....")   
            yot=yot+1
            driver.refresh()
            if(yot==2):
                print("Total comment done by "+username+" is ",tocom)  
                driver.close()
                return

            continue
        
        sleep(2)

        for j in range(1,11):

            try:
                sleep(1)
                print("Pasting Comment...",j) 
                commen=driver.find_element(by=By.CSS_SELECTOR, value=".x1i0vuye")
                commen.send_keys(ch(com))
                sleep(3)

                print("Sending Comment... using ==> ",username)
                driver.find_element(by=By.CSS_SELECTOR, value="div.xdl72j9").click()  
                sleep(3)
                tocom=tocom+1

            except:
                print("=============> Fail to comment....")
                print("\n")
                pass

            sleep(2)

            try:
                print("Gatting Next Post...")
                print("\n")
                driver.find_element(by=By.CSS_SELECTOR, value=".\_aaqg .\_ab6-").click()
                sleep(3)

            except:
                print("========> Fail to get next post...")
                print("\n")
                try:
                    print("Again trying...")
                    driver.find_element(by=By.CSS_SELECTOR, value=".\_aaqg .\_ab6-").click()

                except:
                    print("========> Again fail...")
                    driver.close() 
                    print("Total comment done by "+username+" is ",tocom)  
                    print("\n")      
                    return

    print("Total comment done by "+username+" is ",tocom)  
    print("\n")      

    print("=====>Logouting from "+username)
    driver.close()


#call function 
comment(username, password)
