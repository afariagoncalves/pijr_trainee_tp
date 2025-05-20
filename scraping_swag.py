from seleniumbase import SB
import time


with SB(browser="chrome") as sb:

    def raspa_produto(seletor_nome, seletor_descricao, seletor_preco):

        produto = []

        nome_elemento = sb.find_element(seletor_nome)
        nome = nome_elemento.text
        produto.append(nome)

        descricao_elemento = sb.find_element(seletor_descricao)
        descricao = descricao_elemento.text
        produto.append(descricao)

        preco_elemento = sb.find_element(seletor_preco)
        preco = preco_elemento.text
        produto.append(preco)

        return produto
        
    def login():
        sb.open("https://www.saucedemo.com")    
        sb.type("#user-name", "standard_user")  
        sb.type("#password", "secret_sauce\n")

    def coleta_dados():
        sb.wait_for_element('.app_logo')
        time.sleep(1)
        
        dados["mochila"] = raspa_produto("#item_4_title_link > div:nth-child(1)",
                                         "div.inventory_item:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)",
                                         "div.inventory_item:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
        
        dados["lanterna"] = raspa_produto("#item_0_title_link > div:nth-child(1)",
                                          "div.inventory_item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)",
                                          "div.inventory_item:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
        
        dados["camisa preta"] = raspa_produto("#item_1_title_link > div:nth-child(1)",
                                              "div.inventory_item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)",
                                              "div.inventory_item:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
        
        dados["casaco"] = raspa_produto("#item_5_title_link > div:nth-child(1)",
                                        "div.inventory_item:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)",
                                        "div.inventory_item:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
        
        dados["macacão"] = raspa_produto("#item_2_title_link > div:nth-child(1)",
                                         "div.inventory_item:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)",
                                         "div.inventory_item:nth-child(5) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
        
        dados["camisa laranja"] = raspa_produto("#item_3_title_link > div:nth-child(1)",
                                                "div.inventory_item:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)",
                                                "div.inventory_item:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")

    dados = {"mochila": [], 
          "lanterna": [], 
          "camisa preta": [], 
          "casaco": [], 
          "macacão": [],
          "camisa laranja": []}
    
    login()
    coleta_dados()