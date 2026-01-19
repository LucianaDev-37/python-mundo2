# --- PREPARAÇÃO (Fora do loop) ---
lista_pacientes = []
continuar = 'S'

print("=== SISTEMA DE CADASTRO - CLÍNICA FISIO LIFE ===")

while continuar == 'S':
    print(f"\n--- Cadastro do Paciente nº{len(lista_pacientes) + 1} ---")
    
    # --- COLETA DE DADOS (Dentro do loop) ---
    nome = str(input('Nome completo: ')).strip()
    idade = int(input('Idade: '))
    motivo = str(input('Motivo da Fisioterapia: ')).strip()
    
    # Criamos uma "ficha" (dicionário) para este paciente
    paciente = {
        'nome': nome,
        'idade': idade,
        'motivo': motivo
    }
    
    # Guardamos a ficha na nossa lista da clínica
    lista_pacientes.append(paciente)
    
    # --- CONDIÇÃO DE PARADA ---
    continuar = str(input('Deseja cadastrar outro paciente? [S/N]: ')).upper().strip()[0]

# --- RELATÓRIO FINAL (Fora do loop) ---
print("\n" + "="*40)
print(f"CADASTRO FINALIZADO: {len(lista_pacientes)} pacientes registrados.")
print("="*40)

# Mostrando a lista de quem foi cadastrado
for p in lista_pacientes:
    print(f"Paciente: {p['nome']} | Idade: {p['idade']} | Tratamento: {p['motivo']}")

print("\nSistema encerrado. Bom trabalho!")