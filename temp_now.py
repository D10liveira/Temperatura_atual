import requests

# Dicionário de tradução das condições meteorológicas
traducao_condicoes = {
    'Clear': 'Céu Limpo',
    'Clouds': 'Nuvens',
    'Drizzle': 'Garoinha',
    'Rain': 'Chuva',
    'Thunderstorm': 'Tempestade',
    'Snow': 'Neve',
    'Mist': 'Névoa',
    'Fog': 'Nevoeiro',
    'Haze': 'Neblina',
    'Smoke': 'Fumaça',
    'Dust': 'Poeira',
    'Sand': 'Areia',
    'Ash': 'Cinzas',
    'Squall': 'Rajadas de Vento',
    'Tornado': 'Tornado'
}


def obter_clima(api_key, cidade, pais):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={
        cidade},{pais}&appid={api_key}&units=metric'
    resposta = requests.get(url)
    dados = resposta.json()

    if dados['cod'] == 200:
        clima_cod = dados['weather'][0]['main']
        if clima_cod in traducao_condicoes:
            clima = traducao_condicoes[clima_cod]
        else:
            clima = clima_cod
        temperatura = dados['main']['temp']
        umidade = dados['main']['humidity']
        vento = dados['wind']['speed']

        print(f'Condição: {clima}')
        print(f'Temperatura: {temperatura}°C')
        print(f'Umidade: {umidade}%')
        print(f'Vento: {vento} m/s')
    else:
        print('Não foi possível obter informações de clima para esta localização.')


def main():
    api_key = 'dfda2c514b9860c116c076b55cb1a9a8'
    cidade = input('Digite o nome da cidade: ')
    pais = input('Digite o código do país (ex: BR, US): ')

    obter_clima(api_key, cidade, pais)


if __name__ == '__main__':
    main()
