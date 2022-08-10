from PageObjectApp import SearchHelper

def registr_your_store(browser):
    register_account_page = SearchHelper(browser)
    register_account_page.go_to_site()
    register_account_page.fill_fields_and_submit()
    elements_of_registration = register_account_page.chek_register_succsess()
    assert "Account" and "Success" in elements_of_registration

