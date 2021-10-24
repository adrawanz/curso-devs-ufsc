def imposto_renda(nro_horas, valor_h, nro_filhos):
    salario_bruto = valor_h * nro_horas
    valor_deducao = nro_filhos * 189.59
    salario_liquido = salario_bruto - valor_deducao
    
    if salario_liquido > 4664.68:
        valor_aliquota = salario_liquido * 0.275
        imposto_renda = valor_aliquota - 869.36
    else:
        if salario_liquido > 3751.06:
            valor_aliquota = salario_liquido * 0.225
            imposto_renda = valor_aliquota - 636.13
        else:
            if salario_liquido > 2826.66:
                valor_aliquota = salario_liquido * 0.15
                imposto_renda = valor_aliquota - 354.80
            else:
                if salario_liquido > 1903.98:
                    valor_aliquota = salario_liquido * 0.075
                    imposto_renda = valor_aliquota - 142.80
                else:
                    imposto_renda = 0
    return imposto_renda
                
def main():
    nro_horas = int(input())
    valor_h = float(input())
    nro_filhos = int(input())
    ir = imposto_renda(nro_horas, valor_h, nro_filhos)

    ir_formatado = "{:.2f}".format(ir)
    print(ir_formatado)

main()