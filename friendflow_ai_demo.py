import json
import os

class FriendFlowAI:
    def __init__(self, data_file='friendflow_data.json'):
        self.data_file = data_file
        self.tasks = self._load_data()

    def _load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def _save_data(self):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def add_task(self, description, category="Uncategorized"):
        # Simulates converting complex thought to actionable step
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "category": category,
            "status": "Open" # Represents a clear action
        }
        self.tasks.append(task)
        self._save_data()
        print(f"Task added: '{description}' in category '{category}'.")

    def view_tasks(self, category=None):
        print("\n--- Your FriendFlow Board ---")
        filtered_tasks = self.tasks
        if category:
            filtered_tasks = [t for t in self.tasks if t['category'].lower() == category.lower()]
            print(f"Filtering by category: {category}")

        if not filtered_tasks:
            print("No tasks found.")
            return

        for task in filtered_tasks:
            print(f"[{task['status']}] {task['id']}. {task['description']} ({task['category']})")
        print("----------------------------")

    def update_status(self, task_id, new_status):
        # Simulates progress tracking on actionable steps
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = new_status
                self._save_data()
                print(f"Task {task_id} status updated to '{new_status}'.")
                return
        print(f"Task with ID {task_id} not found.")

    def remove_task(self, task_id):
        initial_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        if len(self.tasks) < initial_len:
            self._save_data()
            print(f"Task {task_id} removed.")
        else:
            print(f"Task with ID {task_id} not found.")

if __name__ == "__main__":
    # Initialize the local, private task board
    board = FriendFlowAI()

    # Example: Converting complex thoughts into actionable tasks
    print("Adding initial tasks...")
    board.add_task("Araştırma makalesini gözden geçir", "Akademik")
    board.add_task("Yeni özellik için prototip oluştur", "Proje X")
    board.add_task("Aile ile akşam yemeği planla", "Kişisel")
    board.add_task("Kullanıcı geri bildirimlerini analiz et", "Proje X")

    # View all tasks
    board.view_tasks()

    # View tasks by category
    board.view_tasks(category="Proje X")

    # Update task status (moving from complex thought to completed action)
    board.update_status(1, "In Progress")
    board.update_status(3, "Completed")

    # View tasks again to see status changes
    board.view_tasks()

    # Remove a task
    board.remove_task(2)
    board.view_tasks()

    print("\nFriendFlow AI demo finished. Data saved to friendflow_data.json")
