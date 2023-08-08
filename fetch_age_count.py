"""
Problem statement:
    In the Python file, write a program to perform a GET request on the route
    https://coderbyte.com/api/challenges/json/age-counting which contains a data
    key and the value is a string which contains items in the
    format: key=STRING, age=INTEGER.
    Your goal is to count how many items exist that have an age equal to or greater than 50,
    and print this final value.
    Example Input
    {"data":"key=IAfpK, age=58, key=WNVdi, age=64, key=jp9zt, age=47"}
    Example Output
    2
"""


import requests


class FetchCount:

    def __init__(self, url, age_key, threshold_goal):
        self.url = url
        self.age_key = age_key
        self.threshold_goal = threshold_goal

    def count_items_with_age(self):
        try:
            response = requests.get(self.url)

            # Check if the request was successful (status code 200)
            response.raise_for_status()

            data = response.json().get("data")
            items = data.split(', ')
            age_values = []

            for item in items:
                if self.age_key in item:
                    age = int(item.split(self.age_key + '=')[1])
                    age_values.append(age)

            count = sum(value >= self.threshold_goal for value in age_values)
            return count

        except requests.exceptions.RequestException as e:
            print("Error during the request:", e)
            return None

        except (ValueError, KeyError) as e:
            print("Error processing the response:", e)
            return None

        except Exception as e:
            print("An unexpected error occurred:", e)
            return None

cls_obj = FetchCount(url="https://coderbyte.com/api/challenges/json/age-counting",
                     age_key="age", threshold_goal=50)
result = cls_obj.count_items_with_age()
if result is not None:
    print("-->", result)
