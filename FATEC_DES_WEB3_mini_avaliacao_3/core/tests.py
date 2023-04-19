from msilib.schema import SelfReg
from typing import Self
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
class FeriadoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp, 'não é feriado')
        
from django.test import TestCase
class NatalTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)
    def test_texto(self):
        self.assertContains(self.resp, 'natal')
    def test_template_natal(self):
        self.assertTemplateUsed(self.resp, 'natal.html')
        
from feriados import FeriadoModel
from datetime import datetime
class FeriadoModelTest(TestCase):
    def setUp(self):
        self.feriado = 'Natal'
        self.mes = 12
        self.dia = 25
        self.cadastro = FeriadoModel(
    nome=self.feriado,
    dia=self.dia,
    mes=self.mes,
)
        self.cadastro.save()
    def test_created(self):
        self.assertTrue(FeriadoModel.objects.exists())
    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)
    def test_nome_feriado(self):
        nome = self.cadastro.__dict__.get('nome', '')
        Self.assertEqual(nome, self.feriado)
    def test_dia_feriado(self):
        dia = self.cadastro.__dict__.get('dia', '')
        SelfReg.assertEqual(dia, self.dia)