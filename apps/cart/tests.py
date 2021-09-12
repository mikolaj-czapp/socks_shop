from django.test import TestCase, Client
from django.urls import reverse
from apps.cart.models import Cart, ProductCart
from apps.product.models import Brand, Category, Product
from apps.user.models import MyUser


class CartByUserTest(TestCase):
    def setUp(self):
        # create two users
        test_user_1 = MyUser.objects.create_user(
            username='testuser1',
            password='1X<ISRUkw+tuK',
            email='test1@test.com',
            city='testcity1',
            street='teststreet1',
            postal_code='00-001',
        )
        test_user_2 = MyUser.objects.create_user(
            username='testuser2',
            password='1X<ISRUkw+Kut',
            email='test2@test.com',
            city='testcity2',
            street='teststreet2',
            postal_code='00-002',
        )
        test_user_1.save()
        test_user_2.save()

        # Create a product
        test_name = 'test_name'
        test_brand = Brand.objects.create(name='test_brand')
        test_description = 'test_description'
        test_category = Category.objects.create(name='test_category')
        test_price = 10
        test_product = Product.objects.create(
            name=test_name,
            brand=test_brand,
            description=test_description,
            category=test_category,
            price=test_price,
        )
        test_product.save()

        # Create 10 ProductCarts
        number_of_product_carts = 10
        for i in range(number_of_product_carts):
            user = test_user_1 if i % 2 else test_user_2
            ProductCart.objects.create(
                user=user,
                product=test_product,
                quantity=i,
            )

        # Create a cart
        test_items_for_cart = ProductCart.objects.all()
        test_cart_1 = Cart.objects.create(user=test_user_1)
        test_cart_1.items.set(test_items_for_cart)
        test_cart_1.save()
        test_cart_2 = Cart.objects.create(user=test_user_2)
        test_cart_2.items.set(test_items_for_cart)
        test_cart_2.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('cart_by_user'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/user/login?'))

    def test_cart(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('cart_by_user'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'shopping/cart.html')

        self.assertTrue('object' in response.context)

        