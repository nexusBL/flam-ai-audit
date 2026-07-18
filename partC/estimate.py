# Constraints

languages = 6

review_hours_per_week = 10

weeks = 2

samples_per_hour = 50

review_capacity = review_hours_per_week * weeks * samples_per_hour

print("Reviewer capacity:", review_capacity)

synthetic_pairs = 50000

print("Synthetic training pairs:", synthetic_pairs)

print("Human review coverage:",
      review_capacity / synthetic_pairs * 100,
      "%")