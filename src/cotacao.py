import urllib.request
import json

def buscar_cotacao_dolar() -> float | None:
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read())
            return float(data["USDBRL"]["bid"])
    except Exception:
        return None
