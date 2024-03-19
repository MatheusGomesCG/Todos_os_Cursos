from bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given-Contexto
        entrada = '13/03/2000'
        esperado = 22
        
        Funcionario_teste = Funcionario("Teste", entrada, 1111)
        