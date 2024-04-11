import pandas as pd
import pytest
from mateus_media.calcular_medias_mensais import calcular_medias_mensais


@pytest.fixture
def exemplo_dataframe():
    # Cria um exemplo de DataFrame para teste
    data = {
        'data': pd.date_range(start='2024-01-01', end='2024-01-31', freq='H'),
        'hora': range(24),
        'radiacao': [10] * 31 * 24,
    }
    return pd.DataFrame(data)


def test_calcular_medias_mensais(exemplo_dataframe):
    # Testa se a função retorna um DataFrame
    assert isinstance(
        calcular_medias_mensais('caminho/do/arquivo.xlsx', 1), pd.DataFrame
    )

    # Testa se a função retorna as médias corretas para um mês específico
    resultado_janeiro = calcular_medias_mensais('caminho/do/arquivo.xlsx', 1)
    assert (
        len(resultado_janeiro) == 31 * 24
    )  # Verifica se todas as horas do mês estão presentes
    assert (
        resultado_janeiro['média da radiação'].mean() == 10
    )  # Verifica se a média é 10


def test_calcular_medias_mensais(exemplo_dataframe):
    # Testa se a função retorna um DataFrame
    assert isinstance(
        calcular_medias_mensais('caminho/do/arquivo.xlsx', 1), pd.DataFrame
    )

    # Testa se a função retorna as médias corretas para um mês específico
    resultado_janeiro = calcular_medias_mensais('caminho/do/arquivo.xlsx', 1)
    assert (
        len(resultado_janeiro) == 31 * 24
    )  # Verifica se todas as horas do mês estão presentes
    assert (
        resultado_janeiro['média da radiação'].mean() == 10
    )  # Verifica se a média é 10

    # Testa se a função lança uma exceção quando o caminho do arquivo não existe
    with pytest.raises(FileNotFoundError, match='caminho não encontrado'):
        calcular_medias_mensais('caminho/inexistente/arquivo.xlsx', 1)
