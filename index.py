import inquirer
import subprocess

def escolher_prefixo():
  try:
    perguntas = [
        inquirer.List(
            'prefixo',
            message="Escolha um prefixo:",
            choices=[
                ('✨ feat', 'feat'),
                ('🐛 fix', 'fix'),
                ('📚 docs', 'docs'),
                ('🚀 chore', 'chore'),
                ('💄 style', 'style'),
                ('🔨 refactor', 'refactor'),
                ('🧪 test', 'test'),
                ('🎉 init', 'init'),
            ]
        )
    ]
    resposta = inquirer.prompt(perguntas)
    return resposta['prefixo']
  except KeyboardInterrupt: 
    print("\nOperação cancelada pelo usuário.")
    exit(0)

def obter_emoji(prefixo):
    emojis = {
        'feat': '✨',
        'fix': '🐛',
        'docs': '📚',
        'chore': '🚀',
        'style': '💄',
        'refactor': '🔨',
        'test': '🧪',
        'init': '	🎉',
    }
    return emojis.get(prefixo, '✨')  # Emoji padrão é '✨' se o prefixo não for encontrado

def criar_commit():
    try:
        prefixo = escolher_prefixo()
        emoji = obter_emoji(prefixo)
        mensagem = input("Digite a mensagem do commit: ")

        commit_mensagem = f"{emoji} {prefixo}: {mensagem}"
        
        subprocess.run(["git", "commit", "-m", commit_mensagem])

    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        exit(0)

if __name__ == "__main__":
    criar_commit()
