from src.main import adicionar_produto


def test_adicao_sucesso():
    """Teste de sucesso."""
    assert adicionar_produto({}, "Vela", 10) is True


def test_adicao_negativa():
    """Teste de erro com valor negativo."""
    assert adicionar_produto({}, "Vela", -5) is False


def test_estoque_vazio():
    """Teste de estado inicial."""
    estoque = {}
    assert len(estoque) == 0
  
