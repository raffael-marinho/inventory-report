from collections import Counter
# https://docs.python.org/3/library/collections.html


class SimpleReport:

    @staticmethod
    def generate(list):
        data_fabricacao = min(dict["data_de_fabricacao"] for dict in list)
        print(data_fabricacao)

        data_validade = min(dict["data_de_validade"] for dict in list)
        print(data_validade)

        nome_empresa = Counter(
            dict["nome_da_empresa"] for dict in list
        ).most_common(1)[0][0]

        print('nome da empresa - linha 15', nome_empresa)

        return (
            f"Data de fabricação mais antiga: {data_fabricacao}\n"
            f"Data de validade mais próxima: {data_validade}\n"
            f"Empresa com mais produtos: {nome_empresa}"
        )
