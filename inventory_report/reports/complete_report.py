from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(products_list):
        simple_report = SimpleReport.generate(products_list)
        complete_report = simple_report + "\nProdutos estocados por empresa:"
        companies_products = CompleteReport.__get_companies_products(
            products_list
        )

        for company in companies_products:
            complete_report += f"\n- {company}: {companies_products[company]}"

        return complete_report + "\n"

    @staticmethod
    def __get_companies_products(product_list):
        companies = {}

        for product in product_list:
            company_name = product["nome_da_empresa"]
            if company_name in companies:
                companies[company_name] += 1
            else:
                companies[company_name] = 1

        return companies
