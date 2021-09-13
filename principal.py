# Aqui vai ficar os testes

from dominio import Usuario, Lance, Leilao, Avaliador

# criando usuarios

gui = Usuario('Gui')
yuri = Usuario('Yuri')

# lances

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

# Leilão

leilao = Leilao('Celular')

# dando um lance
leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_yuri)

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')


# avaliação do leilão

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'o menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')