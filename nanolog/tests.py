from django.test import TestCase
from nanolog.models import Nanolog
from nanolog.utils import nanolog
from django.contrib.auth.models import User


class SimpleTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
                username='test', email='test@test', password='test')


    def test_nanolog(self):
        logs = Nanolog.objects.all()
        self.assertEquals(logs.count(), 0)
        nanolog(self.user, 'access', 'user')
        self.assertEquals(logs.count(), 1)
        self.assertEquals(logs[0].school, 'school_dev')
        self.assertEquals(logs[0].details, 'access#user')
        self.assertEquals(logs[0].note, None)
        nanolog(self.user, 'wrong_type', 'user')
        self.assertEquals(logs.count(), 1)
        nanolog(self.user, 'access', '')
        self.assertEquals(logs.count(), 2)
        self.assertEquals(logs[0].school, 'school_dev')
        self.assertEquals(logs[0].details, 'access#')
        self.assertEquals(logs[0].note, None)
        nanolog(self.user, 'login', 'user')
        self.assertEquals(logs.count(), 3)
        self.assertEquals(logs[0].school, 'school_dev')
        self.assertEquals(logs[0].details, 'login#user')
        self.assertEquals(logs[0].note, None)
        nanolog(self.user, 'failed_login', 'user')
        self.assertEquals(logs.count(), 4)
        self.assertEquals(logs[0].school, 'school_dev')
        self.assertEquals(logs[0].details, 'failed_login#user')
        self.assertEquals(logs[0].note, None)
        nanolog(self.user, 'failed_login', 'user', 'note')
        self.assertEquals(logs.count(), 5)
        self.assertEquals(logs[0].school, 'school_dev')
        self.assertEquals(logs[0].details, 'failed_login#user')
        self.assertEquals(logs[0].note, 'note')
