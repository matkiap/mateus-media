import subprocess
import tempfile
import pandas as pd
import numpy as np

def test_calcular_medias_com_planilha_aleatoria():
    # Gerar dados aleatórios para a planilha
    data = {
        'data': pd.date_range(start='2024-01-01', end='2024-01-31', freq='H'),
        'hora': np.random.randint(0, 24, size=744),
        'radiacao': np.random.uniform(0, 2000, size=744)
    }
    df = pd.DataFrame(data)

    # Salvar os dados em um arquivo Excel temporário
    temp_excel_path = tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False).name
    df.to_excel(temp_excel_path, index=False)

    # Caminho para o seu CLI
    caminho_cli = r"C:\Users\franc\mateus-media\mateus_media\cli.py"

    # Executa o CLI com o arquivo Excel aleatório como argumento
    result = subprocess.run(["python", caminho_cli, temp_excel_path, "1"], capture_output=True)

    # Verifica se a execução foi bem-sucedida (código de retorno 0)
    assert result.returncode == 0

    # Verifica se a saída contém as informações esperadas
    assert "Médias horárias de radiação para o mês selecionado:" in result.stdout.decode()
    assert "Resultado:" in result.stdout.decode()

    # Remover o arquivo Excel temporário após o teste
    os.remove(temp_excel_path)
