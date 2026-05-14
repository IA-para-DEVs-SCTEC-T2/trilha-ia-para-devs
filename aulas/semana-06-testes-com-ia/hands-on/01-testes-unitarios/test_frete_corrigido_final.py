import pytest
from frete import calcular_frete


class TestCalcularFrete:
    """Testes unitários para calcular_frete"""
    
    # ========== CENÁRIOS POSITIVOS ==========
    
    def test_frete_gratis_compra_200_ou_mais(self):
        """Frete grátis para compras de R$ 200 ou mais"""
        assert calcular_frete(200, 5) == 0
        assert calcular_frete(300, 15) == 0
        assert calcular_frete(500, 100) == 0
    
    def test_frete_10_reais_compra_abaixo_200_distancia_ate_10(self):
        """R$ 10 para compras abaixo de R$ 200 e distância até 10 km"""
        assert calcular_frete(199.99, 5) == 10
        assert calcular_frete(150, 10) == 10
        assert calcular_frete(0, 0) == 10
    
    def test_frete_20_reais_compra_abaixo_200_distancia_acima_10(self):
        """R$ 20 para compras abaixo de R$ 200 e distância acima de 10 km"""
        assert calcular_frete(199.99, 10.01) == 20
        assert calcular_frete(150, 15) == 20
        assert calcular_frete(0, 100) == 20
    
    # ========== EDGE CASES ==========
    
    def test_edge_case_limite_compra_200(self):
        """Edge case: compra exatamente R$ 200"""
        assert calcular_frete(200, 0) == 0
        assert calcular_frete(200, 10) == 0
        assert calcular_frete(200, 10.01) == 0
    
    def test_edge_case_limite_distancia_10(self):
        """Edge case: distância exatamente 10 km"""
        assert calcular_frete(199.99, 10) == 10
        assert calcular_frete(200, 10) == 0
        assert calcular_frete(150, 10) == 10
    
    def test_edge_case_valores_decimais(self):
        """Edge case: valores decimais"""
        assert calcular_frete(199.99, 9.99) == 10
        assert calcular_frete(199.99, 10.01) == 20
        assert calcular_frete(200.01, 5.5) == 0
    
    # ========== ENTRADAS INVÁLIDAS ==========
    
    def test_entrada_invalida_tipos_nao_numericos(self):
        """Entrada inválida: tipos não numéricos"""
        with pytest.raises(TypeError, match="valor_compra deve ser numérico"):
            calcular_frete("100", 10)
        with pytest.raises(TypeError, match="distancia_km deve ser numérico"):
            calcular_frete(100, "10")
        with pytest.raises(TypeError):
            calcular_frete(None, 10)
        with pytest.raises(TypeError):
            calcular_frete(100, None)
    
    def test_entrada_invalida_valores_negativos(self):
        """Entrada inválida: valores negativos"""
        with pytest.raises(ValueError, match="Valores inválidos"):
            calcular_frete(-100, 10)
        with pytest.raises(ValueError, match="Valores inválidos"):
            calcular_frete(100, -10)
        with pytest.raises(ValueError, match="Valores inválidos"):
            calcular_frete(-100, -10)
    
    def test_entrada_invalida_tipos_compostos(self):
        """Entrada inválida: listas e dicionários"""
        with pytest.raises(TypeError):
            calcular_frete([100], 10)
        with pytest.raises(TypeError):
            calcular_frete(100, [10])
        with pytest.raises(TypeError):
            calcular_frete({"valor": 100}, 10)
        with pytest.raises(TypeError):
            calcular_frete(100, {"distancia": 10})


if __name__ == "__main__":
    pytest.main([__file__, "-v"])