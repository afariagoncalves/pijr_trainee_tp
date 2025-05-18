from seleniumbase import SB

dados = {"mochila": [], 
          "lanterna": [], 
          "camisa preta": [], 
          "casaco": [], 
          "macacão": [],
          "camisa laranja": []}

with SB(browser="chrome") as sb:

    def login():
        sb.open("https://www.saucedemo.com")    
        sb.type("#user-name", "standard_user")  
        sb.type("#password", "secret_sauce\n")

    def coleta_dados():
        sb.assert_element('div:contains("Sauce Labs Backpack")')
        
        #mochila
        dados["mochila"].append(sb.get_text("#item_4_title_link > div:nth-child(1)"))
        dados["mochila"].append(sb.get_text("div.inventory_item:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
        dados["mochila"].append(sb.get_text("div.inventory_item:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)"))

        #lanterna
        dados["lanterna"].append(sb.get_text("#item_0_title_link > div:nth-child(1)"))
        dados["lanterna"].append(sb.get_text("div.inventory_item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
        dados["lanterna"].append(sb.get_text("div.inventory_item:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)"))
        
        #camisa preta
        dados["camisa preta"].append(sb.get_text("#item_1_title_link > div:nth-child(1)"))
        dados["camisa preta"].append(sb.get_text("div.inventory_item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
        dados["camisa preta"].append(sb.get_text("div.inventory_item:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)"))
    
        #casaco
        dados["casaco"].append(sb.get_text("#item_5_title_link > div:nth-child(1)"))
        dados["casaco"].append(sb.get_text("div.inventory_item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))   
        dados["casaco"].append(sb.get_text("div.inventory_item:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)"))
   
        #macacão
        dados["macacão"].append(sb.get_text("#item_2_title_link > div:nth-child(1)"))
        dados["macacão"].append(sb.get_text("div.inventory_item:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
        dados["macacão"].append(sb.get_text("div.inventory_item:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)"))
        
        #camisa laranja
        dados["camisa laranja"].append(sb.get_text("#item_3_title_link > div:nth-child(1)"))
        dados["camisa laranja"].append(sb.get_text("div.inventory_item:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)"))
        dados["camisa laranja"].append(sb.get_text("div.inventory_item:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)"))

    login()
    coleta_dados()