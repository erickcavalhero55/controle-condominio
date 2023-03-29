import MySQLdb


def conectar():
    try:
        conn = MySQLdb.connect(
            db='portaria',
            host='localhost',
            user='root',
            password='270921'
        )
        return conn
    except MySQLdb.Error as e:
        print(f'Erro ao conectar ao Mysql {e}')


def desconectar(conn):

    if conn:
        conn.close()


def listar():

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cadastro')
    cadastro = cursor.fetchall()

    if len(cadastro) > 0:
        print('listando cadastro....')
        print('.......................')
        for cadastro in cadastro:
            print(f'ID: {cadastro[0]}')
            print(f'UNIDADE: {cadastro[1]}')
            print(f'NOME: {cadastro[2]}')
            print(f'SOBRENOME: {cadastro[3]}')
            print(f'NASCIMENTO: {cadastro[4]}')
            print(f'EMAIL: {cadastro[5]}')
            print(f'TELEFONE: {cadastro[6]}')
            print(f'CELULAR: {cadastro[7]}')
            print(f'RG: {cadastro[8]}')
            print(f'CPF: {cadastro[9]}')
            print(f'TIPO_MORADOR: {cadastro[10]}')
            print('.......................')

    else:
        print('Não existe unidade cadastrada.')


def inserir():
    conn = conectar()
    cursor = conn.cursor()

    unidade = int(input('Informe o numero da unidade: '))
    nome = input('Informe o nome que sera cadastrado: ')
    sobrenome = input('Informe o sobrenome que sera cadastrado: ')
    nascimento = int(input('Informe a data de nascimento que sera cadastrado: '))
    email = input('Informe o email que sera cadastrado: ')
    telefone = int(input('Informe o numero de telefone que sera cadastrado: '))
    celular = int(input('Informe o numero de celular que sera cadastrado: '))
    rg = int(input('Informe o numero de R.G que sera cadastrado: '))
    cpf = int(input('Informe o numero do CPF que sera cadastrado: '))
    tipo_morador = input('Informe o tipo de morador que sera cadastrado: ')

    cursor.execute(f"INSERT INTO cadastro (unidade, nome, sobrenome, nascimento, email, telefone, celular, rg, cpf, tipo_morador) VALUES ({unidade},{nome},{sobrenome},{nascimento},{email},{telefone},{celular},{rg},{cpf},{tipo_morador})")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O Cadastro {unidade} foi inserido com sucesso. ')
    else:
        print('Não foi possivel cadastrar ')
    desconectar(conn)


def atualizar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Digite o numero do codigo: '))
    unidade = int(input('Informe o numero da unidade: '))
    nome = input('Informe o nome que sera cadastrado: ')
    sobrenome = input('Informe o sobrenome que sera cadastrado: ')
    nascimento = int(input('Informe a data de nascimento que sera cadastrado: '))
    email = input('Informe o email que sera cadastrado: ')
    telefone = int(input('Informe o numero de telefone que sera cadastrado: '))
    celular = int(input('Informe o numero de celular que sera cadastrado: '))
    rg = int(input('Informe o numero de R.G que sera cadastrado: '))
    cpf = int(input('Informe o numero do CPF que sera cadastrado: '))
    tipo_morador = input('Informe o tipo de morador que sera cadastrado: ')

    cursor.execute(f"UPDATE cadastro SET unidade={unidade}, nome='{nome}','sobrenome='{sobrenome}',nascimento={nascimento},email='{email}', telefone={telefone}, celular={celular}, rg={rg}, cpf={cpf}, tipo_morador='{tipo_morador}'WHERE id{codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O Cadastro {unidade} foi inserido com sucesso. ')
    else:
        print('Não foi possivel atualiazar ')
    desconectar(conn)


def deletar():
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o codigo do cadastro'))

    cursor.execute(f'DELETE FROM cadastro WHERE id={codigo}')
    conn.commit()

    if cursor.rowcount == 1:
        print('Cadastro excluido com sucesso.')
    else:
        print('Não foi possivel DELETAR. ')
    desconectar(conn)


def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
