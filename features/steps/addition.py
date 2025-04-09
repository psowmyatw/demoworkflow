from behave import given, when, then
from src.hello import add


@given("Addition app is run")
def step_imp(context):
    print("STEP: Given Addition app is run")
    pass


@when('I input "{inp1}" and "{inp2}" to add')
def step_imp(context, inp1, inp2):
    print(f'STEP: When I input "{inp1}" and "{inp2}" to add')
    context.result = add(int(inp1), int(inp2))


@then('I get result as "{out}"')
def step_imp(context, out):
    print(f'STEP: Then I get result as "{out}"')
    assert context.result == int(out), f"Expected {out}, got {context.result}"
