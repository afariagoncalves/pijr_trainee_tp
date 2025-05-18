from seleniumbase import SB

with SB(browser="chrome") as sb:

    def login():
        sb.open("https://www.saucedemo.com")    
        sb.type("#user-name", "standard_user")  
        sb.type("#password", "secret_sauce\n")

    login()