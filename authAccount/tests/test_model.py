from django.test import TestCase
from authAccount.models import User

# faker pakage create email and other data 
# factory for dummy data create   
# if you create custome test class then you have to delete by default genereted tests.py class 
class UserModelTest(TestCase):
    def test_create_user(self):
        email = "test@example.com"
        name = "test User"
        password ="testpassword"

        user = User.objects.create_user(email=email,name=name,password=password)

        self.assertEqual(user.email , email)
        self.assertEqual(user.name , name) 
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.check_password(password))


    def test_create_superuser(self):
        # test case for create admin
        email = "admin@example.com"
        name = "Admin"
        password = "adminpassword"

        superuser = User.objects.create_superuser(email=email,name=name,password=password)

        self.assertEqual(superuser.email,email)
        self.assertEqual(superuser.name, name)
        self.assertFalse(superuser.is_active)
        self.assertTrue(superuser.is_admin)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.check_password(password))

class UserMethodTest(TestCase):
    def test_get_full_name(self):
        """Test getting the user's full name"""
        user = User(email="test@example.com", name="Test User")
        self.assertEqual(user.get_full_name(), "Test User")

    def test_has_perm(self):
        """Test checking if the user has a specific permission"""
        user = User(email="test@example.com", name="Test User")
        self.assertTrue(user.has_perm("some_permission"))

    def test_has_module_perms(self):
        """Test checking if the user has module permissions"""
        user = User(email="test@example.com", name="Test User")
        self.assertTrue(user.has_module_perms("some_app"))

    def test_is_staff(self):
        """Test checking if the user is staff"""
        user = User(email="test@example.com", name="Test User")
        self.assertFalse(user.is_staff)
