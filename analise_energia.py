def consumo_mensal(potencia_w, horas_dia, dias_mes=30):
    return (potencia_w * horas_dia * dias_mes) / 1000


def calcular_cenario():
    horas_dia = 5
    dias_mes = 30
    tarifa_estimada = 1.00

    notebook_w = 65
    lampada_comum_w = 60
    ventilador_w = 60
    lampada_led_w = 9

    consumo_notebook = consumo_mensal(notebook_w, horas_dia, dias_mes)
    consumo_lampada = consumo_mensal(lampada_comum_w, horas_dia, dias_mes)
    consumo_ventilador = consumo_mensal(ventilador_w, horas_dia, dias_mes)

    consumo_atual = consumo_notebook + consumo_lampada + consumo_ventilador
    custo_atual = consumo_atual * tarifa_estimada

    consumo_led = (
        consumo_notebook
        + consumo_mensal(lampada_led_w, horas_dia, dias_mes)
        + consumo_ventilador
    )

    economia_led_kwh = consumo_atual - consumo_led
    economia_led_reais = economia_led_kwh * tarifa_estimada

    painel_w = 100
    horas_sol_pico = 4.5
    rendimento = 0.80

    geracao_solar = (
        painel_w * horas_sol_pico * rendimento * dias_mes / 1000
    )

    cobertura_solar = (geracao_solar / consumo_atual) * 100
    consumo_rede_solar = max(consumo_atual - geracao_solar, 0)
    economia_solar_reais = geracao_solar * tarifa_estimada

    return {
        "consumo_atual": consumo_atual,
        "custo_atual": custo_atual,
        "consumo_led": consumo_led,
        "economia_led_kwh": economia_led_kwh,
        "economia_led_reais": economia_led_reais,
        "geracao_solar": geracao_solar,
        "cobertura_solar": cobertura_solar,
        "consumo_rede_solar": consumo_rede_solar,
        "economia_solar_reais": economia_solar_reais,
    }


def mostrar_analise():
    r = calcular_cenario()

    print("\nANÁLISE DE ENERGIA")
    print("-" * 45)
    print(f"Consumo atual estimado: {r['consumo_atual']:.2f} kWh/mês")
    print(f"Custo atual estimado: R$ {r['custo_atual']:.2f}/mês")

    print("\nALTERNATIVA 1 - LÂMPADA LED")
    print(f"Novo consumo: {r['consumo_led']:.2f} kWh/mês")
    print(f"Economia: {r['economia_led_kwh']:.2f} kWh/mês")
    print(f"Economia estimada: R$ {r['economia_led_reais']:.2f}/mês")
    print("Vantagem: baixo investimento e redução imediata do consumo.")
    print("Limitação: a economia depende do tempo real de uso.")

    print("\nALTERNATIVA 2 - ENERGIA SOLAR")
    print(f"Geração estimada: {r['geracao_solar']:.2f} kWh/mês")
    print(f"Cobertura do consumo: {r['cobertura_solar']:.1f}%")
    print(f"Consumo restante da rede: {r['consumo_rede_solar']:.2f} kWh/mês")
    print(f"Economia estimada: R$ {r['economia_solar_reais']:.2f}/mês")
    print("Vantagem: usa fonte renovável e reduz o consumo da rede.")
    print("Limitação: exige investimento maior e depende da incidência solar.")

    print("\nRECOMENDAÇÃO")
    print(
        "Para começar com pouco investimento, a troca por LED é a opção mais simples. "
        "A energia solar reduz mais o uso da rede no cenário estudado, mas exige maior "
        "investimento inicial."
    )

    print("\nAVISO")
    print(
        "Os valores são estimativas didáticas. Tarifa, potência real dos equipamentos, "
        "horas de uso e geração solar podem variar."
    )
