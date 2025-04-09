Feature: Test Addition Functionality
    Scenario: Addition
      Given Addition app is run
      When I input "1" and "2" to add
      Then I get result as "3"