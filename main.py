from analise_energia import calcular_cenario, mostrar_analise


def responder_pergunta(pergunta):
    texto = pergunta.lower()
    r = calcular_cenario()

    if "led" in texto or "lampada" in texto or "lâmpada" in texto:
        print(
            f"\nA troca da lâmpada comum por LED reduz o consumo estimado "
            f"em {r['economia_led_kwh']:.2f} kWh por mês."
        )
        print(
            f"Na tarifa usada no estudo, isso representa aproximadamente "
            f"R$ {r['economia_led_reais']:.2f} por mês."
        )
        print("Limitação: o resultado depende das horas reais de uso.")

    elif "solar" in texto or "painel" in texto:
        print(
            f"\nUm painel de 100 W teria geração estimada de "
            f"{r['geracao_solar']:.2f} kWh por mês no cenário estudado."
        )
        print(
            f"Isso cobriria cerca de {r['cobertura_solar']:.1f}% do consumo analisado."
        )
        print(
            "Limitação: a geração varia com localização, clima, sombreamento "
            "e características do sistema."
        )

    elif "consumo" in texto or "energia" in texto or "custo" in texto:
        print(
            f"\nO consumo mensal estimado do espaço de estudo é "
            f"{r['consumo_atual']:.2f} kWh."
        )
        print(
            f"Com a tarifa didática de R$ 1,00/kWh, o custo estimado é "
            f"R$ {r['custo_atual']:.2f} por mês."
        )

    else:
        print(
            "\nNão encontrei uma orientação específica. "
            "Tente perguntar sobre consumo, lâmpada LED ou energia solar."
        )

    print(
        "Aviso: as estimativas não são valores garantidos e podem variar "
        "conforme o uso e as condições locais."
    )


def menu():
    while True:
        print("\n" + "=" * 48)
        print("CITIZEN ASSIST AI - ENERGIA E SUSTENTABILIDADE")
        print("=" * 48)
        print("1 - Ver análise de consumo e alternativas")
        print("2 - Fazer uma pergunta sobre energia")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrar_analise()

        elif opcao == "2":
            pergunta = input(
                "Digite sua dúvida sobre consumo, LED ou energia solar: "
            ).strip()

            if pergunta:
                responder_pergunta(pergunta)
            else:
                print("A pergunta não pode ficar vazia.")

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
