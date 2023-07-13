from src.phonebook import Phonebook
from unittest import TestCase

class TestPhonebook(TestCase):

   ####### add #######
    def test_add(self):
        # Setup
        name = "Beatriz"
        number = "999998888"
        resultado_esperado = 'Numero adicionado'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_add_nome_duplicado(self):
        # Setup
        name = "Beatriz"
        number = "999998888"
        resultado_esperado = 'Nome duplicado'

        phonebook = Phonebook()
        phonebook.add(name=name, number=number)

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_add_nome_invalido_cerquilha(self):
        # Setup
        name = "#"
        number = "999998888"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_add_nome_invalido_arroba(self):
        # Setup
        name = "@"
        number = "999998888"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_add_nome_invalido_exclamacao(self):
        # Setup
        name = "!"
        number = "999998888"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_add_nome_invalido_cifrao(self):
        # Setup
        name = "$"
        number = "999998888"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_add_nome_invalido_porcentagem(self):
        # Setup
        name = "%"
        number = "999998888"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_add_numero_vazio(self):
        # Setup
        name = "Amanda"
        number = ""
        resultado_esperado = 'Numero invalid'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name=name, number=number)

        # Avaliacao
        assert resultado_esperado == resultado

    ####### lookup #######
    def test_lookup(self):
        # Setup
        name = "Beatriz"
        number = "999998888"
        resultado_esperado = number
        phonebook = Phonebook()

        phonebook.add(name=name, number="999998888")
        # Chamada
        resultado = phonebook.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_lookup_nome_invalido_cerquilha(self):
        # Setup
        name = "#"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_lookup_nome_invalido_arroba(self):
        # Setup
        name = "@"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_lookup_nome_invalido_exclamacao(self):
        # Setup
        name = "!"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_lookup_nome_invalido_cifrao(self):
        # Setup
        name = "$"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado
    def test_lookup_nome_invalido_porcentagem(self):
        # Setup
        name = "%"
        resultado_esperado = 'Nome invalido'

        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name=name)

        # Avaliacao
        assert resultado_esperado == resultado

    ####### get_names #######
    def test_get_names(self):
        # Setup
        resultado_esperado = ['POLICIA','Beatriz','Amanda']

        phonebook = Phonebook()
        phonebook.add(name='Beatriz', number="999998888")
        phonebook.add(name='Amanda', number="999998888")

        # Chamada
        resultado = phonebook.get_names()

        # Avaliacao
        self.assertListEqual(resultado_esperado, resultado)

    # get_numbers #######
    def test_get_numbers(self):
        # Setup
        resultado_esperado = ['190','999998888','999998889']

        phonebook = Phonebook()
        phonebook.add(name='Beatriz', number="999998888")
        phonebook.add(name='Amanda', number="999998889")
        # Chamada
        resultado = phonebook.get_numbers()

        # Avaliacao
        #assert resultado_esperado == list(resultado)
        self.assertListEqual(resultado_esperado, resultado)

    ####### clear #######
    def test_clear(self):
        # Setup
        resultado_esperado = 'phonebook sem registros'
        phonebook = Phonebook()
        phonebook.add(name='Beatriz', number="999998888")
        phonebook.add(name='Amanda', number="999998889")

        # Chamada
        resultado = phonebook.clear()

        # Avaliacao
        assert resultado_esperado == resultado

    ####### search #######
    def test_search(self):
        # Setup
        resultado_esperado = [{'999998888','Beatriz'}]

        phonebook = Phonebook()
        phonebook.add(name='Beatriz', number="999998888")

        # Chamada
        resultado = phonebook.search('Beatriz')

        # Avaliacao
        assert resultado_esperado == resultado
        #self.assertListEqual(resultado, resultado_esperado)

    def test_search_nao_existente(self):
        # Setup
        resultado_esperado = "Usuário não encontrado"
        phonebook = Phonebook()
        phonebook.add(name='Beatriz', number="999998888")

        # Chamada
        resultado = phonebook.search('Amanda')


        # Avaliacao
        assert resultado_esperado == resultado


    ####### get_phonebook_sorted #######
    def test_phonebook_sorted(self):
        # Setup
        resultado_esperado = {'Amanda': '999998888', 'Beatriz': '999999888', 'Laura': '999998888', 'Mariane': '999998888', 'POLICIA': '190'}
        phonebook = Phonebook()
        phonebook.add(name='Mariane', number="999998888")
        phonebook.add(name='Beatriz', number="999999888")
        phonebook.add(name='Amanda', number="999998888")
        phonebook.add(name='Laura', number="999998888")

        # Chamada
        resultado = phonebook.get_phonebook_sorted()

        # Avaliacao
        self.assertDictEqual(resultado_esperado, resultado)

    ####### get_phonebook_reverse #######
    def test_phonebook_reverse(self):
        # Setup
        resultado_esperado = {'Ziza': '999998888', 'Amanda': '999999888', 'POLICIA': '190'}
        phonebook = Phonebook()
        phonebook.add(name='Amanda', number="999999888")
        phonebook.add(name='Ziza', number="999998888")

        # Chamada
        resultado = phonebook.get_phonebook_reverse()

        # Avaliacao
        #assert resultado_esperado == resultado
        self.assertDictEqual(resultado_esperado,resultado)

    ####### delete #######
    def test_delete(self):
        # Setup
        name = 'Amanda'
        number = "999999888"
        resultado_esperado = 'Numero deletado'
        phonebook = Phonebook()

        phonebook.add(name=name, number=number)

        # Chamada
        resultado = phonebook.delete(name)

        # Avaliacao
        # assert resultado_esperado == resultado
        assert resultado_esperado == resultado
    def test_delete_nao_existente(self):
        # Setup
        name = 'Amanda'
        number = "999999888"
        resultado_esperado = 'Nome não existente'
        phonebook = Phonebook()
        phonebook.add(name='Beatriz', number=number)

        # Chamada
        resultado = phonebook.delete(name)

        # Avaliacao
        # assert resultado_esperado == resultado
        assert resultado_esperado == resultado
