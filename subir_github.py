import os
import subprocess


def rodar_comando(comando):
    print(f"\nExecutando: {comando}")
    resultado = subprocess.run(comando, shell=True)

    if resultado.returncode != 0:
        print(f"\nErro ao executar: {comando}")
        exit()


def criar_gitignore():
    conteudo = """__pycache__/
*.pyc
instance/
*.db
.env
venv/
.venv/
"""

    if not os.path.exists(".gitignore"):
        with open(".gitignore", "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
        print(".gitignore criado com sucesso.")
    else:
        print(".gitignore já existe.")


def main():
    print("=== Script para enviar projeto ao GitHub ===")

    if not os.path.exists(".git"):
        rodar_comando("git init")
    else:
        print("Repositório Git já iniciado.")

    criar_gitignore()

    mensagem = input("\nDigite a mensagem do commit: ").strip()

    if not mensagem:
        mensagem = "Adiciona projeto"

    repo_url = input("\nCole a URL do repositório GitHub: ").strip()

    if not repo_url:
        print("Você precisa informar a URL do repositório.")
        exit()

    rodar_comando("git add .")
    rodar_comando(f'git commit -m "{mensagem}"')
    rodar_comando("git branch -M main")

    remotes = subprocess.run(
        "git remote",
        shell=True,
        capture_output=True,
        text=True
    )

    if "origin" not in remotes.stdout:
        rodar_comando(f"git remote add origin {repo_url}")
    else:
        rodar_comando(f"git remote set-url origin {repo_url}")

    rodar_comando("git push -u origin main")

    print("\nProjeto enviado para o GitHub com sucesso!")


if __name__ == "__main__":
    main()