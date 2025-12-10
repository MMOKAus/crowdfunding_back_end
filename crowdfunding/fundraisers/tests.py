from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Fundraiser, Pledge


class UserTests(TestCase): #user creation
    def setUp(self):
        self.client = APIClient()

    def test_user_creation(self):
        data = {
            "username": "testuser",
            "password": "testpassword123",
            "email": "test@example.com"
        }
        response = self.client.post("/users/", data, format="json")
        
       
        self.assertEqual(response.status_code, 201)
        
        
        user_exists = get_user_model().objects.filter(username="testuser").exists()
        self.assertTrue(user_exists)

class FundraiserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username="creator",
            password="testpass123"
        )
        self.client.force_authenticate(user=self.user)

    def test_fundraiser_creation(self):
        data = {
            "title": "Save the Forests",
            "description": "Help us plant trees",
            "goal": 500,
            "image": "",
            "is_open": True
        }
        response = self.client.post("/fundraisers/", data, format="json")

    
        self.assertEqual(response.status_code, 201)

        
        self.assertEqual(Fundraiser.objects.count(), 1)

        fundraiser = Fundraiser.objects.first()
        self.assertEqual(fundraiser.owner, self.user)

class PledgeTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create user
        self.user = get_user_model().objects.create_user(
            username="supporter",
            password="testpass123"
        )
        self.client.force_authenticate(user=self.user)

    
        self.fundraiser = Fundraiser.objects.create(
            title="Save Tigers",
            description="Help wildlife rescue",
            goal=1000,
            is_open=True,
            owner=self.user
        )

    def test_pledge_creation(self):
        data = {
            "amount": 50,
            "comment": "I support this!",
            "anonymous": False,
            "fundraiser": self.fundraiser.id
        }

        response = self.client.post("/pledges/", data, format="json")
        
        
        self.assertEqual(response.status_code, 201)

        # Pledge created
        self.assertEqual(Pledge.objects.count(), 1)

        pledge = Pledge.objects.first()
        self.assertEqual(pledge.supporter, self.user)




