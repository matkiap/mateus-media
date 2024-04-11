![logo do projeto](assets/logo.png){ width="300" .center }
# mateus-media


## Como usar?

Você pode chamar os valores de radiação via linha de comando. Por exemplo para o mês de janeiro:

```bash
poetry run medias "arquivo_excel\dados.xlsx" 1
```

O primeiro parâmetro é o arquivo em excel chamado entre aspas; o segundo, o mês que se deseja calcular a média horário (valores aceitos de 1 a 12).

| data  | hora | média da radiação |
|-------|------|-------------------|
| 01/01 | 0    | 90.204924         |
| 01/01 | 1    | 121.235184        |
| 01/01 | 2    | 121.057851        |
| 01/01 | 3    | 152.140825        |
| 01/01 | 4    | 152.186778        |
| 01/01 | 5    | 152.246778        |
| 01/01 | 6    | 152.375730        |
| 01/01 | 7    | 152.347349        |
| ...   | ...  | ...               |
