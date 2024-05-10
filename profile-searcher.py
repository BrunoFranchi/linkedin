import requests

# Token de acesso
access_token ='AQVwz-14ltDtQWI7o21mwZ4iyofSQrutyXb3atuye0wkA58Wcn8yeoI_lBU1dgu-kmFli0yxDzeCY6VYPWI3bw8WFYCvbBrTiiwm7KwE3m2oI7k-DxQz9o5tNwfwURKFM8dw_mPpl9MUEbUtp4RiDke0o-xTkmqCnznzAmHOJtzvkazppYAmIhg1k9wQPpbG-2URH4_CJ1dn5YnmNakH1Q2kFlD2b1lr_2EE2uG0mb4Mve0KBA5pnQp0CAR8pbeJGeZp2oIRifxrD1J_KLUCjhK4GZnmDzgcXNDT0nkuLQfxT6TQvZQCKzwQYtzI94mBmB-doE2zfPmW2_wW55-GQO-_p84eGA'

# Endpoint para obter informações do usuário
me_url = 'https://api.linkedin.com/v2/me'

# Headers com o token de autorização
headers = {
    'Authorization': f'Bearer {access_token}',
    'Connection': 'Keep-Alive',
    'Content-Type': 'application/json',
}

# Fazendo a requisição GET para obter informações do usuário
response = requests.get(me_url, headers=headers)

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    # Obtém o ID do usuário do LinkedIn
    user_data = response.json()
    user_id = user_data['id']
    print(user_id)
    
    # Endpoint para criação de post
    post_url = 'https://api.linkedin.com/v2/ugcPosts'
    
    # Corpo do post
    post_body = {
        "author": f"urn:li:person:{user_id}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": "Este é um post de teste através da API do linkedin usando Python!"
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    # Fazendo a requisição POST para criar o post
    response = requests.post(post_url, json=post_body, headers=headers)

    # Verifica se a requisição foi bem sucedida
    if response.status_code == 201:
        print("Post criado com sucesso!")
    else:
        print("Erro ao criar o post:", response.text)
else:
    print("Erro ao obter informações do usuário:", response.text)
