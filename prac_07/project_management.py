from project import Project

FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

def main():
    """Project management program."""
    print("Welcome to the Project Management Program")
    projects = []

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            projects = load_projects(FILENAME)
        elif choice == "S":
            save_projects(FILENAME, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project manager")

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        next(file)  # skip header
        for line in file:
            parts = line.strip().split('\t')
            name, start_date, priority, cost_estimate, completion_percentage = parts
            project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    """Save all projects to the file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    """Display incomplete and complete projects separately, sorted by priority."""
    incomplete = [p for p in projects if p.completion_percentage < 100]
    complete = [p for p in projects if p.completion_percentage == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(complete):
        print(f"  {project}")

from datetime import datetime

def filter_projects(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    filtered_projects = [project for project in projects if datetime.strptime(project.start_date, "%d/%m/%Y").date() > filter_date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(f"  {project}")


def add_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)

def update_project(projects):
    """Update an existing project's completion percentage or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project_to_update = projects[choice]
    except (IndexError, ValueError):
        print("Invalid project choice.")
        return

    new_percentage = input(f"New Percentage (leave blank to keep {project_to_update.completion_percentage}%): ")
    new_priority = input(f"New Priority (leave blank to keep {project_to_update.priority}): ")

    if new_percentage != "":
        try:
            project_to_update.completion_percentage = int(new_percentage)
        except ValueError:
            print("Invalid percentage. No change made.")

    if new_priority != "":
        try:
            project_to_update.priority = int(new_priority)
        except ValueError:
            print("Invalid priority. No change made.")
