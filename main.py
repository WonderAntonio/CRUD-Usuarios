from models.database import DatabaseModel
from views.user_view import UserView
from controllers.user_controller import UserController

if __name__ == "__main__":
    model = DatabaseModel()
    view = UserView()
    controller = UserController(model, view)
    view.mainloop()