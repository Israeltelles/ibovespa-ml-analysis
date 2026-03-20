import pandas as pd
from pathlib import Path


class IbovespaETL:

    def __init__(self, path):
        self.path = Path(path)
        self.df = None

        self.colspecs = [
            (2, 10), (10, 12), (12, 24), (27, 39),
            (56, 69), (69, 82), (82, 95), (108, 121),
            (152, 170), (170, 188)
        ]

        self.columns = [
            'data_pregao', 'codbdi', 'sigla_acao', 'nome_acao',
            'preco_abertura', 'preco_maximo', 'preco_minimo',
            'preco_fechamento', 'qtd_negocios', 'volume_negocios'
        ]

    def extract(self, file_path):
        self.df = pd.read_fwf(
            file_path,
            colspecs=self.colspecs,
            names=self.columns,
            skiprows=1
        )

    def transform(self):
        self._filter_stocks()
        self._parse_date()
        self._parse_values()

    def _filter_stocks(self):
        self.df = self.df[self.df['codbdi'] == 2].drop(columns=['codbdi'])

    def _parse_date(self):
        self.df['data_pregao'] = pd.to_datetime(
            self.df['data_pregao'],
            format='%Y%m%d'
        )

    def _parse_values(self):
        cols = [
            'preco_abertura',
            'preco_maximo',
            'preco_minimo',
            'preco_fechamento'
        ]

        for col in cols:
            self.df[col] = (self.df[col] / 100).astype(float)

    def load(self, output_file):
        self.df.to_csv(output_file, index=False)

    def run(self, name_file, years, file_type, final_file):
        dfs = []

        for year in years:
            file_path = self.path / f"{name_file}{year}.{file_type}"

            self.extract(file_path)
            self.transform()
            dfs.append(self.df.copy())

        self.df = pd.concat(dfs, ignore_index=True)

        output_path = self.path / f"{final_file}.csv"
        self.load(output_path)

if __name__ == "__main__":
    path = r'D:/Python/ibovespa-ml-analysis/data'
    name_file = 'COTAHIST_A'
    years = ['2023', '2024', '2025', '2026']
    file_type = 'TXT'
    final_file = 'all_ibovespa'

    etl = IbovespaETL(path)
    etl.run(name_file, years, file_type, final_file)
