from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCpnj(documento)
        else:
            raise ValueError("Quantidade de digitos está incorreta")

class DocCpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido")

    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCpnj:

    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CPNJ Inválido")
        
    def __str__(self) -> str:
        return self.mask_cnpj()
    
    def valida(self, documento):
        validar_o_cpnj = CNPJ()
        return validar_o_cpnj.validate(documento)
    
    def format(self):
        texto_cpnj = CNPJ()
        return texto_cpnj.mask(self.cnpj)
