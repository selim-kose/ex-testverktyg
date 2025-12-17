## U1

#som en anvvändare vill jag vill jag kunna favoritmarkera böcker och ett hjärta läggs till vid sidan av titeln i katalogvyn
#så att jag kan se vilka böcker som har lagts till som mina favoriter i katalogvyn

Feature: Add favorite marking

  Scenario: Add favorite marking
    Given user is on the main page
    When user clicks on a heart icon next to a book title
    Then the heart icon should be filled, indicating the book is marked as favorite 
