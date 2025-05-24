from seleniumbase import SB
import time
import csv


with SB(browser="chrome") as sb:

    dados = {"mochila": [], 
        "lanterna": [], 
        "camisa preta": [], 
        "casaco": [], 
        "macacão": [],
        "camisa laranja": []}

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
        

    def salvar_csv(dados):

        with open('produtos.csv', 'w+') as arquivo:
            writer = csv.writer(arquivo)
            # Escrever cabeçalho
            writer.writerow(['Nome', 'Descrição', 'Preço'])
            # Escrever dados
            for i in dados:
                writer.writerow([dados[i][0], dados[i][1], dados[i][2]])

        print("Dados salvos em produtos.csv")


    def adiciona_carrinho():

        seletor_botao = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-bolt-t-shirt", 
                         "sauce-labs-fleece-jacket", "sauce-labs-onesie", "test\\.allthethings\\(\\)-t-shirt-\\(red\\)"]
        for i in seletor_botao:
            sb.click(f"#add-to-cart-{i}")
            sb.wait_for_element(f"#remove-{i}")
 

    def checkout():

        sb.type("#first-name", "Trainee")
        sb.type("#last-name", "PiJunior")
        sb.type("#postal-code", "31270-901")


    def raspar_compra():

        pagamento_elemento = sb.find_element("div.summary_value_label:nth-child(2)")
        informacoes_compra["meio de pagamento"] = pagamento_elemento.text

        entrega_elemento = sb.find_element("div.summary_value_label:nth-child(4)")
        informacoes_compra["forma de entrega"] = entrega_elemento.text

        total_elemento = sb.find_element(".summary_total_label")
        informacoes_compra["total"] = total_elemento.text

    
    login()
    sb.wait_for_element('.app_logo')
    time.sleep(1)

    coleta_dados()

    salvar_csv(dados);

    adiciona_carrinho()

    sb.click(".shopping_cart_link")
    sb.wait_for_element(".cart_quantity_label")
    for i in range(6):
        sb.find_element(f"#item_{i}_title_link > div:nth-child(1)")    
        

    sb.click("#checkout")
    sb.wait_for_element(".checkout_info")

    checkout()

    sb.click("#continue")
    sb.wait_for_element(".cart_quantity_label")

    informacoes_compra = {"meio de pagamento" : "",
                          "forma de entrega": "",
                          "total": ""}
    
    raspar_compra()

    sb.click("#finish")
    elemento = sb.find_element(".complete-header")
    if (elemento.text != "Thank you for your order!"):
        print("Erro ao realizar compra")
    else:   
        print("Compra realizada com sucesso!")

