from src.helpers.check_input import CheckInput

check_input = CheckInput()


def set_options_on_site():
    items = {
        'local': check_input.local_data(),
        'provider': check_input.provider_data(),
        'subsection': check_input.subsection_data(),
        'month_one': check_input.month_data(1),
        'month_two': check_input.month_data(2),
        'month_three': check_input.month_data(3),
    }
    return items
