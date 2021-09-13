from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def setUp(self): # método do unittest para criação de cenarios ou seja cada função abaixo sera invocado automaticamente esta função antes
        # criando usuarios

        self.gui = Usuario('Gui')
        self.yuri = Usuario('Yuri')

        # lances

        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)

        # Leilão

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionado_em_ordem_crescente(self):
        # dando um lance
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)

        # avaliação do leilão

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150.0, avaliador.menor_lance)
        self.assertEqual(150.0, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        vini = Usuario('Vini')

        # lances

        lance_do_vini = Lance(vini, 200.0)

        # Leilão

        leilao = Leilao('Celular')

        # dando um lance
        leilao.propoe(self.lance_do_gui)
        leilao.propoe(self.lance_do_yuri)
        leilao.propoe(lance_do_vini)

        # avaliação do leilão

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)