# -*- coding: utf-8 -*-

from django.test import TestCase
from splinter.browser import Browser
from should_dsl import should

URL = 'http://localhost:8000'

class ContactTest(TestCase):

    def setUp(self):
        self.browser = Browser()
        self.browser.visit(URL)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_acess_contact_page(self):
        self.browser.find_by_name('contact').click()
        self.browser.title |should| equal_to('RiceTeam - Contato')
        
    def test_contact_sucess(self):
        self.browser.find_by_name('contact').click()
        self.browser.fill_in('name', 'Usuário de teste')
        self.browser.fill_in('email', 'usuario_de_teste@teste.com')
        self.browser.fill_in('message', 'Mensagem de teste')
        self.browser.find_by_name('submit').click()
        contact_successful = self.browser.find_by_name('contact_successful')
        contact_successful |should| equal_to('Contato enviado!')
