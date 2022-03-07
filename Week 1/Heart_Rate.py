"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

user_age = float(input("\nWhat is your Age? "))
maximun = 220 - user_age
x1 = maximun * 0.65
x2 = maximun * 0.85
print(f"\nYour Exercise Heart Rate Range is {x1:1.0f}-{x2:1.0f}bpm\n")