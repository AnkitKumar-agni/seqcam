import numpy as np

class UserName:


    def __init__(self):
        self.name = "no name"
        self.address = "India"
        self.Phone_Number = 000
        self.Consumer_No = 0

    def GetData(self):

        print("Enter the Details")
        print("=====================================")

        self.name = input("Name : ")
        self.address = input("Address : ")
        self.Phone_Number = int(input("Phone Number : "))
        self.Consumer_No = int(input("Consumer Number : "))

    def DisplayAll(self):
        # Function to display details of the customer

        print("Consumer Number : ", self.Consumer_No)
        print("Name : ", self.name)
        print("Phone Number : ", self.Phone_Number)
        print("Address : ", self.address)

    def Search(self):
        # Function to search records

        print("Search Options"
              "1. Through Phone Number"
              "2. Through Consumer Number")

        n = int(input("Enter Your choice "))
        search_Phone = 000

        if n==1:
            Search_Phone = int(input("Enter the phone number "))

            






















