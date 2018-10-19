from behave import *
from main import test, Users


@given('we have behave installed')
def step_impl(context):
    pass

@when('Выбран клиент "{user_type}"')
def step_impl(contex, user_type):
    usr = Users.Users(user_type)
    assert usr.get_user()



@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False