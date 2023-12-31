from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search():
    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')
    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_login_btn_on_saved():

    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with step('Click Saved in bottom menu'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Saved")).click()
    with step('Check button register on the page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/positiveButton")).should(be.clickable and be.visible)


def test_login_btn_on_edits():

    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with step('Click Edits in bottom menu'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/nav_tab_edits")).click()
    with step('Check button register on the page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/positiveButton")).should(be.clickable and be.visible)


def test_login_btn_on_more():

    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with step('Click More in bottom menu'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/nav_more_container")).click()
    with step('Check button register on the page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/main_drawer_login_button")).should(be.clickable and be.visible)


def test_login_btn_on_search_menu():

    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
    with step('Click Search in bottom menu'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.wikipedia.alpha:id/navigation_bar_item_small_label_view" and @text="Search"]')).click()
    with step('Check button register on the page'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/history_empty_title")).should(be.clickable and be.visible and have.text('No recently viewed articles'))
