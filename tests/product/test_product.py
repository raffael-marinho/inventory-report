from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "Produto x",
        "Empresa y",
        "20/09/2022",
        "20/09/2023",
        "123456789",
        "instruções",
    )
    assert product.id == 1
    assert product.nome_do_produto == "Produto x"
    assert product.nome_da_empresa == "Empresa y"
    assert product.data_de_fabricacao == "20/09/2022"
    assert product.data_de_validade == "20/09/2023"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "instruções"
