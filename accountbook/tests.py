import json

from django.test import TransactionTestCase, Client

from users.models import User
from accountbook.models import AccountBook


class PostAccountBookTest(TransactionTestCase):
    def setUp(self):
        User.objects.create(
            id=6,
            created_at='2022-12-25',
            updated_at='2022-12-25',
            name='재환',
            email='asd123@gmail.com',
            password='asd123@@@'
        )

        AccountBook.objects.create(
            id='12',
            created_at='2022-12-25',
            updated_at='2022-12-25',
            amount='1000',
            amount_detail='커피',
            note_content='스타벅스',
            url='',
            user_id='6'
        )

    def tearDown(self):
        User.objects.all().delete()
        AccountBook.objects.all().delete()

    def test_fail_expired_token_with_post_method(self):
        client = Client()
        accountbook = {
            'amount': '2000',
            'amount_detail': '스타벅스',
            'note_content': '커피가맛이없다',
            'url': ''
        }
        headers = {'HTTP_Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwiZXhwIjoxNjcxOTQyMzMxfQ.QdP34loAuSClJweOjvRCKI5E1pdP7lz2AgdIEd2lbOs'}
        response = client.post('/accountbook/post', json.dumps(accountbook), content_type='application.json', **headers)

        self.assertEqual(response.status_code, 408)
        self.assertEqual(response.json(),
                         {
                             'message': 'Expired_Token'
                         })

    def test_fail_invalid_token_with_post_method(self):
        client = Client()
        accountbook = {
            'amount': '2000',
            'amount_detail': '스타벅스',
            'note_content': '커피가맛이없다',
            'url': ''
        }
        headers = {'HTTP_Authorization': 'CI6NiwiZXhwIjoxNjcxOTQyMzMxfQ.QdP34loAuSClJweOjvRCKI5E1pdP7lz2AgdIEd2lbOs'}
        response = client.post('/accountbook/post', json.dumps(accountbook), content_type='application.json', **headers)

        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json(),
                         {
                             'message': 'Invalid_Token'
                         })

    def test_fail_invalid_user_with_post_method(self):
        client = Client()
        accountbook = {
            'amount': '2000',
            'amount_detail': '스타벅스',
            'note_content': '커피가맛이없다',
            'url': ''
        }
        headers = {'HTTP_Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjIsImV4cCI6MTY3MjAyODk1NX0.La9LLNdJzk89I-Q6wjS4p647kNlBuCBlnLeJIK4LeR0'}
        response = client.post('/accountbook/post', json.dumps(accountbook), content_type='application.json', **headers)

        self.assertEqual(response.status_code, 407)
        self.assertEqual(response.json(),
                         {
                             'message': 'Invalid_User'
                         })

    def test_success_post_account_book_with_post_method(self):
        client = Client()
        accountbook = {
            'amount': '2000',
            'amount_detail': '스타벅스',
            'note_content': '커피가맛이없다',
            'url': ''
        }
        headers = {'HTTP_Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwiZXhwIjoxNjcyMDI3MTg1fQ.vOGOraN-xqyC_oLSgwXHauttyldREkPyd-ryibV9vtg'}
        response = client.post('/accountbook/post', json.dumps(accountbook), content_type='application.json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),
                         {
                             'message': 'Success'
                         })

    def test_fail_key_error_with_post_method(self):
        client = Client()
        accountbook = {
            'amount': '3000',
            'note_content': '커피가맛이없다',
            'url': ''
        }
        headers = {'HTTP_Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwiZXhwIjoxNjcyMDI3MTg1fQ.vOGOraN-xqyC_oLSgwXHauttyldREkPyd-ryibV9vtg'}
        response = client.post('/accountbook/post', json.dumps(accountbook), content_type='application.json', **headers)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),
                         {
                             'message': 'Key_Error'
                         })

    def test_fail_value_error_with_post_method(self):
        client = Client()
        accountbook = {
            'amount': '1.0',
            'amount_detail': '스타벅스',
            'note_content': '커피가맛이없다',
            'url': ''
        }
        headers = {'HTTP_Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwiZXhwIjoxNjcyMDI3MTg1fQ.vOGOraN-xqyC_oLSgwXHauttyldREkPyd-ryibV9vtg'}
        response = client.post('/accountbook/post', json.dumps(accountbook), content_type='application.json', **headers)

        self.assertEqual(response.status_code, 408)
        self.assertEqual(response.json(),
                         {
                             'message': 'Value_Error'
                         })


class GetAccountBookTest(TransactionTestCase):
    def setUp(self):
        User.objects.create(
            id=6,
            created_at='2022-12-25',
            updated_at='2022-12-25',
            name='재환',
            email='asd123@gmail.com',
            password='asd123@@@'
        )

        AccountBook.objects.create(
            id='12',
            created_at='2022-12-25',
            updated_at='2022-12-25',
            amount='1000',
            amount_detail='커피',
            note_content='스타벅스',
            url='',
            user_id='6'
        )

    def tearDown(self):
        User.objects.all().delete()
        AccountBook.objects.all().delete()

    def test_success_account_book_with_get_method(self, user_id=6):
        client = Client()
        header = {'HTTP_Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NiwiZXhwIjoxNjcyMDI3MTg1fQ.vOGOraN-xqyC_oLSgwXHauttyldREkPyd-ryibV9vtg'}
        response = client.get(f'/accountbook/get/{user_id}', content_type='application.json', **header)

        accountbooks = AccountBook.objects.filter(user_id=user_id)

        self.assertEqual(response.json(),
                         {
                             'message': [{
                                 'userId': accountbook.user_id,
                                 'accountbookId': accountbook.id,
                                 'amount': accountbook.amount,
                                 'amount_detail': accountbook.amount_detail,
                                 'note_content': accountbook.note_content
                             }for accountbook in accountbooks]
                         })
        self.assertEqual(response.status_code, 200)