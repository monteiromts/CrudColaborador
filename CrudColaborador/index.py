import mysql.connector

#conecção Mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123321"
)

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS escola")
mydb.database = "escola"
cursor.execute("""
    CREATE TABLE IF NOT EXISTS NewColaborador (
        idUsuario INT AUTO_INCREMENT PRIMARY KEY,
        matricula INT NOT NULL UNIQUE,
        curriculo VARCHAR(255),
        imagem VARCHAR(255) NOT NULL,
        tagSetor VARCHAR(255) NOT NULL,
        departamento VARCHAR(255) NOT NULL,
        ativo TINYINT(1) NOT NULL CHECK (ativo IN (0,1)),
        tipo VARCHAR(255),
        tagSetorEng VARCHAR(255) NOT NULL,
        cargoEng VARCHAR(255) NOT NULL,
        dataNascimento DATE,
        departamento_hibrido VARCHAR(255)
    )
""")


print("Tabela criada com Exito")

#Inclusão do usuários
def adicionar_usuario(matricula, curriculo, imagem, tagSetor, departamento, ativo, tipo, tagSetorEng, cargoEng, dataNascimento, departamento_hibrido):
    cursor.execute("""
        INSERT INTO NewColaborador (matricula, curriculo, imagem, tagSetor, departamento, ativo, tipo, tagSetorEng, cargoEng, dataNascimento, departamento_hibrido)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (matricula, curriculo, imagem, tagSetor, departamento, ativo, tipo, tagSetorEng, cargoEng, dataNascimento, departamento_hibrido))
    mydb.commit()

#Listar Usuários
def listar_usuarios():
    cursor.execute("SELECT * FROM NewColaborador")
    Colaboradores = cursor.fetchall()
    for usuario in Colaboradores:
        print(usuario) 

#Atualizar Usuáios
def atualizar_usuario(matricula, curriculo, imagem, tagSetor, departamento, ativo, tipo, tagSetorEng, cargoEng, dataNascimento, departamento_hibrido):
    cursor.execute("""
        UPDATE NewColaorador (matricula, curriculo, imagem, tagSetor, departamento, ativo, tipo, tagSetorEng, cargoEng, dataNascimento, departamento_hibrido)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""), (matricula, curriculo, imagem, tagSetor, departamento, ativo, tipo, tagSetorEng, cargoEng, dataNascimento, departamento_hibrido)
    mydb.commit()

#Deletar Usuários
def deletar_usuario(id):
    cursor.execute("DELETE FROM NewColaborador WHERE id = %s", (id))
    mydb.commit()

#Exibir Menu
def menu():
    print("\n1. Adicionar Usuario")
    print("2. Listar Usuarios")
    print("3. Atualizar Usuario")
    print("4 Delatar Usuario")
    print("5. Sair")

    # Loop principal do menu
while True:
    menu()
    escolha = int(input("Escolha uma opcao: "))

    if escolha == 1:
        matricula =int(input("Digite a matricula do usuário:"))
        curriculo = (input("Digite o currículo do usuário:"))
        imagem = (input("Digitar Rota da Imagem:"))
        tagSetor = (input("Digite o Setor do colaborador:"))
        departamento = (input("Digitar o departtamento do colaborardor:"))




        adicionar_usuario(nome, idade)
        print("Usuário adicionado com sucesso!")
    elif escolha == 2:
        print("\nTodos os usuários:")
        listar_usuarios()
    elif escolha == 3:
        id = int(input("Digite o ID do usuário a ser atualizado: "))
        nome = input("Digite o novo nome do usuário: ")
        idade = int(input("Digite a nova idade do usuário: "))
        atualizar_usuario(id, nome, idade)
        print("Usuário atualizado com sucesso!")
    elif escolha == 4:
        id = int(input("Digite o ID do usuário a ser deletado: "))
        deletar_usuario(id)
        print("Usuário deletado com sucesso!")
    elif escolha == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
