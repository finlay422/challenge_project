from django.test import TestCase, Client
from .models import Address, Person
import json


class PeopleTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_data = {}

        address_1 = Address.objects.create(number=123, street='test st', city='test city', state='NSW')
        self.test_data['person_1'] = Person.objects.create(email='test@example.com', name='test user',
                                                           address=address_1)
        address_2 = Address.objects.create(number=321, street='test st 123', city='test city 123', state='VIC')
        self.test_data['person_2'] = Person.objects.create(email='test123@example.com', name='test user 123',
                                                           address=address_2)

    def test_people_query(self):
        query = '{ people { email name address { number street city state } } }'
        response = self.client.post('/graphql', {'query': query}, content_type='application/json')

        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertIn('data', content)
        self.assertIn('people', content['data'])

        person = content['data']['people'][0]
        expected_person = self.test_data['person_1']

        self.assertEqual(person['email'], expected_person.email)
        self.assertEqual(person['name'], expected_person.name)
        self.assertEqual(person['address']['number'], expected_person.address.number)
        self.assertEqual(person['address']['street'], expected_person.address.street)
        self.assertEqual(person['address']['city'], expected_person.address.city)
        self.assertEqual(person['address']['state'], expected_person.address.state)

    def test_people_pagination_query(self):
        query = '{ people(pageSize: 1, pageOffset: 1) { email name address { number street city state } } }'
        response = self.client.post('/graphql', {'query': query}, content_type='application/json')

        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content)
        self.assertIn('data', content)
        self.assertIn('people', content['data'])

        person = content['data']['people'][0]
        expected_person = self.test_data['person_2']

        self.assertEqual(person['email'], expected_person.email)
        self.assertEqual(person['name'], expected_person.name)
        self.assertEqual(person['address']['number'], expected_person.address.number)
        self.assertEqual(person['address']['street'], expected_person.address.street)
        self.assertEqual(person['address']['city'], expected_person.address.city)
        self.assertEqual(person['address']['state'], expected_person.address.state)

        self.assertEqual(len(content['data']['people']), 1)
