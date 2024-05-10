import requests

def search_jobs(access_token, keywords, location):
    # Endpoint para buscar vagas de emprego
    jobs_url = 'https://api.linkedin.com/v2/jobSearch'

    # Parâmetros da busca
    params = {
        'keywords': keywords,
        'location': f'urn:li:postalCode:{location}',
        'count': 5  # Número de resultados desejados
    }

    # Headers com o token de autorização
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
        'Content-Type': 'application/json',
    }

    # Fazendo a requisição GET para buscar vagas de emprego
    response = requests.get(jobs_url, params=params, headers=headers)

    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        # Obtém os dados das vagas de emprego
        job_data = response.json()
        for job in job_data['elements']:
            job_title = job.get('title', 'N/A')
            company_name = job.get('companyName', 'N/A')
            job_location = job.get('location', {}).get('name', 'N/A')
            job_description = job.get('description', 'N/A')
            
            print("Título:", job_title)
            print("Empresa:", company_name)
            print("Localização:", job_location)
            print("Descrição:", job_description)
            print("\n---\n")
    else:
        print("Erro ao buscar vagas de emprego:", response.status_code)

# Token de acesso
access_token ='Seu_access_token'

# Palavras-chave para a busca de vagas de emprego
keywords = input("Informe as habilidades desejadas para a busca de vagas de emprego: ")

# Localização para a busca de vagas de emprego (cidade)
location = input("Informe a cidade para a busca de vagas de emprego: ")

# Realiza a busca de vagas de emprego
search_jobs(access_token, keywords, location)
