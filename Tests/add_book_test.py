from Pages.selected_book_page import SelectedBook
from Pages.user_profile_page import UserBooks
from Pages.login_page import LoginPage
from Pages.header_page import Header
from Tests.data_storage import *

#Goodread is a website for readers and book recommendation, where you can see what books your friends are reading.
#and track the books you're reading, have read, and want to read.
#Test scenario >>> searching and adding a book from the list to shelf functionalaties
#Verify that the user can search the book in header search functionality.
#Verify that users can navigate and choose the book from the searching list
#Verify that the user can add the book to user's "Want to read" shelf.
#Navigate and go to user's shelf and print "want to read" booklist (I did it only for using multiple windows interactions here)
#Go back to user's shelf >> Want to read section
#Delet the book from user's <want to read> list
#i have a problem with assertion

class Test_Search:
    def test_search_book_from_list(self, browser):
        login_pg = LoginPage(browser)
        header_pg = Header(browser)
        browser.get("https://www.goodreads.com/")
        login_pg.with_(correct_username, correct_password)
        header_pg.search_input(book_name)
        results = browser.find_elements_by_tag_name("td")
        results[0].click()
        book_pg = SelectedBook(browser)
        book_pg.add_to_read()
        book_pg.mybook()
        mybook_pg = UserBooks(browser)
        browser.refresh()
        mybook_pg.present_books()
        window_before = browser.window_handles[0]
        browser.find_element_by_link_text("Print").click()
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        browser.find_element_by_link_text("My Books").click()
        browser.switch_to.window(window_before)
        mybook_pg.delete_book()
        browser.switch_to.alert.accept()
        mybook_pg.verify_empty_shelf()





