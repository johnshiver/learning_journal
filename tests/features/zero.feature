Feature: Learning Journal
    In order to test new learning
    journal feature we'll test a
    local server with a mock client

    Scenario: Request Homepage
        Given I have a Client
        When I request the page "/"
        Then the page loads succesfully

    Scenario: Request Edit
        Given I have a Client
        When I request the page "/edit/1"
        Then the page loads succesfully

    Scenario: Edit blog test
        Given I have a Client
        When I request the page "/edit/2"
        Then the page loads new submission form with old text