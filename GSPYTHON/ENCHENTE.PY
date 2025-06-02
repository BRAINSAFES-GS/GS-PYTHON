print("Alunos:\nRafael Moraes Ribeiro dos Santos RM:565075\nGuilherme Andrade Amaral RM:562112\nEnrico Bagli RM:562541")

# Sistema de Monitoramento de Enchentes 

# Lista para armazenar os dados dos registros
dados = []

# Função para exibir o menu
def exibir_menu():
    print("\n===============================")
    print("🌊💧 Sistema de Monitoramento de Enchentes 💧🌊")
    print("===============================")
    print("📅 1. Cadastrar dados do dia")
    print("📊 2. Visualizar todos os dados")
    print("🚨 3. Analisar risco no último dado")
    print("📝 4. Gerar relatório de risco")
    print("❌ 5. Sair")
    print("===============================")

# Função para cadastrar dados
def cadastrar_dados():
    print("\n📅 --- Cadastro de Dados ---")
    data = input("📆 Informe a data (DD/MM/AAAA): ")
    
    while True:
        try:
            chuva = float(input("🌧️ Informe a quantidade de chuva (mm): "))
            if chuva < 0:
                print("⚠️ Chuva não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("❌ Valor inválido. Digite um número.")

    while True:
        try:
            nivel_rio = float(input("🌊 Informe o nível do rio (m): "))
            if nivel_rio < 0:
                print("⚠️ Nível do rio não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("❌ Valor inválido. Digite um número.")

    registro = {
        "data": data,
        "chuva": chuva,
        "nivel_rio": nivel_rio
    }

    dados.append(registro)
    print("✅ Dados cadastrados com sucesso!")

# Função para exibir os dados
def exibir_dados():
    print("\n📊 --- Dados Cadastrados ---")
    if len(dados) == 0:
        print("🚫 Nenhum dado cadastrado.")
    else:
        for registro in dados:
            print(f"📅 Data: {registro['data']} | 🌧️ Chuva: {registro['chuva']} mm | 🌊 Nível do Rio: {registro['nivel_rio']} m")

# Função para analisar risco
def analisar_risco(registro):
    return registro['chuva'] > 80 or registro['nivel_rio'] > 5

# Função para analisar o risco do último dado cadastrado
def analisar_ultimo_risco():
    print("\n🚨 --- Análise de Risco no Último Dado ---")
    if len(dados) == 0:
        print("🚫 Nenhum dado cadastrado para análise.")
    else:
        ultimo = dados[-1]
        if analisar_risco(ultimo):
            print(f"⚠️  📅 Data: {ultimo['data']} | 🌧️ Chuva: {ultimo['chuva']} mm | 🌊 Nível do Rio: {ultimo['nivel_rio']} m --> 🔴 RISCO DE ENCHENTE")
        else:
            print(f"✅  📅 Data: {ultimo['data']} | 🌧️ Chuva: {ultimo['chuva']} mm | 🌊 Nível do Rio: {ultimo['nivel_rio']} m --> 🟢 Sem risco de enchente")

# Função para gerar relatório de risco
def gerar_relatorio():
    print("\n📝 --- Relatório de Dias com Risco de Enchente ---")
    risco_encontrado = False
    for registro in dados:
        if analisar_risco(registro):
            print(f"⚠️  📅 Data: {registro['data']} | 🌧️ Chuva: {registro['chuva']} mm | 🌊 Nível do Rio: {registro['nivel_rio']} m --> 🔴 RISCO DE ENCHENTE")
            risco_encontrado = True
    if not risco_encontrado:
        print("✅ Nenhum dia com risco de enchente encontrado.")

# Programa Principal
while True:
    exibir_menu()
    opcao = input("👉 Escolha uma opção: ")

    if opcao == "1":
        cadastrar_dados()
    elif opcao == "2":
        exibir_dados()
    elif opcao == "3":
        analisar_ultimo_risco()
    elif opcao == "4":
        gerar_relatorio()
    elif opcao == "5":
        print("👋 Encerrando o sistema. Até mais!")
        break
    else:
        print("❌ Opção inválida. Escolha novamente.")
# Fim do programa