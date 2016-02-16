from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Contact


class ContactTest(TestCase):
    def test_representation(self):
        contact = Contact(first_name='Valeria', last_name='Chernenko')
        self.assertEqual(str(contact), 'Valeria Chernenko')


class ContactsCRUDTest(TestCase):
    def setUp(self):
        contact = Contact(first_name='Valeria', last_name='Chernenko')
        contact.save()
        self.contacts = [contact]

    def test_list_contacts(self):
        response = self.client.get(reverse('list_contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Valeria' in response.content)

    def test_delete_contacts(self):
        response = self.client.get('/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(r'Valeria' not in response.content)

    def test_edit_contact(self):
        response = self.client.post('/edit/1', {'first_name': ''})
        self.assertFormError(response, 'form', 'first_name', 'This field is required.')

        response = self.client.post('/edit/1', {'first_name': 'Ozel', 'last_name': 'Christo',
                                                'phone': '+49823878172'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('list_contacts'))
        self.assertTrue('Ozel' in response.content)

    def test_create_new_contact(self):
        response = self.client.get('/new', {'first_name': 'Ozel', 'last_name': 'Christo',
                                            'phone': '+49823878172'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse('Valeria' in response.content)
