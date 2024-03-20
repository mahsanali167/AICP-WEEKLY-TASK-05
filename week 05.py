class CarParkSystem:
    def __init__(self):
        self.daily_total_payments = 0

    def calculate_price(self, day, arrival_hour, hours_parked, frequent_parking_num=None):
        # Constants for pricing and discounts
        hourly_rates = {
            'Sunday': {'day_rate': 2.00, 'evening_rate': 2.00},
            'Monday': {'day_rate': 10.00, 'evening_rate': 2.00},
            'Tuesday': {'day_rate': 10.00, 'evening_rate': 2.00},
            'Wednesday': {'day_rate': 10.00, 'evening_rate': 2.00},
            'Thursday': {'day_rate': 10.00, 'evening_rate': 2.00},
            'Friday': {'day_rate': 10.00, 'evening_rate': 2.00},
            'Saturday': {'day_rate': 3.00, 'evening_rate': 2.00}
        }
        evening_discount = 0.5 if 16 <= arrival_hour <= 23 else 0.1

        if day not in hourly_rates:
            print("Error: Invalid day entered.")
            return None

        if arrival_hour < 8 or arrival_hour >= 24:
            print("Error: Parking is not allowed between Midnight and 08:00.")
            return None

        if frequent_parking_num:
            if not self.validate_frequent_parking_num(frequent_parking_num):
                print("Error: Incorrect frequent parking number.")
                return None
            else:
                evening_discount = 0.5

        if arrival_hour < 16:
            total_price = hours_parked * hourly_rates[day]['day_rate']
        else:
            total_price = hours_parked * hourly_rates[day]['evening_rate']

        total_price *= (1 - evening_discount)
        return total_price

    def validate_frequent_parking_num(self, num):
        if len(num) != 5 or not num.isdigit():
            return False
        check_digit = int(num[-1])
        num_sum = sum(int(digit) * (i + 1) for i, digit in enumerate(num[:-1]))
        calculated_check_digit = num_sum % 11
        return calculated_check_digit == check_digit

    def process_payment(self, amount_paid):
        self.daily_total_payments += amount_paid

    def display_daily_total(self):
        print(f"Total payments for the day: {self.daily_total_payments}")


# Sample usage of the CarParkSystem class
if __name__ == "__main__":
    system = CarParkSystem()

    # Task 1 - Calculate price
    day = input("Enter day of the week: ")
    arrival_hour = int(input("Enter arrival hour (0-23): "))
    hours_parked = int(input("Enter number of hours parked: "))
    frequent_parking_num = input("Enter frequent parking number (if available): ")

    price = system.calculate_price(day, arrival_hour, hours_parked, frequent_parking_num)
    if price is not None:
        print(f"Total price to park: {price:.2f}")

    # Task 2 - Process payment and display daily total
    amount_paid = float(input("Enter amount paid: "))
    if amount_paid >= price:
        system.process_payment(amount_paid)
        print("Payment processed successfully.")
        system.display_daily_total()

    # Task 3 - Making payments fairer
    # Example: arriving at 14:45 on a Sunday, parking for five hours
    revised_price = system.calculate_price('Sunday', 14, 5) + system.calculate_price('Sunday', 16, 1)
    print(f"Revised price: {revised_price:.2f}")
