from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

class HomePageTestCase(SimpleTestCase):

    def setUp(self) -> None:
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200) 

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_containts_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_containts_correct_html(self):
        self.assertNotContains(self.response, 'Hello. I shoul not be on the page')

    def test_homepage_url_resolves_homepageview(self):
        '''
        Проверяет является обработчиком выбранная функция
        '''
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)