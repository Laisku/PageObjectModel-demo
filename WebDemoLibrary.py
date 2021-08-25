from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver


class WebDemoLibrary:

    def __init__(self):
        self.page = LoginPage(self)
        self.pages = {'Login': self.page,
                      'Welcome': WelcomePage(self),
                      'Error': ErrorPage(self)}
        self.browser = None

    def get_keyword_names(self):
        return self._get_keyword_names(self) + self._get_keyword_names(self.page)

    def _get_keyword_names(self, library):
        return [name for name in dir(library) if self._is_keyword(name, library)]

    def _is_keyword(self, name, library):
        if name.startswith('_'):
            return False
        kw = getattr(library, name)
        return hasattr(kw, 'robot_name')

    def __getattr__(self, name):
        try:
            return getattr(self.page, name)
        except AttributeError:
            raise AttributeError(name)

    @keyword
    def close_browser(self):
        if self.browser:
            self.browser.close()
        self.browser = None

    def new_page(self, name):
        self.page = self.pages[name]
        self.page.should_be_on_correct_page()
        BuiltIn().reload_library(self)


class Page:
    title = None

    def __init__(self, ctx):
        self.ctx = ctx

    @property
    def browser(self):
        return self.ctx.browser

    @browser.setter
    def browser(self, browser):
        self.ctx.browser = browser

    def should_be_on_correct_page(self):
        if self.browser.title != self.title:
            raise AssertionError(f"Expected to be on '{self.title}' but was "
                                 f"on '{self.browser.title}'.")

    def find(self, selector):
        return self.browser.find_element_by_css_selector(selector)


class LoginPage(Page):
    title = 'Login Page'
    url = 'http://localhost:7272'

    @keyword
    def open_browser_to_login_page(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.url)
        self.should_be_on_correct_page()

    @keyword
    def login_page_should_be_open(self):
        self.should_be_on_correct_page()

    @keyword
    def login(self, username, password, next_page='Welcome'):
        self.find('#username_field').send_keys(username)
        self.find('#password_field').send_keys(password)
        self.find('#login_button').click()
        self.ctx.new_page(next_page)


class WelcomePage(Page):
    title = 'Welcome Page'

    @keyword
    def welcome_page_should_be_open(self):
        # Tämä on vähän turha, koska oikealle sivulle päätyminen tarkistetaan
        # jo kun kirjasto vaihtaa sivua.
        self.should_be_on_correct_page()

    @keyword
    def logout(self):
        self.find('a').click()
        self.ctx.new_page('Login')


class ErrorPage(Page):
    title = 'Error Page'

    @keyword
    def error_page_should_be_open(self):
        self.should_be_on_correct_page()
