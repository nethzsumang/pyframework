from framework.MVC.Controller import Controller


class IndexController(Controller):
    @staticmethod
    def index(o_app, a_params):
        print("This is " + o_app.get("APP", "APP_NAME") + " app.")
        from app.models.User import User

        o_app.dump(
            User().insert(
                {
                    "first_name": "Test2",
                    "last_name": "Admin2",
                    "email": "admin2@example.com",
                    "password": "$2y$10$je12Oah47rm6bJXKiYW.que30T7NzWgKu9KeSei5PnKTAhhVCe5SC",
                    "created_at": "2018-09-10 03:07:24",
                    "updated_at": "2018-09-10 03:07:24",
                }
            )
        )
        o_app.dump(
            User()
            .where("first_name", "=", "Test2")
            .update({"first_name": "Updated Test2"})
        )
        o_app.dump(User().where("id", ">=", "1").select(["id", "first_name", "last_name"]))
        o_app.dump(User().where("first_name", "=", "Updated Test2").delete())
        o_app.dump(User().where("id", ">=", "1").select(["id", "first_name", "last_name"]))
        return Controller.redirect(False)
