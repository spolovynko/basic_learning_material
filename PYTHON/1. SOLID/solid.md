# SOLID Principles

The SOLID principles are a set of design guidelines aimed at creating maintainable, scalable, and robust software. Below is a detailed explanation with Python examples and use cases.

---

| Principle                        | Description                                                                                  |
|----------------------------------|----------------------------------------------------------------------------------------------|
| **S - Single Responsibility**    | A class should have only one reason to change, meaning it should have only one responsibility.|
| **O - Open/Closed**              | Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. |
| **L - Liskov Substitution**      | Objects of a superclass should be replaceable with objects of a subclass without altering the correctness of the program. |
| **I - Interface Segregation**    | Clients should not be forced to depend on interfaces they do not use.                       |
| **D - Dependency Inversion**     | High-level modules should not depend on low-level modules. Both should depend on abstractions. |

---

## 1. Single Responsibility Principle (SRP)

### Explanation
Each class should have one responsibility or reason to change. This ensures better maintainability and focus.

### Python Example
```python
class Invoice:
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self, tax):
        return self.amount + (self.amount * tax)

class InvoicePrinter:
    def print_invoice(self, invoice):
        print(f"Invoice Amount: {invoice.amount}")
```

### Use Case
Separating business logic (e.g., calculations) from presentation logic (e.g., printing).

---
## 2. Open/Closed Principle (OCP)
### Explanation
Code should be open for extension but closed for modification. This can be achieved by using inheritance or composition.

### Python Example
```python
Copy
Edit
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, amount):
        pass

class RegularDiscount(Discount):
    def calculate(self, amount):
        return amount * 0.9

class SeasonalDiscount(Discount):
    def calculate(self, amount):
        return amount * 0.8

def get_final_price(amount, discount: Discount):
    return discount.calculate(amount)
```
### Use Case
Adding new functionality (e.g., new discount types) without altering existing code.
---
## 3. Liskov Substitution Principle (LSP)
### Explanation
A subclass should be substitutable for its superclass without affecting program behavior.

### Python Example
```python
Copy
Edit
class Bird:
    def fly(self):
        return "Flying"

class Duck(Bird):
    def fly(self):
        return "Duck flying"

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich can't fly")
```
### Use Case
Avoid substituting classes that break the expected behavior of a parent class (e.g., Ostrich is a bird but doesn't fly).

---
## 4. Interface Segregation Principle (ISP)
### Explanation
A class should not be forced to implement interfaces it does not use.

### Python Example
```python
Copy
Edit
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

class SimplePrinter(Printer):
    def print_document(self):
        print("Printing document")
```
### Use Case
Designing interfaces for devices with different capabilities (e.g., printers vs. multi-function printers).

---
## 5. Dependency Inversion Principle (DIP)
### Explanation
High-level modules should depend on abstractions, not on low-level modules.

### Python Example
```python
Copy
Edit
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

class EmailService(NotificationService):
    def send_message(self, message):
        print(f"Sending Email: {message}")

class SMSService(NotificationService):
    def send_message(self, message):
        print(f"Sending SMS: {message}")

class NotificationManager:
    def __init__(self, service: NotificationService):
        self.service = service

    def notify(self, message):
        self.service.send_message(message)

email_service = EmailService()
sms_service = SMSService()

manager = NotificationManager(email_service)
manager.notify("Hello via Email")

manager = NotificationManager(sms_service)
manager.notify("Hello via SMS")
```
### Use Case

Handling changes in communication mediums (email, SMS, etc.) without altering the notification system's logic.

---
