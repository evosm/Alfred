#noinspection CucumberUndefinedStep
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When Выбран клиент "user_test1"
      Then behave will test it for us!