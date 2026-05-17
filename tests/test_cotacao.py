from unittest.mock import patch, MagicMock
import json
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from cotacao import buscar_cotacao_dolar

def test_cotacao_retorna_valor_valido():
    mock_data = {"USDBRL": {"bid": "5.25"}}
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps(mock_data).encode()
    mock_response.__enter__ = lambda s: s
    mock_response.__exit__ = MagicMock(return_value=False)

    with patch("urllib.request.urlopen", return_value=mock_response):
        resultado = buscar_cotacao_dolar()

    assert resultado == 5.25

def test_cotacao_retorna_none_em_falha():
    with patch("urllib.request.urlopen", side_effect=Exception("timeout")):
        resultado = buscar_cotacao_dolar()

    assert resultado is None
