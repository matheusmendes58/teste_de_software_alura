from dominio import Usuario, Leilao
import pytest

@pytest.fixture()
def vini():
    return Usuario('Vini', 100.0)

@pytest.fixture()
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 50.0)
    assert vini.carteira == 50.0