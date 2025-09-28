def nlq_to_sql(nlq):
    nlq = nlq.lower()

    if "all students" in nlq:
        return "SELECT * FROM students;"

    if "list students" in nlq:
        return "SELECT * FROM students;"

    if "show students" in nlq:
        return "SELECT * FROM students;"

    if "marks greater than 50" in nlq:
        return "SELECT * FROM students WHERE marks > 50;"

    if "marks less than 50" in nlq:
        return "SELECT * FROM students WHERE marks < 50;"

    if "older than 20" in nlq:
        return "SELECT * FROM students WHERE age > 20;"

    if "age greater than 20" in nlq:
        return "SELECT * FROM students WHERE age > 20;"

    if "younger than 20" in nlq:
        return "SELECT * FROM students WHERE age < 20;"

    if "age less than 20" in nlq:
        return "SELECT * FROM students WHERE age < 20;"

    return "Sorry, I cannot understand the query."

# Example usage
user_query = input("Enter query: ")
print("Generated SQL:", nlq_to_sql(user_query))
