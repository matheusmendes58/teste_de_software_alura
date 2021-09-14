from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self): # método do unittest para criação de cenarios ou seja cada função abaixo sera invocado automaticamente esta função antes
        # criando usuarios

        self.gui = Usuario('Gui', 500.0)
        self.yuri = Usuario('Yuri', 500.0)

        # lances

        self.lance_do_yuri = Lance(self.yuri, 100.0)
        self.lance_do_gui = Lance(self.gui, 150.0)

        # Leilão

        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionado_em_ordem_crescente(self):
        # dando um lance
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrecente(self):
        with self.assertRaises(ValueError):
            yuri = Usuario('Yuri', 500.0)
            lance_do_yuri = Lance(yuri, 100.0)
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        vini = Usuario('Vini', 500.0)

        # lances

        lance_do_vini = Lance(vini, 200.0)


        # dando um lance
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lance_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lance_recebido)


    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_youri = Lance(yuri, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_youri)

        quantidade_de_lance_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lance_recebido)


    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200.0)
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)
