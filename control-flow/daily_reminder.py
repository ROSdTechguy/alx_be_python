#!/bin/bash
Task = input("Enter your task: ").strip().capitalize()
Priority = input("Priority(high/medium/low): ").strip().lower()
Time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
yes_time = "that requires immediate attention today!"
no_time = "consider completing when you have time"

match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"Reminder: '{Task}' is a {Priority} priority task{yes_time}")
        elif Time_bound == "no":
            print(f"Reminder: '{Task}' is a {Priority} priority task{no_time}")
    
    case "medium":
        if Time_bound == "yes":
            print(f"Attention: '{Task}' is a {Priority} priority task{yes_time}")
        elif Time_bound == "no":
            print(f"Attention: '{Task}' is a {Priority} priority task{yes_time}")

    case "low":
        if Time_bound == "yes":
            print(f"Note: '{Task}' is a {Priority} priority task{yes_time}")
        elif Time_bound == "no":
            print(f"Note: '{Task}' is a {Priority} priority task{yes_time}")
