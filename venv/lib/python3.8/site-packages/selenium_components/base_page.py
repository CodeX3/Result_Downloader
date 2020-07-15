from selenium.common import exceptions
from selenium.webdriver.common import keys
from selenium.webdriver.remote.webdriver import WebDriver

from selenium_utils import element


class InstanceRepresentation(object):
    def __repr__(self):
        return str(
            {key: value for key, value in self.__dict__.items()
             if "__" not in key})


class BasePage(InstanceRepresentation):
    def __init__(self, driver: WebDriver):
        self.driver = driver


class Element(InstanceRepresentation):
    """Element class represents primitives in models."""

    def __init__(self, driver, locator):
        super(Element, self).__init__()
        self._driver = driver
        self._locator = locator
        self.element = self.get_element()
        self.text = self.element.text

    def get_element(self):
        """
        Return: selenium.webdriver.remote.webelement.WebElement
        """
        return element.get_when_visible(self._driver, self._locator)

    def click(self):
        """Click on element."""
        self.element.click()

    def click_when_visible(self):
        """Wait for element to be visible and only then performs click."""
        element.get_when_visible(self._driver, self._locator).click()


class Label(Element):
    """Generic label."""


class RichTextInputField(Element):
    """Common class for representation of Rich Text input."""
    def __init__(self, driver, locator):
        """
        Args: driver (CustomDriver):
        """
        super(RichTextInputField, self).__init__(driver, locator)
        self._driver = driver
        self._locator = locator
        self.text = self.element.text

    def enter_text(self, text):
        """Clear fields and enteres text."""
        self.click_when_visible()
        self.element.clear()
        self.element.send_keys(text)
        self.text = text

    def paste_from_clipboard(self, el):
        """
        Paste value from clipboard into text input element.
        Details:
        We want to update value of this element after pasting. In order to
        do that, we click on another element.
        Args: element (Element)
        """
        self.element.clear()
        self.element.send_keys(keys.Keys.CONTROL, 'v')
        el.click()
        el = self._driver.find_element(*self._locator)
        self.text = el.get_attribute("value")


class TextInputField(RichTextInputField):
    """Generic model for text input field."""


class TextFilterDropdown(Element):
    """
    Model for elements which are using autocomplete in text field with dropdown list of found results and static 
    dropdown list of text elements.
    """
    def __init__(self, driver, textbox_locator, dropdown_locator):
        super(TextFilterDropdown, self).__init__(driver, textbox_locator)
        self._locator_dropdown = dropdown_locator
        self._elements_dropdown = None
        self.text_to_filter = None

    def find_and_select_el_by_text(self, text):
        """Find and select text element in dropdown by text."""
        self.text_to_filter = text
        self.element.click()


class Iframe(Element):
    """Iframe element methods."""

    def find_iframe_and_enter_data(self, text):
        """
        Args: text (basestring): string want to enter
        """
        iframe = element.get_when_visible(self._driver, self._locator)
        self._driver.switch_to.frame(iframe)
        el = self._driver.find_element_by_tag_name("body")
        el.clear()
        el.send_keys(text)
        self._driver.switch_to.default_content()
        self.text = text


class DatePicker(Element):
    """Date picker element methods."""
    def __init__(self, driver, date_picker_locator, field_locator):
        """
        Args:
        date_picker_locator (tuple)
        field_locator (tuple): locator of field we have to click on to
        activate date picker
        """
        super(DatePicker, self).__init__(driver, field_locator)
        self._locator_datepcker = date_picker_locator
        self._element_datepicker = None

    def get_day_els_current_month(self):
        """Get day elements for current month.
        Return: list of selenium.webdriver.remote.webelement.WebElement
        """
        self.element.click()
        elements = self._driver.find_elements(*self._locator_datepcker)
        return elements

    def select_day_in_current_month(self, day):
        """Select day - sequential element from date picker. Days go from 0 to
        28,29 or 30, depending on current month. Since we're selecting an element
        from list, we can pass e.g. -1 to select last day in month.
        Args: day (int)
        """
        elements = self.get_day_els_current_month()
        elements[day].click()
        # wait for fadeout in case we're above some other element
        element.get_when_invisible(self._driver, self._locator_datepcker)
        self.text = self.element.get_attribute("value")

    def select_month_end(self):
        """Select last day of current month."""
        elements = self.get_day_els_current_month()
        elements[-1].click()
        # wait for fadeout in case we're above some other element
        element.get_when_invisible(self._driver, self._locator_datepcker)
        self.text = self.element.get_attribute("value")

    def select_month_start(self):
        """Select first day of current month."""
        elements = self.get_day_els_current_month()
        elements[0].click()
        # wait for fadeout in case we're above some other element
        element.get_when_invisible(self._driver, self._locator_datepcker)
        self.text = self.element.get_attribute("value")


class Button(Element):
    """Generic button element."""
    def get_element(self):
        return element.get_when_clickable(self._driver, self._locator)


class Checkbox(Element):
    """Generic checkbox element."""
    def __init__(self, driver, locator):
        super(Checkbox, self).__init__(driver, locator)
        self.is_checked = self.element.is_selected()

    def get_element(self):
        return element.get_when_clickable(self._driver, self._locator)

    def check(self):
        if not self.is_checked:
            self.element.click()

    def uncheck(self):
        if self.is_checked:
            self.element.click()


class Toggle(Element):
    """
    Generic toggle element.
    Note that special function is used for detecting if element is active
    which may not work on an arbitrary element.
    """
    def __init__(self, driver, locator, is_active_attr_val="active"):
        super(Toggle, self).__init__(driver, locator)
        self.is_activated = element.is_value_in_attr(
            self.element, value=is_active_attr_val)

    def get_element(self):
        return element.get_when_clickable(self._driver, self._locator)

    def toggle(self, on_el=True):
        """Click on element based on is_active status and "on" arg.
        Args: on_el (bool)
        """
        if on_el and not self.is_activated:
            self.element.click()
            self.is_activated = True
        elif not on_el and self.is_activated:
            self.element.click()
            self.is_activated = False


class Tab(Element):
    """Generic element representing tab."""
    def __init__(self, driver, locator, is_activated=True):
        super(Tab, self).__init__(driver, locator)
        self.is_activated = is_activated

    def get_element(self):
        return element.get_when_clickable(self._driver, self._locator)

    def click(self):
        """When clicking on tab to first make sure it's clickable i.e.
        that this element will receive click."""
        element.get_when_clickable(self._driver, self._locator).click()
        self.is_activated = True


class Dropdown(Element):
    """Generic dropdown."""


class DropdownStatic(Element):
    """Dropdown with predefined static elements."""

    def __init__(self, driver, dropdown_locator, elements_locator):
        super(DropdownStatic, self).__init__(driver, dropdown_locator)
        self._locator_dropdown_elements = elements_locator
        self.elements_dropdown = self._driver.find_elements(
            *self._locator_dropdown_elements)

    def click(self):
        self.element.click()

    def select(self, member_name):
        """Selects dropdown element based on dropdown element name."""
        for el in self.elements_dropdown:
            if el.get_attribute("value") == member_name:
                el.click()
                break
        else:
            exceptions.NoSuchElementException(member_name)


class Component(InstanceRepresentation):
    """Component class is container for elements."""
    def __init__(self, driver):
        self._driver = driver


class AnimatedComponent(Component):
    """
    Class for components where animation must first complete before elements are visible.
    """
    def __init__(self, driver, locators_to_check, wait_until_visible):
        """
        Args:
        driver (CustomDriver)
        locators_to_check (list of tuples): locators to wait for to become
        (in)visible
        wait_until_visible (bool): for all elements to be visible do we
        have to wait for certain elements to be invisible or visible?
        """
        super(AnimatedComponent, self).__init__(driver)
        self._locators = locators_to_check
        if wait_until_visible:
            self._wait_until_visible()
        else:
            self._wait_until_invisible()

    def _wait_until_visible(self):
        for item_locator in self._locators:
            element.get_when_visible(self._driver, item_locator)

    def _wait_until_invisible(self):
        for item_locator in self._locators:
            element.get_when_invisible(self._driver, item_locator)


class Modal(Component):
    """Generic modal element."""


class FilterCommon(Component):
    """Common filter elements for LHN and Tree View."""
    def __init__(self, driver, text_box_locator, bt_submit_locator, bt_clear_locator):
        super(FilterCommon, self).__init__(driver)
        self.text_box = TextInputField(driver, text_box_locator)
        self.button_submit = Button(driver, bt_submit_locator)
        self.button_clear = driver.find_element(*bt_clear_locator)

    def enter_query(self, query):
        """Enter query to field."""
        self.text_box.enter_text(query)

    def submit_query(self):
        """Submit query that was entered to field."""
        self.button_submit.click()

    def clear_query(self):
        """Clear query that was entered to field."""
        self.button_clear.click()


class AbstractPage(Component):
    """Represent page that can be navigate to, but we don't necessarily know it's url in advance."""
    def __init__(self, driver):
        """
        Args: driver (CustomDriver)
        """
        super(AbstractPage, self).__init__(driver)
        self.url = driver.current_url


class Page(AbstractPage):
    """
    Page class represents components with special properties i.e. they have *static* URL-s, can be navigated to etc.
    """
    def __init__(self, driver):
        """
        Args: driver (CustomDriver)
        """
        super(Page, self).__init__(driver)


class DropdownDynamic(AnimatedComponent):
    """Dropdown that doesn't load all contents at once."""

    def __init__(self, driver, locators_to_check, wait_until_visible):
        """
        Args:
        driver (CustomDriver)
        locators_to_check (list of tuples): locators to wait for to become
        (in)visible
        wait_until_visible (bool): for all elements to be visible do we
        have to wait for certain elements to be invisible or visible?
        """
        super(DropdownDynamic, self).__init__(driver, locators_to_check, wait_until_visible)
        self.members_visible = None
        self.members_loaded = None

    def _update_loaded_members(self):
        """New members that are loaded are added to members_loaded container."""
        raise NotImplementedError

    def _set_visible_members(self):
        """
        When moving in dropdown it can happen we don't always see all the members. Here we set members, that are visible
        to user.
        """
        raise NotImplementedError

    def scroll_down(self):
        raise NotImplementedError

    def scroll_up(self):
        raise NotImplementedError


class Selectable(Element):
    """Representing list of elements that are selectable."""


class ListCheckboxes(Component):
    """Generic list of checkboxes elements."""
    def __init__(self, driver, titles_locator, checkboxes_locator):
        super(ListCheckboxes, self).__init__(driver)
        self.locator_titles = titles_locator
        self.locator_checkboxes = checkboxes_locator

    @staticmethod
    def _unselect_unnecessary(objs, list_titles):
        """Unselect unnecessary elements according objs (titles and checkboxes elements) and list of titles."""
        unselect = [obj[1].click() for obj in objs
                    if obj[0].text not in list_titles if obj[1].is_selected()]
        return unselect

    @staticmethod
    def _select_necessary(objs, list_titles):
        """Select necessary elements according objs (titles and checkboxes elements) and list of titles."""
        select = [obj[1].click() for obj in objs
                  if obj[0].text in list_titles if not obj[1].is_selected()]
        return select

    def select_by_titles(self, list_titles):
        """Select checkboxes according titles."""
        element.get_when_all_visible(self._driver, self.locator_titles)
        objs_titles = self._driver.find_elements(*self.locator_titles)
        objs_checkboxes = self._driver.find_elements(*self.locator_checkboxes)
        objs = zip(objs_titles, objs_checkboxes)
        self._unselect_unnecessary(objs, list_titles)
        self._select_necessary(objs, list_titles)
