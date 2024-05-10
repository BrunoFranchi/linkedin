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
    
    # Endpoint para obter as últimas publicações com o ID do usuário
    posts_url = f'https://api.linkedin.com/v2/ugcPosts?q=authors&authors=List({user_id})&count=5'

    # Fazendo a requisição GET para obter as últimas publicações
    response = requests.get(posts_url, headers=headers)

    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        # Obtém os dados das últimas publicações
        posts_data = response.json()
        for post in posts_data['elements']:
            post_content = post.get('specificContent', {}).get('com.linkedin.ugc.ShareContent', {}).get('shareCommentary', {}).get('text', 'No content')
            print("Post Content:", post_content)
    else:
        print("Erro ao obter as publicações:", response.status_code)
else:
    print("Erro ao obter informações do usuário:", response.status_code)