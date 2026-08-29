import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date


# ============================================================
# CORES
# ============================================================

COR_FUNDO = "#F4F7FB"
COR_AZUL = "#1F3A6D"
COR_AZUL_CLARO = "#EEF3FF"

COR_BOTAO = "#315EFB"
COR_BOTAO_HOVER = "#2447C6"

COR_TEXTO = "#1D2939"
COR_TEXTO_SECUNDARIO = "#667085"

COR_CARD = "#FFFFFF"
COR_BORDA = "#D8DFEA"

COR_VERDE = "#EAF8EF"
COR_AMARELO = "#FFF7E6"
COR_VERMELHO = "#FFF0F0"


# ============================================================
# BASE DE CONHECIMENTO
# ============================================================

regras = [

    {
        "condicoes": {
            "urgencia": "super urgente"
        },

        "decisao":
            "A prova é hoje. Entre imediatamente em modo de revisão final.",

        "explicacao":
            "Como a prova acontece hoje, não existe tempo suficiente para aprender "
            "grandes conteúdos novos. A prioridade agora é revisar o que você já sabe.",

        "plano":
            "1. Não tente estudar toda a matéria.\n"
            "2. Revise fórmulas e conceitos principais.\n"
            "3. Resolva poucas questões importantes.\n"
            "4. Revise seus erros mais frequentes.\n"
            "5. Descanse antes da prova."
    },

    {
        "condicoes": {
            "urgencia": "muito urgente",
            "conteudo_atrasado": True
        },

        "decisao":
            "A prova é amanhã. Priorize somente os assuntos essenciais.",

        "explicacao":
            "Falta apenas um dia para a prova e ainda existe conteúdo atrasado. "
            "Tentar estudar tudo agora pode gerar sobrecarga.",

        "plano":
            "1. Escolha 3 ou 4 assuntos importantes.\n"
            "2. Revise apenas os pontos principais.\n"
            "3. Resolva exercícios.\n"
            "4. Revise os erros.\n"
            "5. Durma adequadamente."
    },

    {
        "condicoes": {
            "urgencia": "muito urgente",
            "materia_pratica": True
        },

        "decisao":
            "Concentre seu tempo em exercícios e provas anteriores.",

        "explicacao":
            "A prova é amanhã e a matéria exige prática. "
            "Resolver questões permite encontrar rapidamente suas dificuldades.",

        "plano":
            "1. Resolva uma prova anterior.\n"
            "2. Marque os erros.\n"
            "3. Revise a teoria relacionada aos erros.\n"
            "4. Resolva novamente as questões."
    },

    {
        "condicoes": {
            "urgencia": "urgente",
            "dificuldade": "alta",
            "conteudo_atrasado": True
        },

        "decisao":
            "Monte um plano intensivo focado nos assuntos prioritários.",

        "explicacao":
            "Faltam poucos dias, a matéria possui alta dificuldade "
            "e existem conteúdos atrasados.",

        "plano":
            "1. Separe os assuntos por prioridade.\n"
            "2. Estude primeiro os fundamentais.\n"
            "3. Resolva exercícios após cada assunto.\n"
            "4. Reserve o último dia para revisão."
    },

    {
        "condicoes": {
            "urgencia": "urgente",
            "cansado": True,
            "dificuldade_concentracao": True
        },

        "decisao":
            "Estude em sessões curtas e inclua pausas obrigatórias.",

        "explicacao":
            "A prova está próxima, mas estudar cansado e sem concentração "
            "pode diminuir muito o rendimento.",

        "plano":
            "1. Estude por 25 minutos.\n"
            "2. Descanse por 5 minutos.\n"
            "3. Repita o ciclo.\n"
            "4. Trabalhe somente com conteúdos prioritários."
    },

    {
        "condicoes": {
            "urgencia": "alta prioridade",
            "conteudo_atrasado": True
        },

        "decisao":
            "Use os próximos dias para recuperar primeiro os conteúdos mais importantes.",

        "explicacao":
            "Ainda existe algum tempo, mas será necessário organizar "
            "os assuntos por prioridade.",

        "plano":
            "1. Liste o conteúdo atrasado.\n"
            "2. Classifique por prioridade.\n"
            "3. Comece pelos assuntos mais importantes.\n"
            "4. Reserve os últimos dias para revisão."
    },

    {
        "condicoes": {
            "urgencia": "alta prioridade",
            "materia_pratica": True
        },

        "decisao":
            "Alterne teoria e exercícios todos os dias até a prova.",

        "explicacao":
            "Como faltam poucos dias e a matéria é prática, exercícios frequentes "
            "ajudam a consolidar o aprendizado.",

        "plano":
            "1. Revise um assunto.\n"
            "2. Resolva exercícios.\n"
            "3. Corrija os erros.\n"
            "4. Refaça as questões no dia seguinte."
    },

    {
        "condicoes": {
            "urgencia": "atencao",
            "dificuldade": "alta"
        },

        "decisao":
            "Comece agora um cronograma estruturado.",

        "explicacao":
            "Ainda existem vários dias, mas a dificuldade da matéria exige "
            "organização antecipada.",

        "plano":
            "1. Divida os assuntos pelos dias disponíveis.\n"
            "2. Estude teoria e prática no mesmo dia.\n"
            "3. Faça revisões periódicas.\n"
            "4. Reserve os dias finais para simulados."
    },

    {
        "condicoes": {
            "urgencia": "planejamento",
            "conteudo_atrasado": False
        },

        "decisao":
            "Você possui tempo suficiente. Siga um cronograma progressivo até a prova.",

        "explicacao":
            "A prova ainda está relativamente distante e você não possui conteúdo atrasado.",

        "plano":
            "1. Estude um pouco todos os dias.\n"
            "2. Faça revisões semanais.\n"
            "3. Resolva exercícios periodicamente.\n"
            "4. Intensifique a revisão perto da prova."
    },

    {
        "condicoes": {
            "dificuldade_concentracao": True,
            "cansado": False
        },

        "decisao":
            "Use a técnica Pomodoro e elimine distrações.",

        "explicacao":
            "Você não está cansado, mas informou dificuldade de concentração.",

        "plano":
            "1. Afaste o celular.\n"
            "2. Estude por 25 minutos.\n"
            "3. Descanse por 5 minutos.\n"
            "4. Escreva o que aprendeu sem consultar."
    },

    {
        "condicoes": {
            "cansado": True,
            "prova_proxima": False
        },

        "decisao":
            "Descanse antes de continuar estudando.",

        "explicacao":
            "Não existe uma prova imediata e você está cansado.",

        "plano":
            "1. Faça uma pausa maior.\n"
            "2. Descanse adequadamente.\n"
            "3. Retome quando estiver mais disposto.\n"
            "4. Evite estudar muitas horas seguidas."
    },

    {
        "condicoes": {
            "materia_pratica": True,
            "dificuldade": "alta",
            "tempo": "longo"
        },

        "decisao":
            "Combine teoria curta com bastante prática.",

        "explicacao":
            "A matéria é prática, difícil e você possui bastante tempo disponível.",

        "plano":
            "1. Leia a teoria.\n"
            "2. Observe um exemplo.\n"
            "3. Resolva exercícios sozinho.\n"
            "4. Corrija seus erros.\n"
            "5. Tente novamente."
    },

    {
        "condicoes": {
            "dificuldade": "alta",
            "materia_pratica": False
        },

        "decisao":
            "Use explicação ativa, resumos e mapas mentais.",

        "explicacao":
            "A matéria é mais teórica e possui alta dificuldade.",

        "plano":
            "1. Leia um pequeno trecho.\n"
            "2. Feche o material.\n"
            "3. Explique com suas palavras.\n"
            "4. Confira o que esqueceu.\n"
            "5. Crie um resumo curto."
    },

    {
        "condicoes": {
            "conteudo_atrasado": True,
            "tempo": "curto"
        },

        "decisao":
            "Trabalhe somente com os conteúdos essenciais.",

        "explicacao":
            "Você possui pouco tempo e ainda existe conteúdo atrasado.",

        "plano":
            "1. Escolha os temas mais importantes.\n"
            "2. Ignore detalhes secundários por enquanto.\n"
            "3. Resolva algumas questões.\n"
            "4. Revise seus erros."
    },

    {
        "condicoes": {
            "tempo": "medio",
            "dificuldade": "media",
            "conteudo_atrasado": False
        },

        "decisao":
            "Divida seu tempo entre teoria, prática e revisão.",

        "explicacao":
            "Sua situação está equilibrada e permite trabalhar diferentes formas de estudo.",

        "plano":
            "1. Use 40% do tempo para teoria.\n"
            "2. Use 40% para exercícios.\n"
            "3. Use 20% para revisão.\n"
            "4. Ajuste conforme suas dificuldades."
    },

    {
        "condicoes": {},

        "decisao":
            "Use uma estratégia equilibrada de teoria, exercícios e revisão.",

        "explicacao":
            "Nenhuma situação crítica específica foi identificada.",

        "plano":
            "1. Estude a teoria.\n"
            "2. Faça um resumo.\n"
            "3. Resolva exercícios.\n"
            "4. Revise seus erros."
    }
]


# ============================================================
# TEMPO DIARIO
# ============================================================

def obter_tempo_diario():

    if tempo_var.get() == "curto":
        return "45 minutos"

    elif tempo_var.get() == "medio":
        return "1 hora e 30 minutos"

    else:
        return "2 horas e 30 minutos"


# ============================================================
# GERAR CRONOGRAMA
# ============================================================

def gerar_cronograma(dados_urgencia):

    dias = dados_urgencia["dias"]

    dificuldade = dificuldade_var.get()

    materia_pratica = pratica_var.get() == "Sim"
    atrasado = atrasado_var.get() == "Sim"
    cansado = cansado_var.get() == "Sim"
    concentracao = concentracao_var.get() == "Sim"

    tempo_diario = obter_tempo_diario()


    if dias is None:

        return (
            "CRONOGRAMA SEMANAL\n\n"

            f"Tempo diário recomendado: {tempo_diario}\n\n"

            "SEGUNDA\n"
            "• Aprender conteúdo novo.\n\n"

            "TERÇA\n"
            "• Continuar teoria e fazer exercícios.\n\n"

            "QUARTA\n"
            "• Revisar conteúdos anteriores.\n\n"

            "QUINTA\n"
            "• Aprender novo conteúdo e praticar.\n\n"

            "SEXTA\n"
            "• Resolver exercícios e corrigir erros.\n\n"

            "SÁBADO\n"
            "• Revisão geral da semana.\n\n"

            "DOMINGO\n"
            "• Descanso ou revisão leve."
        )


    if dias == 0:

        return (
            "CRONOGRAMA PARA HOJE\n\n"

            "BLOCO 1 - 30 minutos\n"
            "• Revise fórmulas, conceitos e resumos.\n\n"

            "BLOCO 2 - 30 minutos\n"
            "• Revise os assuntos em que você mais erra.\n\n"

            "BLOCO 3 - 20 minutos\n"
            "• Resolva poucas questões importantes.\n\n"

            "ANTES DA PROVA\n"
            "• Pare de estudar com antecedência.\n"
            "• Descanse e faça uma refeição leve."
        )


    if dias == 1:

        return (
            "CRONOGRAMA PARA AS PRÓXIMAS 24 HORAS\n\n"

            "MANHÃ\n"
            "• Revisar assuntos mais importantes.\n\n"

            "TARDE\n"
            "• Resolver exercícios ou prova anterior.\n\n"

            "NOITE\n"
            "• Revisar erros e resumos.\n\n"

            "IMPORTANTE\n"
            "• Não vire a noite estudando."
        )


    if dias <= 3:

        texto = (
            f"CRONOGRAMA INTENSIVO DE {dias} DIAS\n\n"

            f"Tempo diário: {tempo_diario}\n\n"

            "DIA 1\n"
            "• Conteúdos de maior prioridade.\n"
            "• Exercícios logo após a teoria.\n\n"
        )

        if dias == 3:

            texto += (
                "DIA 2\n"
                "• Conteúdos restantes.\n"
                "• Exercícios e correção dos erros.\n\n"
            )

        texto += (
            f"DIA {dias} - VÉSPERA\n"
            "• Revisão geral.\n"
            "• Questões-chave.\n"
            "• Descanso adequado."
        )

        return texto


    if dias <= 7:

        dias_teoria = max(
            2,
            dias - 3
        )

        return (
            f"CRONOGRAMA DE {dias} DIAS\n\n"

            f"Tempo diário: {tempo_diario}\n\n"

            f"DIAS 1 A {dias_teoria}\n"
            "• Estudo dos conteúdos prioritários.\n"
            "• Exercícios após cada assunto.\n\n"

            f"DIA {dias_teoria + 1}\n"
            "• Revisão dos assuntos estudados.\n\n"

            f"DIA {dias - 1}\n"
            "• Simulado ou prova anterior.\n"
            "• Correção dos erros.\n\n"

            f"DIA {dias}\n"
            "• Revisão leve.\n"
            "• Descanso."
        )


    if dias <= 14:

        fase_aprendizado = dias - 5

        return (
            f"CRONOGRAMA DE PREPARAÇÃO - {dias} DIAS\n\n"

            f"Tempo diário: {tempo_diario}\n\n"

            f"DIAS 1 A {fase_aprendizado}\n"
            "FASE 1 - APRENDIZADO\n"
            "• Divida todo o conteúdo entre esses dias.\n"
            "• Estude teoria e faça exercícios diariamente.\n\n"

            f"DIAS {fase_aprendizado + 1} E {fase_aprendizado + 2}\n"
            "FASE 2 - REVISÃO\n"
            "• Revise todos os assuntos.\n"
            "• Priorize os conteúdos difíceis.\n\n"

            f"DIAS {dias - 2} E {dias - 1}\n"
            "FASE 3 - SIMULADOS\n"
            "• Resolva provas anteriores.\n"
            "• Corrija os erros.\n\n"

            f"DIA {dias}\n"
            "FASE 4 - REVISÃO FINAL\n"
            "• Faça revisão leve."
        )


    fase_aprendizado = dias - 7

    texto = (
        f"CRONOGRAMA COMPLETO DE {dias} DIAS\n\n"

        f"Tempo diário recomendado: {tempo_diario}\n\n"

        f"DIAS 1 A {fase_aprendizado}\n"
        "FASE 1 - APRENDIZADO\n"
        "• Divida o conteúdo pelos dias disponíveis.\n"
        "• Estude 1 ou 2 assuntos por dia.\n"
        "• Faça exercícios após cada conteúdo.\n"
        "• Faça revisão curta a cada 3 dias.\n\n"

        f"DIAS {fase_aprendizado + 1} A {dias - 4}\n"
        "FASE 2 - REVISÃO GERAL\n"
        "• Revise todos os conteúdos.\n"
        "• Faça mapas mentais ou resumos.\n"
        "• Priorize temas mais difíceis.\n\n"

        f"DIAS {dias - 3} E {dias - 2}\n"
        "FASE 3 - SIMULADOS\n"
        "• Resolva provas anteriores.\n"
        "• Simule o tempo real da prova.\n"
        "• Corrija todos os erros.\n\n"

        f"DIA {dias - 1}\n"
        "FASE 4 - CORREÇÃO DE ERROS\n"
        "• Revise apenas os assuntos que ainda apresentam dificuldade.\n\n"

        f"DIA {dias}\n"
        "FASE 5 - VÉSPERA\n"
        "• Revisão leve.\n"
        "• Leia resumos.\n"
        "• Organize o material.\n"
        "• Durma adequadamente."
    )


    if atrasado:

        texto += (
            "\n\nAJUSTE - CONTEÚDO ATRASADO\n"
            "• Use os primeiros dias para recuperar os conteúdos mais importantes."
        )


    if materia_pratica:

        texto += (
            "\n\nAJUSTE - MATÉRIA PRÁTICA\n"
            "• Reserve pelo menos metade do tempo diário para exercícios."
        )


    if dificuldade == "alta":

        texto += (
            "\n\nAJUSTE - ALTA DIFICULDADE\n"
            "• Faça revisões mais frequentes.\n"
            "• Evite muitos assuntos diferentes no mesmo dia."
        )


    if concentracao:

        texto += (
            "\n\nAJUSTE - CONCENTRAÇÃO\n"
            "• Use ciclos de 25 minutos de estudo e 5 minutos de pausa."
        )


    if cansado:

        texto += (
            "\n\nAJUSTE - CANSAÇO\n"
            "• Reduza sessões muito longas.\n"
            "• Priorize sono e pausas."
        )


    return texto


# ============================================================
# CALCULAR URGENCIA
# ============================================================

def calcular_urgencia():

    if prova_var.get() == "Nao":

        return {
            "urgencia": "sem prova proxima",
            "dias": None,
            "texto": "Nenhuma prova próxima informada."
        }


    try:

        dia = int(dia_var.get())
        mes = int(mes_var.get())
        ano = int(ano_var.get())

        data_prova = date(
            ano,
            mes,
            dia
        )

        hoje = date.today()

        dias = (
            data_prova - hoje
        ).days


    except ValueError:

        messagebox.showerror(
            "Data inválida",
            "Selecione uma data válida para a prova."
        )

        return None


    if dias < 0:

        messagebox.showerror(
            "Data inválida",
            "A data da prova não pode estar no passado."
        )

        return None


    if dias == 0:

        return {
            "urgencia": "super urgente",
            "dias": dias,
            "texto": "SUPER URGENTE - A prova é HOJE!"
        }


    elif dias == 1:

        return {
            "urgencia": "muito urgente",
            "dias": dias,
            "texto": "MUITO URGENTE - A prova é AMANHÃ!"
        }


    elif dias <= 3:

        return {
            "urgencia": "urgente",
            "dias": dias,
            "texto": f"URGENTE - Faltam apenas {dias} dias."
        }


    elif dias <= 7:

        return {
            "urgencia": "alta prioridade",
            "dias": dias,
            "texto": f"ALTA PRIORIDADE - Faltam {dias} dias."
        }


    elif dias <= 14:

        return {
            "urgencia": "atencao",
            "dias": dias,
            "texto": f"ATENÇÃO - Faltam {dias} dias."
        }


    else:

        return {
            "urgencia": "planejamento",
            "dias": dias,
            "texto": f"PLANEJAMENTO - Faltam {dias} dias."
        }


# ============================================================
# MOTOR DE INFERENCIA
# ============================================================

def tomar_decisao():

    if (
        tempo_var.get() == ""
        or dificuldade_var.get() == ""
    ):

        messagebox.showwarning(
            "Campos incompletos",
            "Preencha todas as informações antes de tomar a decisão."
        )

        return


    dados_urgencia = calcular_urgencia()


    if dados_urgencia is None:
        return


    fatos = {

        "tempo":
            tempo_var.get(),

        "dificuldade":
            dificuldade_var.get(),

        "prova_proxima":
            prova_var.get() == "Sim",

        "cansado":
            cansado_var.get() == "Sim",

        "materia_pratica":
            pratica_var.get() == "Sim",

        "conteudo_atrasado":
            atrasado_var.get() == "Sim",

        "dificuldade_concentracao":
            concentracao_var.get() == "Sim",

        "urgencia":
            dados_urgencia["urgencia"]
    }


    melhor_regra = None
    melhor_pontuacao = -1
    numero_regra = 0


    for indice, regra in enumerate(
        regras,
        start=1
    ):

        compativel = True
        pontuacao = 0


        for fato, valor_esperado in regra["condicoes"].items():

            if fatos[fato] == valor_esperado:

                pontuacao += 1

            else:

                compativel = False
                break


        if (
            compativel
            and pontuacao > melhor_pontuacao
        ):

            melhor_regra = regra
            melhor_pontuacao = pontuacao
            numero_regra = indice


    cronograma = gerar_cronograma(
        dados_urgencia
    )


    mostrar_resultado(
        melhor_regra,
        melhor_pontuacao,
        numero_regra,
        dados_urgencia,
        cronograma
    )


# ============================================================
# MOSTRAR RESULTADO
# ============================================================

def mostrar_resultado(
    regra,
    pontuacao,
    numero,
    dados_urgencia,
    cronograma
):

    decisao_label.config(
        text=regra["decisao"]
    )


    explicacao_label.config(
        text=regra["explicacao"]
    )


    regra_label.config(
        text=(
            f"Regra utilizada: {numero}"
            f"   •   Condições atendidas: {pontuacao}"
        )
    )


    urgencia = dados_urgencia["urgencia"]


    if urgencia in [
        "super urgente",
        "muito urgente"
    ]:

        frame_urgencia.config(
            bg=COR_VERMELHO
        )

        urgencia_label.config(
            bg=COR_VERMELHO,
            fg="#B42318"
        )


    elif urgencia in [
        "urgente",
        "alta prioridade"
    ]:

        frame_urgencia.config(
            bg=COR_AMARELO
        )

        urgencia_label.config(
            bg=COR_AMARELO,
            fg="#B54708"
        )


    else:

        frame_urgencia.config(
            bg=COR_VERDE
        )

        urgencia_label.config(
            bg=COR_VERDE,
            fg="#027A48"
        )


    urgencia_label.config(
        text=dados_urgencia["texto"]
    )


    # CRONOGRAMA

    cronograma_texto.config(
        state="normal"
    )

    cronograma_texto.delete(
        "1.0",
        tk.END
    )

    cronograma_texto.insert(
        "1.0",
        cronograma
    )

    cronograma_texto.config(
        state="disabled"
    )


    # PLANO

    plano_texto.config(
        state="normal"
    )

    plano_texto.delete(
        "1.0",
        tk.END
    )

    plano_texto.insert(
        "1.0",
        regra["plano"]
    )

    plano_texto.config(
        state="disabled"
    )


# ============================================================
# MOSTRAR DATA
# ============================================================

def atualizar_campo_data(event=None):

    if prova_var.get() == "Sim":

        frame_data.pack(
            fill="x",
            pady=(8, 5)
        )

    else:

        frame_data.pack_forget()


# ============================================================
# LIMPAR
# ============================================================

def limpar():

    tempo_var.set("")
    dificuldade_var.set("")

    prova_var.set("Nao")
    cansado_var.set("Nao")
    pratica_var.set("Nao")
    atrasado_var.set("Nao")
    concentracao_var.set("Nao")


    hoje = date.today()

    dia_var.set(
        str(hoje.day)
    )

    mes_var.set(
        str(hoje.month)
    )

    ano_var.set(
        str(hoje.year)
    )


    frame_data.pack_forget()


    decisao_label.config(
        text="Aguardando tomada de decisão..."
    )


    explicacao_label.config(
        text="Preencha as informações e clique em TOMAR DECISÃO."
    )


    regra_label.config(
        text="Nenhuma regra selecionada"
    )


    frame_urgencia.config(
        bg=COR_AZUL_CLARO
    )


    urgencia_label.config(
        text="Urgência da prova será calculada aqui.",
        bg=COR_AZUL_CLARO,
        fg=COR_TEXTO_SECUNDARIO
    )


    cronograma_texto.config(
        state="normal"
    )

    cronograma_texto.delete(
        "1.0",
        tk.END
    )

    cronograma_texto.insert(
        "1.0",
        "O cronograma personalizado será mostrado aqui."
    )

    cronograma_texto.config(
        state="disabled"
    )


    plano_texto.config(
        state="normal"
    )

    plano_texto.delete(
        "1.0",
        tk.END
    )

    plano_texto.insert(
        "1.0",
        "O plano de ação recomendado será mostrado aqui."
    )

    plano_texto.config(
        state="disabled"
    )


# ============================================================
# JANELA
# ============================================================

janela = tk.Tk()

janela.title(
    "StudyAI - Sistema Especialista"
)

janela.geometry(
    "1280x900"
)

janela.minsize(
    1050,
    750
)

janela.configure(
    bg=COR_FUNDO
)


# ============================================================
# ESTILO
# ============================================================

estilo = ttk.Style()

estilo.theme_use(
    "clam"
)

estilo.configure(
    "TCombobox",
    padding=6,
    font=("Segoe UI", 10)
)


# ============================================================
# CABECALHO
# ============================================================

cabecalho = tk.Frame(
    janela,
    bg=COR_AZUL,
    height=100
)

cabecalho.pack(
    fill="x"
)

cabecalho.pack_propagate(
    False
)


tk.Label(
    cabecalho,
    text="StudyAI",
    font=("Segoe UI", 26, "bold"),
    bg=COR_AZUL,
    fg="white"
).pack(
    anchor="w",
    padx=40,
    pady=(17, 0)
)


tk.Label(
    cabecalho,
    text="Sistema Especialista para Tomada de Decisões em Estratégias de Estudo",
    font=("Segoe UI", 11),
    bg=COR_AZUL,
    fg="#DCE6F8"
).pack(
    anchor="w",
    padx=42
)


# ============================================================
# CONTEUDO
# ============================================================

conteudo = tk.Frame(
    janela,
    bg=COR_FUNDO
)

conteudo.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=20
)

conteudo.grid_columnconfigure(
    0,
    weight=1
)

conteudo.grid_columnconfigure(
    1,
    weight=1
)

conteudo.grid_rowconfigure(
    0,
    weight=1
)


# ============================================================
# CARD ESQUERDO
# ============================================================

card_formulario = tk.Frame(
    conteudo,
    bg=COR_CARD,
    highlightthickness=1,
    highlightbackground=COR_BORDA
)

card_formulario.grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=(0, 12)
)

card_formulario.grid_rowconfigure(
    1,
    weight=1
)

card_formulario.grid_columnconfigure(
    0,
    weight=1
)


# ============================================================
# TITULO FORMULARIO
# ============================================================

topo_formulario = tk.Frame(
    card_formulario,
    bg=COR_CARD
)

topo_formulario.grid(
    row=0,
    column=0,
    sticky="ew"
)


tk.Label(
    topo_formulario,
    text="Sua situação",
    font=("Segoe UI", 18, "bold"),
    bg=COR_CARD,
    fg=COR_AZUL
).pack(
    anchor="w",
    padx=30,
    pady=(18, 4)
)


tk.Label(
    topo_formulario,
    text="Informe sua situação para a IA montar a melhor estratégia.",
    font=("Segoe UI", 10),
    bg=COR_CARD,
    fg=COR_TEXTO_SECUNDARIO
).pack(
    anchor="w",
    padx=30,
    pady=(0, 10)
)


# ============================================================
# VARIAVEIS
# ============================================================

tempo_var = tk.StringVar()
dificuldade_var = tk.StringVar()

prova_var = tk.StringVar(
    value="Nao"
)

cansado_var = tk.StringVar(
    value="Nao"
)

pratica_var = tk.StringVar(
    value="Nao"
)

atrasado_var = tk.StringVar(
    value="Nao"
)

concentracao_var = tk.StringVar(
    value="Nao"
)


hoje = date.today()

dia_var = tk.StringVar(
    value=str(hoje.day)
)

mes_var = tk.StringVar(
    value=str(hoje.month)
)

ano_var = tk.StringVar(
    value=str(hoje.year)
)


# ============================================================
# AREA ROLAVEL FORMULARIO
# ============================================================

area_scroll = tk.Frame(
    card_formulario,
    bg=COR_CARD
)

area_scroll.grid(
    row=1,
    column=0,
    sticky="nsew"
)

area_scroll.grid_rowconfigure(
    0,
    weight=1
)

area_scroll.grid_columnconfigure(
    0,
    weight=1
)


canvas_form = tk.Canvas(
    area_scroll,
    bg=COR_CARD,
    highlightthickness=0
)

canvas_form.grid(
    row=0,
    column=0,
    sticky="nsew"
)


scroll_form = ttk.Scrollbar(
    area_scroll,
    orient="vertical",
    command=canvas_form.yview
)

scroll_form.grid(
    row=0,
    column=1,
    sticky="ns"
)


canvas_form.configure(
    yscrollcommand=scroll_form.set
)


formulario = tk.Frame(
    canvas_form,
    bg=COR_CARD
)


janela_form = canvas_form.create_window(
    (0, 0),
    window=formulario,
    anchor="nw"
)


def ajustar_scroll(event):

    canvas_form.configure(
        scrollregion=canvas_form.bbox("all")
    )


def ajustar_largura(event):

    canvas_form.itemconfigure(
        janela_form,
        width=event.width
    )


formulario.bind(
    "<Configure>",
    ajustar_scroll
)

canvas_form.bind(
    "<Configure>",
    ajustar_largura
)


# ============================================================
# CRIAR CAMPO
# ============================================================

def adicionar_campo(
    titulo,
    variavel,
    valores
):

    bloco = tk.Frame(
        formulario,
        bg=COR_CARD
    )

    bloco.pack(
        fill="x",
        padx=30,
        pady=4
    )


    tk.Label(
        bloco,
        text=titulo,
        font=("Segoe UI", 10, "bold"),
        bg=COR_CARD,
        fg="#344054"
    ).pack(
        anchor="w",
        pady=(0, 3)
    )


    combo = ttk.Combobox(
        bloco,
        textvariable=variavel,
        values=valores,
        state="readonly"
    )

    combo.pack(
        fill="x"
    )


    return combo


# ============================================================
# CAMPOS
# ============================================================

adicionar_campo(
    "Quanto tempo você possui para estudar por dia?",
    tempo_var,
    [
        "curto",
        "medio",
        "longo"
    ]
)


adicionar_campo(
    "Qual a dificuldade da matéria?",
    dificuldade_var,
    [
        "baixa",
        "media",
        "alta"
    ]
)


# ============================================================
# PROVA
# ============================================================

bloco_prova = tk.Frame(
    formulario,
    bg=COR_CARD
)

bloco_prova.pack(
    fill="x",
    padx=30,
    pady=4
)


tk.Label(
    bloco_prova,
    text="A prova está próxima?",
    font=("Segoe UI", 10, "bold"),
    bg=COR_CARD,
    fg="#344054"
).pack(
    anchor="w",
    pady=(0, 3)
)


combo_prova = ttk.Combobox(
    bloco_prova,
    textvariable=prova_var,
    values=[
        "Sim",
        "Nao"
    ],
    state="readonly"
)

combo_prova.pack(
    fill="x"
)


combo_prova.bind(
    "<<ComboboxSelected>>",
    atualizar_campo_data
)


# ============================================================
# DATA
# ============================================================

frame_data = tk.Frame(
    bloco_prova,
    bg="#F8FAFC",
    padx=12,
    pady=10
)


tk.Label(
    frame_data,
    text="Selecione a data da prova:",
    font=("Segoe UI", 10, "bold"),
    bg="#F8FAFC",
    fg="#344054"
).pack(
    anchor="w",
    pady=(0, 7)
)


linha_data = tk.Frame(
    frame_data,
    bg="#F8FAFC"
)

linha_data.pack(
    fill="x"
)


# DIA

frame_dia = tk.Frame(
    linha_data,
    bg="#F8FAFC"
)

frame_dia.pack(
    side="left",
    expand=True,
    fill="x",
    padx=(0, 5)
)


tk.Label(
    frame_dia,
    text="Dia",
    bg="#F8FAFC",
    fg=COR_TEXTO_SECUNDARIO
).pack(
    anchor="w"
)


ttk.Combobox(
    frame_dia,
    textvariable=dia_var,
    values=[
        str(i)
        for i in range(1, 32)
    ],
    state="readonly"
).pack(
    fill="x"
)


# MES

frame_mes = tk.Frame(
    linha_data,
    bg="#F8FAFC"
)

frame_mes.pack(
    side="left",
    expand=True,
    fill="x",
    padx=5
)


tk.Label(
    frame_mes,
    text="Mês",
    bg="#F8FAFC",
    fg=COR_TEXTO_SECUNDARIO
).pack(
    anchor="w"
)


ttk.Combobox(
    frame_mes,
    textvariable=mes_var,
    values=[
        str(i)
        for i in range(1, 13)
    ],
    state="readonly"
).pack(
    fill="x"
)


# ANO

frame_ano = tk.Frame(
    linha_data,
    bg="#F8FAFC"
)

frame_ano.pack(
    side="left",
    expand=True,
    fill="x",
    padx=(5, 0)
)


tk.Label(
    frame_ano,
    text="Ano",
    bg="#F8FAFC",
    fg=COR_TEXTO_SECUNDARIO
).pack(
    anchor="w"
)


ttk.Combobox(
    frame_ano,
    textvariable=ano_var,
    values=[
        str(hoje.year + i)
        for i in range(0, 6)
    ],
    state="readonly"
).pack(
    fill="x"
)


frame_data.pack_forget()


# ============================================================
# OUTRAS PERGUNTAS
# ============================================================

adicionar_campo(
    "Você está cansado?",
    cansado_var,
    [
        "Sim",
        "Nao"
    ]
)


adicionar_campo(
    "A matéria possui exercícios práticos?",
    pratica_var,
    [
        "Sim",
        "Nao"
    ]
)


adicionar_campo(
    "Existe conteúdo atrasado?",
    atrasado_var,
    [
        "Sim",
        "Nao"
    ]
)


adicionar_campo(
    "Você está com dificuldade de concentração?",
    concentracao_var,
    [
        "Sim",
        "Nao"
    ]
)


# ============================================================
# BOTOES FIXOS
# ============================================================

rodape_formulario = tk.Frame(
    card_formulario,
    bg=COR_CARD
)

rodape_formulario.grid(
    row=2,
    column=0,
    sticky="ew"
)


tk.Frame(
    rodape_formulario,
    bg="#E4E7EC",
    height=1
).pack(
    fill="x"
)


frame_botoes = tk.Frame(
    rodape_formulario,
    bg=COR_CARD
)

frame_botoes.pack(
    fill="x",
    padx=30,
    pady=15
)


botao_decisao = tk.Button(
    frame_botoes,
    text="TOMAR DECISÃO",
    command=tomar_decisao,
    font=("Segoe UI", 11, "bold"),
    bg=COR_BOTAO,
    fg="white",
    activebackground=COR_BOTAO_HOVER,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=12
)

botao_decisao.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 8)
)


botao_limpar = tk.Button(
    frame_botoes,
    text="LIMPAR",
    command=limpar,
    font=("Segoe UI", 10, "bold"),
    bg="#EDF1F7",
    fg="#344054",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=12
)

botao_limpar.pack(
    side="left",
    padx=(8, 0)
)


# ============================================================
# CARD DIREITO
# ============================================================

card_resultado = tk.Frame(
    conteudo,
    bg=COR_CARD,
    highlightthickness=1,
    highlightbackground=COR_BORDA
)

card_resultado.grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=(12, 0)
)


# ============================================================
# SCROLL RESULTADO
# ============================================================

canvas_resultado = tk.Canvas(
    card_resultado,
    bg=COR_CARD,
    highlightthickness=0
)

canvas_resultado.pack(
    side="left",
    fill="both",
    expand=True
)


scroll_resultado = ttk.Scrollbar(
    card_resultado,
    orient="vertical",
    command=canvas_resultado.yview
)

scroll_resultado.pack(
    side="right",
    fill="y"
)


canvas_resultado.configure(
    yscrollcommand=scroll_resultado.set
)


resultado_interno = tk.Frame(
    canvas_resultado,
    bg=COR_CARD
)


janela_resultado = canvas_resultado.create_window(
    (0, 0),
    window=resultado_interno,
    anchor="nw"
)


def atualizar_scroll_resultado(event):

    canvas_resultado.configure(
        scrollregion=canvas_resultado.bbox("all")
    )


def ajustar_resultado(event):

    canvas_resultado.itemconfigure(
        janela_resultado,
        width=event.width
    )


resultado_interno.bind(
    "<Configure>",
    atualizar_scroll_resultado
)

canvas_resultado.bind(
    "<Configure>",
    ajustar_resultado
)


# ============================================================
# TITULO
# ============================================================

tk.Label(
    resultado_interno,
    text="Tomada de decisão da IA",
    font=("Segoe UI", 18, "bold"),
    bg=COR_CARD,
    fg=COR_AZUL
).pack(
    anchor="w",
    padx=30,
    pady=(20, 5)
)


regra_label = tk.Label(
    resultado_interno,
    text="Nenhuma regra selecionada",
    font=("Segoe UI", 9),
    bg=COR_CARD,
    fg="#7B879A"
)

regra_label.pack(
    anchor="w",
    padx=30
)


# ============================================================
# URGENCIA
# ============================================================

frame_urgencia = tk.Frame(
    resultado_interno,
    bg=COR_AZUL_CLARO
)

frame_urgencia.pack(
    fill="x",
    padx=30,
    pady=(15, 5)
)


urgencia_label = tk.Label(
    frame_urgencia,
    text="Urgência da prova será calculada aqui.",
    font=("Segoe UI", 10, "bold"),
    bg=COR_AZUL_CLARO,
    fg=COR_TEXTO_SECUNDARIO
)

urgencia_label.pack(
    anchor="w",
    padx=15,
    pady=10
)


# ============================================================
# DECISAO
# ============================================================

frame_decisao = tk.Frame(
    resultado_interno,
    bg=COR_AZUL_CLARO
)

frame_decisao.pack(
    fill="x",
    padx=30,
    pady=8
)


tk.Label(
    frame_decisao,
    text="DECISÃO DA IA",
    font=("Segoe UI", 9, "bold"),
    bg=COR_AZUL_CLARO,
    fg=COR_BOTAO
).pack(
    anchor="w",
    padx=20,
    pady=(15, 5)
)


decisao_label = tk.Label(
    frame_decisao,
    text="Aguardando tomada de decisão...",
    font=("Segoe UI", 14, "bold"),
    bg=COR_AZUL_CLARO,
    fg=COR_TEXTO,
    wraplength=500,
    justify="left"
)

decisao_label.pack(
    anchor="w",
    padx=20,
    pady=(0, 18)
)


# ============================================================
# CRONOGRAMA - AGORA LOGO ABAIXO DA DECISAO
# ============================================================

tk.Label(
    resultado_interno,
    text="Cronograma recomendado",
    font=("Segoe UI", 12, "bold"),
    bg=COR_CARD,
    fg="#344054"
).pack(
    anchor="w",
    padx=30,
    pady=(12, 8)
)


cronograma_texto = tk.Text(
    resultado_interno,
    height=18,
    font=("Segoe UI", 10),
    bg="#F8FAFC",
    fg="#344054",
    bd=0,
    padx=15,
    pady=15,
    wrap="word"
)

cronograma_texto.pack(
    fill="x",
    padx=30,
    pady=(0, 20)
)


cronograma_texto.insert(
    "1.0",
    "O cronograma personalizado será mostrado aqui."
)

cronograma_texto.config(
    state="disabled"
)


# ============================================================
# EXPLICACAO
# ============================================================

tk.Label(
    resultado_interno,
    text="Por que a IA tomou essa decisão?",
    font=("Segoe UI", 12, "bold"),
    bg=COR_CARD,
    fg="#344054"
).pack(
    anchor="w",
    padx=30,
    pady=(5, 5)
)


explicacao_label = tk.Label(
    resultado_interno,
    text="Preencha as informações e clique em TOMAR DECISÃO.",
    font=("Segoe UI", 10),
    bg=COR_CARD,
    fg=COR_TEXTO_SECUNDARIO,
    wraplength=500,
    justify="left"
)

explicacao_label.pack(
    anchor="w",
    padx=30,
    pady=(0, 15)
)


# ============================================================
# PLANO
# ============================================================

tk.Label(
    resultado_interno,
    text="Plano de ação recomendado",
    font=("Segoe UI", 12, "bold"),
    bg=COR_CARD,
    fg="#344054"
).pack(
    anchor="w",
    padx=30,
    pady=(5, 8)
)


plano_texto = tk.Text(
    resultado_interno,
    height=8,
    font=("Segoe UI", 10),
    bg="#F8FAFC",
    fg="#344054",
    bd=0,
    padx=15,
    pady=15,
    wrap="word"
)

plano_texto.pack(
    fill="x",
    padx=30,
    pady=(0, 30)
)


plano_texto.insert(
    "1.0",
    "O plano de ação recomendado será mostrado aqui."
)

plano_texto.config(
    state="disabled"
)


# ============================================================
# RODAPE
# ============================================================

rodape = tk.Label(
    janela,
    text="StudyAI • Sistema Especialista baseado em regras e motor de inferência",
    font=("Segoe UI", 9),
    bg=COR_FUNDO,
    fg="#98A2B3"
)

rodape.pack(
    pady=(0, 10)
)


# ============================================================
# EXECUTAR
# ============================================================

janela.mainloop()